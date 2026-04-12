"""
pymunk_helpers.py v2026-04-12

Experimental module to help simplify playing with physics
simulations using  pymunk <pymunk.org> and py5 <py5coding.org>
It requires pymunk, shapely, trimesh and mapbox_earcut
"""
from collections.abc import Sequence

import py5
import pymunk
import shapely
from trimesh.creation import triangulate_polygon  # pip install trimesh[easy]


class Simulation:
    """Inits a pymunk.Space object, keeps track and draws simulated objects and joints."""
    _default = None
    mass_scale = 0.1
    KINEMATIC = pymunk.Body.KINEMATIC
    STATIC = pymunk.Body.STATIC
    DYNAMIC = pymunk.Body.DYNAMIC

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
            cls._default = Simulation()
        return cls._default

    def step(self, s):
        """Advance the pymunk space simulation step."""
        self.space.step(s)

    def draw_and_update(self, step=None):
        """Draw all objects then constraints, do removals, and optionally advance step."""
        # draw simulated objects
        for obj in self.living_set:
            if isinstance(obj, SObj):
                obj.draw()
        # draw constraints
        for ct in self.living_set:
            if isinstance(ct, Constraint):
                ct.draw()
        # remove objects marked for removal from the living_set
        self.living_set.difference_update(self.for_removal)
        self.for_removal.clear()
        # advance the pymunk space simulation step
        if step is not None:
            self.step(step)

    def add_kinematic_segment(self, xa, ya, xb, yb, radius=2, fill_color=128):
        return Segment(xa, ya, xb, yb, radius, fill_color, kinematic=True, simulation=self)
    def add_static_segment(self, xa, ya, xb, yb, radius=2, fill_color=0):
        return Segment(xa, ya, xb, yb, radius, fill_color, static=True, simulation=self)
    def add_segment(self, xa, ya, xb, yb, radius=2, fill_color=255):
        return Segment(xa, ya, xb, yb, radius, fill_color, simulation=self)
    def add_ball(self, x, y, diameter, fill_color=None):
        return Ball(x, y, diameter, fill_color, simulation=self)
    def add_poly(self, poly: Sequence[Sequence] | shapely.Polygon, fill_color=None, kinematic=False):
        return Poly(poly, fill_color, kinematic, simulation=self)
    def add_box(self, x, y, w, h, fill_color=None, kinematic=False):
        return Box(x, y, w, h, fill_color, simulation=self)


class SObj:
    """Base functionality for simulated objects."""
    friction = 0.5
    elasticity = 0.5
    
    def __init__(self, simulation=None):
        self.simulation = simulation or Simulation.get_default()
        self.space = self.simulation.space
        self.static_body = self.space.static_body
        self.constraints = set()  # tracks attached constraints

    def register_object(self):
        """Add body and shape to space, and register for drawing."""
        if not hasattr(self, "shapes"):
            self.shapes = (self.shape,)
        if self.body is not self.space.static_body:
            self.space.add(self.body, *self.shapes)
        else:
            self.space.add(*self.shapes)
        self.simulation.living_set.add(self)
        self.type = self.body.body_type


    def remove_from_sim(self):
        """
        Remove from space and mark for removal from drawing registry.
        Also, somewhat cumbersome removal of attached constraints.
        """
        # emove all attached constraints first
        for ct in list(self.constraints):
            ct.remove_from_sim()
        if self.body is not self.space.static_body:
            self.space.remove(self.body, *self.shapes)
        else:
            self.space.remove(*self.shapes)
        self.simulation.for_removal.add(self)

    def rotate(self, rot):
        self.body.angle += rot

    def translate(self, dx, dy):
        self.body.position += pymunk.Vec2d(dx, dy)

    def vel_update(self, dx, dy):
        self.body.velocity = pymunk.Vec2d(dx, dy) * 10


    def under_mouse(self):
        s = self.simulation.current_sketch
        if hasattr(self, "geometry"):
            translated_mouse = shapely.Point(
                (s.mouse_x - self.body.position.x,
                 s.mouse_y - self.body.position.y))
            return self.geometry.contains(translated_mouse)
        else:
            info = self.shape.point_query((s.mouse_x, s.mouse_y))
            return info.distance < 2

    def draw(self):
        raise NotImplementedError  # must be defined in subclasses.


