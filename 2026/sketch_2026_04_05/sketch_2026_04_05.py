# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org

import py5
import pymunk

ongoing_creation = None

def setup():
    py5.size(600, 600)
    global sim
    sim = Simulation()
    Segment(50, 500, 550, 500)
    #Box(100, 100, 100, 50)
    #Box(200, 200, 100, 50, kinematic=False)

def draw():
    py5.background(200)
    sim.draw_and_update()  # draw and clean up
    # create many balls
    if py5.is_key_pressed and py5.key_code == py5.SHIFT:
        d = py5.random(10, 50)
        c = py5.color(d * 5, 0, 255 - d * 5)
        Ball(py5.mouse_x + py5.random(-1, 1), py5.mouse_y, d, c)
    # preview object creation
    if ongoing_creation:
        with py5.push_style():
            py5.no_fill()
            py5.stroke_weight(2)
            py5.stroke(255)
            if ongoing_creation[-1] == 'p':
                pts = ongoing_creation[0]
                x, y = py5.mouse_x, py5.mouse_y
                with py5.push_style(), py5.begin_shape():
                    py5.vertices(pts)
                    py5.vertex(x, y)            
                if len(pts) and py5.dist(x, y, *pts[-1]) < 20:
                    return
                ongoing_creation[0].append((x, y))
            elif ongoing_creation[-1] == 'w':            
                sx, sy = ongoing_creation[:2]
                x, y = py5.mouse_x, py5.mouse_y
                with py5.push_style(), py5.begin_shape():
                    py5.line(sx, sy, x, y)
            elif ongoing_creation[-1] in ('c', 'k'):
                sx, sy = ongoing_creation[:2]
                x, y = py5.mouse_x, py5.mouse_y
                py5.rect_mode(py5.CORNERS)
                py5.rect(sx, sy, x, y)
    # advance simulation
    sim.step(1 / 60)

    
def mouse_pressed():
    global ongoing_creation
    if py5.key == 'k' and py5.is_key_pressed:
        ongoing_creation = (py5.mouse_x, py5.mouse_y, 'k')
    elif py5.key == 'c' and py5.is_key_pressed:
        ongoing_creation = (py5.mouse_x, py5.mouse_y, 'c')
    elif py5.key == 'w' and py5.is_key_pressed:
        ongoing_creation = (py5.mouse_x, py5.mouse_y, 'w')
    elif py5.key == 'p' and py5.is_key_pressed:
        ongoing_creation = ([], 'p')

      
def mouse_released():
    global ongoing_creation
    match ongoing_creation:
        case inicial_x, inicial_y, kind:
            final_x = py5.mouse_x
            final_y = py5.mouse_y
            if kind in ('k', 'c'):
                w = abs(inicial_x - final_x)
                h = abs(inicial_y - final_y)
                x = (inicial_x + final_x) / 2
                y = (inicial_y + final_y) / 2
                Box(x, y, w, h, kinematic=(kind == 'k'))
            elif kind == 'w':
                Segment(inicial_x, inicial_y, final_x, final_y)
        case pts, 'p':
            # TODO: add polygon
            print(f'{pts} \nPoly not implemented yet')
    ongoing_creation = None

def mouse_dragged():
    if not py5.is_key_pressed:
        for obj in sim:
            if obj.under_mouse():
                obj.translate(py5.mouse_x - py5.pmouse_x,
                              py5.mouse_y - py5.pmouse_y) 

def mouse_wheel(e):
    for obj in sim:
        if obj.under_mouse():
            obj.rotate(py5.radians(e.get_count()))


