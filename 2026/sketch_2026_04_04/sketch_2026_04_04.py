# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org

import py5
import pymunk

space = pymunk.Space()
space.gravity = 0, 900

mass_scale = 0.1

object_creation = None

def setup():
    py5.size(600, 600)
    Segment(50, 500, 550, 500)
    Box(100, 100, 100, 50)
    Box(200, 200, 100, 50, kinematic=False)
    #py5.frame_rate(30)
    
def draw():
    py5.background(200)
    SObj.draw_and_update_objects()  # draw and clean up
    # create more balls
    if py5.is_key_pressed and py5.key_code == py5.SHIFT:
        d = py5.random(10, 50)
        c = py5.color(d * 5, 0, 255 - d * 5)
        Ball(py5.mouse_x + py5.random(-1, 1), py5.mouse_y, d, c)
    # advance simulation
    space.step(1 / 60)

    
def mouse_pressed():
    global object_creation
    if py5.key == 'k' and py5.is_key_pressed:
        object_creation = (py5.mouse_x, py5.mouse_y, 'k')
    elif py5.key == 'c' and py5.is_key_pressed:
        object_creation = (py5.mouse_x, py5.mouse_y, 'c')
    elif py5.key == 'w' and py5.is_key_pressed:
        object_creation = (py5.mouse_x, py5.mouse_y, 'w')
    elif py5.key == 'p' and py5.is_key_pressed:
        print('pp')
        object_creation = ([], 'p')
      
def mouse_released():
    global object_creation
    match  object_creation:
        case inicial_x, inicial_y, kind:
            final_x = py5.mouse_x
            final_y = py5.mouse_y
            if kind in ('k', 'c'):
                w = abs(inicial_x - final_x)
                h = abs(inicial_y - final_y)
                x = (inicial_x + final_x) / 2
                y = (inicial_y + final_y) / 2
                Box(x, y, w, h, kind == 'k')
            elif kind == 'w':
                Segment(inicial_x, inicial_y, final_x, final_y)
        case pts, 'p':
            # TODO: add polygon
            print(f'{pts!r} \nPoly not implemented yet')
    object_creation = None
    
def mouse_dragged():
    if not py5.is_key_pressed:
        for obj in SObj.living_set:
            if obj.under_mouse():
                obj.translate(py5.mouse_x - py5.pmouse_x,
                              py5.mouse_y - py5.pmouse_y)
    elif object_creation:
        #print(object_creation)
        if py5.key == 'p':
            print('p')
            object_creation[0].append((py5.mouse_x, py5.mouse_y))
        
def mouse_wheel(e):
    for obj in SObj.living_set:
        if obj.under_mouse():
            obj.rotate(py5.radians(e.get_count()))
    

class SObj:
    
    living_set = set()
    for_removal = set()
    
    def register_object(self):
        if self.body is not space.static_body:
            space.add(self.body, self.shape)
        else:
            space.add(self.shape)
        self.living_set.add(self)
    
    @classmethod
    def draw_and_update_objects(cls):
        for obj in cls.living_set:
            obj.draw()
        cls.living_set.difference_update(cls.for_removal)
        cls.for_removal.clear()

    def remove_object(self):
        space.remove(self.shape)
        if self.body is not space.static_body:
            space.remove(self.body)
        self.for_removal.add(self)

    def rotate(self, rot):
        self.body.angle += rot

    def translate(self, dx, dy):
        self.body.position += pymunk.Vec2d(dx, dy)

    def under_mouse(self):
        info = self.shape.point_query((py5.mouse_x, py5.mouse_y))
        return info.distance < 2


class Segment(SObj):

    def __init__(self, xa, ya, xb, yb, radius=2):
        self.body = space.static_body  # corpo estático compartilhado pelo spaço
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

    def __init__(self, x, y, diametro, fill_color):
        radius = diametro / 2
        self.fill_color = fill_color
        mass = py5.PI * radius ** 2 * mass_scale
        moment = pymunk.moment_for_circle(mass, 0, radius)
        self.body = pymunk.Body(mass, moment)
        self.body.position = x, y
        self.shape = pymunk.Circle(self.body, radius, (0, 0))
        self.register_object()
        
    def draw(self):
        py5.no_stroke()
        py5.fill(self.fill_color)
        x = self.body.position.x
        y = self.body.position.y
        d = self.shape.radius * 2
        py5.circle(x, y, d)
        if y > py5.height + 20:
             self.remove_object()


class Box(SObj):

    def __init__(self, x, y, w, h, kinematic=True):
        if kinematic:
            self.body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        else:
            mass = w * h * mass_scale
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
            x, y = self.body.position.x, self.body.position.y
            py5.translate(x, y)
            py5.rotate(self.body.angle)
            with py5.begin_closed_shape():
                py5.vertices(self.shape.get_vertices())
        if y > py5.height + 20:
             self.remove_object()
             


py5.run_sketch(block=False)