class Segment(SObj):
    """
    Line segment of variable length - thickness double the radius.
    It can also be kinematic or static.
    """
    friction = 0.5
    elasticity = 0.5
    
    def __init__(self, xa, ya, xb, yb,
                 radius=2,
                 fill_color=None,
                 kinematic=False,
                 static=False,
                 simulation=None):
        super().__init__(simulation)
        self.thickness = radius * 2
        self.length = py5.dist(xa, ya, xb, yb)
        self.stroke_color = fill_color or py5.color(0)
        cx, cy = (xa + xb) / 2, (ya + yb) / 2
        rxa, rya = xa - cx, ya - cy
        rxb, ryb = xb - cx, yb - cy
        if static:
            self.body = self.space.static_body
            self.shape = pymunk.Segment(self.body, (xa, ya), (xb, yb), radius=radius)
        elif kinematic:
            self.body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
            self.shape = pymunk.Segment(self.body, (xa, ya), (xb, yb), radius=radius)
        else:
            rect_area = self.length * self.thickness
            caps_area = py5.PI * radius**2
            total_area = rect_area + caps_area
            mass = total_area * self.simulation.mass_scale
            moment = pymunk.moment_for_segment(mass, (rxa, rya), (rxb, ryb), radius)
            self.body = pymunk.Body(mass, moment)
            self.body.position = cx, cy
            self.shape = pymunk.Segment(self.body, (rxa, rya), (rxb, ryb), radius=radius)
        self.shape.friction = self.friction
        self.shape.elasticity = self.elasticity
        self.register_object()

    def draw(self):
        s = self.simulation.current_sketch
        s.stroke_weight(self.thickness)
        s.stroke(self.stroke_color)
        with s.push_matrix():
            s.translate(self.body.position.x, self.body.position.y)
            s.rotate(self.body.angle)
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
        self.shape.friction = self.friction
        self.shape.elasticity = self.elasticity
        self.register_object()

    def draw(self):
        s = self.simulation.current_sketch
        s.no_stroke()
        s.fill(self.fill_color)
        s.circle(self.body.position.x, self.body.position.y, self.shape.radius * 2)
        # trigger removal of falling objects... might be improved
        if self.body.position.y > s.height + self.diameter * 2:
            self.remove_from_sim()


class Poly(SObj):
    """
    A simulated polygonal, Kinematic or Dynamic, custom object.
    It can be created from a sequence of vertices, or shapely [Multi]Polygons.
    """
    def __init__(self, geometry:
                     Sequence[Sequence] | shapely.Polygon | shapely.MultiPolygon,
                 fill_color=None,
                 kinematic=False,
                 simulation=None):
        super().__init__(simulation)
        if isinstance(geometry, shapely.Polygon):
            cx, cy = geometry.centroid.x, geometry.centroid.y
            geometry = shapely.affinity.translate(geometry, -cx, -cy)
            polygons = (geometry,)
        elif isinstance(geometry, shapely.MultiPolygon):
            cx, cy = geometry.centroid.x, geometry.centroid.y
            geometry = shapely.affinity.translate(geometry, -cx, -cy)
            polygons = tuple(geometry.geoms)
        else:
            geometry = shapely.Polygon(geometry)
            cx, cy = geometry.centroid.x, geometry.centroid.y
            geometry = shapely.affinity.translate(geometry, -cx, -cy)
            polygons = (geometry,)
        self.fill_color = fill_color or py5.color(255)
        self.geometry = geometry
        self.py5shape = py5.convert_shape(geometry)
        self.py5shape.disable_style()
        self.shapes = []
        triangles = [] # the translated to origin triangles
        for poly in polygons:
            vs, faces = triangulate_polygon(poly)
            triangles.extend((tuple(vs[a]), tuple(vs[b]), tuple(vs[c]))
                             for a, b, c in faces)
        if kinematic:
            self.body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        else:
            mass = geometry.area * self.simulation.mass_scale
            moment = sum(
                pymunk.moment_for_poly(mass / len(triangles), tri, (0, 0))
                for tri in triangles
            )
            self.body = pymunk.Body(mass, moment)       
        for tri in triangles:
            shape = pymunk.Poly(self.body, tri)
            shape.friction = self.friction
            shape.elasticity = self.elasticity
            self.shapes.append(shape)
        self.body.position = (cx, cy)
        self.register_object()

    def draw(self):
        s = self.simulation.current_sketch
        s.fill(self.fill_color)
        s.no_stroke()
        if self.py5shape is None:
            self.py5shape = py5.convert_shape(self.geometry)        
        with s.push_matrix():
            s.translate(self.body.position.x, self.body.position.y)
            s.rotate(self.body.angle)
            s.shape(self.py5shape)
        # trigger removal of falling objects... might be improved
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
        self.shape.friction = self.friction
        self.shape.elasticity = self.elasticity
        self.vertices = self.shape.get_vertices()
        if fill_color is None:
            self.fill_color = (
                py5.color(100, 0, 0) if kinematic else py5.color(0, 100, 0)
            )
        else:
            self.fill_color = fill_color
        self.register_object()

    def draw(self):
        s = self.simulation.current_sketch
        s.fill(self.fill_color)
        s.no_stroke()
        with s.push_matrix():
            s.translate(self.body.position.x, self.body.position.y)
            s.rotate(self.body.angle)
            with s.begin_closed_shape():
                s.vertices(self.vertices)
        # trigger removal of falling objects... might be improved
        if self.body.position.y > s.height + 200:
            self.remove_from_sim()