class Simulation:
    _default = None

    def __init__(self, name=None, gravity=(0, 900), mass_scale=0.1):
        self.name = name
        self.space = pymunk.Space()
        self.space.gravity = gravity
        self.mass_scale = mass_scale
        # object registry management
        self.living_set = set()
        self.for_removal = set()
        # if no name provided, make this the default simulation
        if name is None:
            Simulation._default = self
    
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
        """Advance the simulation step."""
        self.space.step(s)
    
    def draw_and_update(self):
        """Draw all objects and remove marked ones."""
        for obj in self.living_set:
            obj.draw()
        self.living_set.difference_update(self.for_removal)
        self.for_removal.clear()
    
    def register(self, obj):
        """Register an object for drawing."""
        self.living_set.add(obj)
    
    def mark_for_removal(self, obj):
        """Mark an object for removal."""
        self.for_removal.add(obj)
        
    def segment(self, xa, ya, xb, yb, radius=2):
        return Segment(xa, ya, xb, yb, radius=radius, space=self.space, simulation=self)
    
    def ball(self, x, y, diameter, fill_color):
        return Ball(x, y, diameter, fill_color, space=self.space, simulation=self)
    
    def box(self, x, y, w, h, kinematic=True):
        return Box(x, y, w, h, kinematic=kinematic, space=self.space, simulation=self)


class SObj:
    
    def __init__(self, space=None, simulation=None):
        self.space = space or Simulation.get_default().space
        self.simulation = simulation or Simulation.get_default()
        self.body = None
        self.shape = None
    
    def register_object(self):
        """Add body and shape to space, and register for drawing."""
        if self.body is not self.space.static_body:
            self.space.add(self.body, self.shape)
        else:
            self.space.add(self.shape)
        self.simulation.register(self)
    
    def remove_object(self):
        """Remove from space and mark for removal from drawing registry."""
        self.space.remove(self.shape)
        if self.body is not self.space.static_body:
            self.space.remove(self.body)
        self.simulation.mark_for_removal(self)

    def rotate(self, rot):
        self.body.angle += rot

    def translate(self, dx, dy):
        self.body.position += pymunk.Vec2d(dx, dy)

    def under_mouse(self):
        info = self.shape.point_query((py5.mouse_x, py5.mouse_y))
        return info.distance < 2

    def draw(self):
        """Defined in subclasses."""
        raise NotImplementedError


class Segment(SObj):

    def __init__(self, xa, ya, xb, yb,
                 radius=2,
                 space=None,
                 simulation=None):
        super().__init__(space, simulation)
        self.body = self.space.static_body
        self.shape = pymunk.Segment(
            self.body, (xa, ya), (xb, yb), radius=radius)
        self.shape.friction = 0.99
        self.register_object()

    def draw(self):
        py5.stroke_weight(self.shape.radius * 2)
        py5.stroke(0)
        py5.line(self.shape.a.x, self.shape.a.y,
                 self.shape.b.x, self.shape.b.y)


class Ball(SObj):

    def __init__(self, x, y, diameter, fill_color=None, space=None, simulation=None):
        super().__init__(space, simulation)
        radius = diameter / 2
        self.fill_color = fill_color or py5.color(255)
        mass = py5.PI * radius ** 2 * self.simulation.mass_scale
        moment = pymunk.moment_for_circle(mass, 0, radius)
        self.body = pymunk.Body(mass, moment)
        self.body.position = x, y
        self.shape = pymunk.Circle(self.body, radius, (0, 0))
        self.register_object()
        
    def draw(self):
        py5.no_stroke()
        py5.fill(self.fill_color)
        py5.circle(self.body.position.x,
                   self.body.position.y,
                   self.shape.radius * 2)
        if self.body.position.y > py5.height + 20:
             self.remove_object()


class Box(SObj):

    def __init__(self, x, y, w, h, kinematic=True, space=None, simulation=None):
        super().__init__(space, simulation)
        if kinematic:
            self.body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        else:
            mass = w * h * self.simulation.mass_scale
            moment = pymunk.moment_for_box(mass, (w, h))
            self.body = pymunk.Body(mass, moment)
        self.body.position = x, y
        self.shape = pymunk.Poly.create_box(self.body, (w, h))
        self.shape.friction = 0.80
        self.fill_color = py5.color(100, 0, 0) if kinematic else py5.color(0, 100, 0)
        self.register_object()

    def draw(self):
        py5.fill(self.fill_color)
        py5.no_stroke()
        with py5.push_matrix():
            py5.translate(self.body.position.x, self.body.position.y)
            py5.rotate(self.body.angle)
            with py5.begin_closed_shape():
                py5.vertices(self.shape.get_vertices())
        if self.body.position.y > py5.height + 20:
             self.remove_object()


py5.run_sketch(block=False)
