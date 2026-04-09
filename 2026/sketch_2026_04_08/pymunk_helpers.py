"""
pymunk_helpers.py

Experimental module to help simplify playing with physics
simulations using  pymunk <pymunk.org> and py5 <py5coding.org>
It requires pymunk, shapely, trimesh and mapbox_earcut
"""
from collections.abc import Sequence

import py5
import pymunk
import shapely
from trimesh.creation import triangulate_polygon # pip install trimesh[easy]

class Simulation:
    """Inits a pymunk.Space object, keeps track and draws simulated objects.""" 
    _default = None
    mass_scale = 0.1
    poly_friction = 0.99
    box_friction = 0.99
    segment_friction = 0.99

    def __init__(self, name=None, gravity=(0, 900), py5_sketch=None):
        self.name = name
        self.space = pymunk.Space()
        self.space.gravity = gravity
        # object registry management
        self.living_set = set()
        self.for_removal = set()
        # if no name is provided, make this the default simulation
        if name is None:
            Simulation._default = self
        # py5 sketch instance for drawing
        self.current_sketch = py5_sketch or py5.get_current_sketch()

    def __iter__(self):
        """To traverse living objects."""
        return iter(self.living_set)

    @classmethod
    def get_default(cls):
        """Get or create the default simulation."""
        if cls._default is None:
            cls._default = Simulation()  # Creates unnamed default
        return cls._default

    def step(self, s):
        """Advance the pymunk space simulation step."""
        self.space.step(s)

    def draw_and_update(self, step=None):
        """Draw all objects, remove marked ones and optionally advance sim step."""
        # ask objects in the living_set to draw themselves
        for obj in self.living_set:
            obj.draw()
        # remove objects marked for removal from the living_set
        self.living_set.difference_update(self.for_removal)
        self.for_removal.clear()
        # advance the pymunk space simulation step
        if step is not None:
            self.step(step)
        
    def add_segment(self, xa, ya, xb, yb, radius=2):
        return Segment(xa, ya, xb, yb, radius, simulation=self)
    def add_ball(self, x, y, diameter, fill_color=None):
        return Ball(x, y, diameter, fill_color, simulation=self)
    def add_poly(self, poly: Sequence[Sequence] | shapely.Polygon, fill_color=None, kinematic=False):
        return Poly(poly, fill_color, kinematic, simulation=self)
    def add_box(self, x, y, w, h, fill_color=None, kinematic=False):
        return Box(x, y, w, h, fill_color, simulation=self)

class SObj:
    """Base functionality for simulated objects."""
    def __init__(self, simulation=None):
        self.simulation = simulation or Simulation.get_default()
        self.space = self.simulation.space
        self.current_sketch = self.simulation.current_sketch

    def register_object(self):
        """Add body and shape to space, and register for drawing."""
        if not hasattr(self, "shapes"):
            self.shapes = (self.shape,)
        if self.body is not self.space.static_body:
            self.space.add(self.body, *self.shapes)
        else:
            self.space.add(*self.shapes)
        self.simulation.living_set.add(self)

    def remove_from_sim(self):
        """Remove from space and mark for removal from drawing registry."""
        if self.body is not self.space.static_body:
            self.space.remove(self.body, *self.shapes)
        else:
            self.space.remove(*self.shapes)
        self.simulation.for_removal.add(self)

    def rotate(self, rot):
        self.body.angle += rot

    def translate(self, dx, dy):
        self.body.position += pymunk.Vec2d(dx, dy)

    def under_mouse(self):
        s = self.current_sketch
        if hasattr(self, "poly"):
            translated_mouse = shapely.Point(
                (s.mouse_x - self.body.position.x,
                 s.mouse_y - self.body.position.y))
            return self.poly.contains(translated_mouse)
        else:
            info = self.shape.point_query((s.mouse_x, s.mouse_y))
            return info.distance < 2

    def draw(self):
        raise NotImplementedError # must be defined in subclasses.