class Constraint:
    """Base class for pymunk constraints wrappers."""
    visible = True
    def __init__(self, obj_a, obj_b, simulation=None):
        self.simulation = simulation or Simulation.get_default()
        self.space = self.simulation.space
        # Keep SObj references (may be None)
        self.obj_a = obj_a if isinstance(obj_a, SObj) else None
        self.obj_b = obj_b if isinstance(obj_b, SObj) else None
        self.type = 'CONSTRAINT' # not Body.KINEMATIC etc.

    def register_constrain(self):
        """Add joint to space, register in simulation, and link to attached SObjs."""
        self.space.add(self.joint)
        self.simulation.living_set.add(self)
        # register this constraint on the owning SObjs so they can cascade removal
        if self.obj_a is not None:
            self.obj_a.constraints.add(self)
        if self.obj_b is not None:
            self.obj_b.constraints.add(self)

    def remove_from_sim(self):
        """Remove joint from space, unlink from SObjs, and mark for removal."""
        living_set = self.simulation.living_set
        for_removal = self.simulation.for_removal
        if self in living_set and self not in for_removal:
            for_removal.add(self)
            self.space.remove(self.joint)
        # unregister from SObjs
        if self.obj_a is not None:
            self.obj_a.constraints.discard(self)
        if self.obj_b is not None:
            self.obj_b.constraints.discard(self)

    def under_mouse(self):
        raise NotImplementedError  # must be defined in subclasses

    def draw(self):
        raise NotImplementedError  # must be defined in subclasses


class PivotJoint(Constraint):
    """A pivot joint (revolute) - draws as a circle at the world-space anchor point."""
    def __init__(self, obj_a, obj_b, anchor=None, radius=4, color=None, simulation=None):
        super().__init__(obj_a, obj_b, simulation)
        self.radius = radius
        self.color = color or py5.color(0, 128, 0)
        self.body_a = obj_a.body if isinstance(obj_a, SObj) else obj_a
        self.body_b = obj_b.body if isinstance(obj_b, SObj) else obj_b
        # PivotJoint anchor is in world/screen coordinates
        anchor = anchor or obj_a.body.position  # obj_a position if none
        self.joint = pymunk.PivotJoint(self.body_a, self.body_b, anchor)
        self.joint.collide_bodies = False
        self.register_constrain()

    @property
    def position(self):
        return self.body_a.local_to_world(self.joint.anchor_a)

    def under_mouse(self):
        s = self.simulation.current_sketch
        return s.dist(s.mouse_x, s.mouse_y, *self.position) < self.radius + 4

    def draw(self):
        if self.visible:
            s = self.simulation.current_sketch
            s.fill(self.color)
            s.no_stroke()
            s.circle(*self.position, self.radius * 2)


class PinJoint(Constraint):
    """A pin joint (distance constraint) - draws as a line between anchor points."""
    def __init__(self, obj_a, obj_b, anchor_a=None, anchor_b=None,
                 radius=4, color=None, simulation=None):
        super().__init__(obj_a, obj_b, simulation)
        self.radius = radius
        self.color = color or py5.color(0, 128, 0)
        self.body_a = obj_a.body if isinstance(obj_a, SObj) else obj_a
        self.body_b = obj_b.body if isinstance(obj_b, SObj) else obj_b
        # PinJoint anchors are in locala body coordinates: (0, 0) = body.position
        # If world-space anchors are supplied, convert them with world_to_local().
        self.anchor_a = self.body_a.world_to_local(anchor_a) if anchor_a else (0, 0)
        self.anchor_b = self.body_b.world_to_local(anchor_b) if anchor_b else (0, 0)
        self.joint = pymunk.PinJoint(
            self.body_a, self.body_b, self.anchor_a, self.anchor_b
        )
        self.joint.collide_bodies = False
        self.register_constrain()

    def under_mouse(self):
        s = self.simulation.current_sketch
        mouse = shapely.Point(s.mouse_x, s.mouse_y)
        a = self.body_a.local_to_world(self.anchor_a)
        b = self.body_b.local_to_world(self.anchor_b)
        return shapely.LineString([a, b]).distance(mouse) < self.radius + 2

    def draw(self):
        if self.visible:
            s = self.simulation.current_sketch
            s.stroke_weight(self.radius * 2)
            s.stroke(self.color)
            s.no_fill()
            ax, ay = self.body_a.local_to_world(self.anchor_a)
            bx, by = self.body_b.local_to_world(self.anchor_b)
            s.line(ax, ay, bx, by)