class Segment(SObj):
    """Static wall-like line segment."""
    def __init__(self, xa, ya, xb, yb, radius=2, simulation=None):
        super().__init__(simulation)
        self.thickness = radius * 2
        self.body = self.space.static_body
        self.shape = pymunk.Segment(self.body, (xa, ya), (xb, yb), radius=radius)
        self.shape.friction = self.simulation.segment_friction
        self.register_object()

    def draw(self):
        s = self.current_sketch
        s.stroke_weight(self.thickness)
        s.stroke(0)
        s.line(self.shape.a.x, self.shape.a.y, self.shape.b.x, self.shape.b.y)

class Ball(SObj):
    """A color-filled ball."""
    def __init__(self, x, y, diameter, fill_color=None, simulation=None):
        super().__init__(simulation)
        self.diameter = diameter
        radius = diameter / 2
        self.fill_color = fill_color or py5.color(255)
        mass = py5.PI * radius**2 * self.simulation.mass_scale
        moment = pymunk.moment_for_circle(mass, 0, radius)
        self.body = pymunk.Body(mass, moment)
        self.body.position = x, y
        self.shape = pymunk.Circle(self.body, radius, (0, 0))
        self.register_object()

    def draw(self):
        s = self.current_sketch
        s.no_stroke()
        s.fill(self.fill_color)
        s.circle(self.body.position.x, self.body.position.y, self.shape.radius * 2)
        if self.body.position.y > s.height + self.diameter:
            self.remove_from_sim()

class Poly(SObj):
    """A simulated polygon-shaped object, from a shapely.Polygon. Kinematic or Dynamic."""
    def __init__(self, poly: Sequence[Sequence] | shapely.Polygon,
                 fill_color=None,
                 kinematic=False,
                 simulation=None):
        super().__init__(simulation)
        if not isinstance(poly, shapely.Polygon):
            poly = shapely.Polygon(poly)
        cx, cy = poly.centroid.x, poly.centroid.y
        self.poly = shapely.affinity.translate(poly, -cx, -cy)
        if kinematic:
            self.body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        else:
            mass = poly.area * self.simulation.mass_scale
            moment = pymunk.moment_for_poly(mass, self.poly.exterior.coords, (0, 0))
            self.body = pymunk.Body(mass, moment)
        self.body.position = (cx, cy)
        self.shapes = []
        vs, faces = triangulate_polygon(poly)
        triangles = [(vs[a], vs[b], vs[c]) for a, b, c in faces]
        for tri in triangles:
            translated_tri = [(x - cx, y - cy) for x, y in tri]
            shape = pymunk.Poly(self.body, translated_tri)
            shape.friction = self.simulation.poly_friction
            self.shapes.append(shape)
        self.fill_color = fill_color or py5.color(255)
        self.register_object()

    def draw(self):
        s = self.current_sketch
        s.fill(self.fill_color)
        s.no_stroke()
        with s.push_matrix():
            s.translate(self.body.position.x, self.body.position.y)
            s.rotate(self.body.angle)
            with s.begin_closed_shape():
                s.vertices(self.poly.exterior.coords)
        if self.body.position.y > s.height + 200:
            self.remove_from_sim()

class Box(SObj):
    """A rectangular polygon. Kinematic or Dynamic."""
    def __init__(self, x, y, w, h, fill_color=None, kinematic=False, simulation=None):
        super().__init__(simulation)
        if kinematic:
            self.body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        else:
            mass = w * h * self.simulation.mass_scale
            moment = pymunk.moment_for_box(mass, (w, h))
            self.body = pymunk.Body(mass, moment)
        self.body.position = x, y
        self.shape = pymunk.Poly.create_box(self.body, (w, h))
        self.shape.friction = 0.80
        self.vertices = self.shape.get_vertices()
        if fill_color is None:
            self.fill_color = (
                py5.color(100, 0, 0) if kinematic else py5.color(0, 100, 0)
            )
        else:
            self.fill_color = fill_color
        self.register_object()

    def draw(self):
        s = self.current_sketch
        s.fill(self.fill_color)
        s.no_stroke()
        with s.push_matrix():
            s.translate(self.body.position.x, self.body.position.y)
            s.rotate(self.body.angle)
            with s.begin_closed_shape():
                s.vertices(self.vertices)
        if self.body.position.y > s.height + 200:
            self.remove_from_sim()