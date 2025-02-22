# Based on sketch_2022_02_04py5.py

import py5   
import pymunk
from random import randint, sample, choice

space = pymunk.Space() # create a new space for your simulation
space.gravity = (0, 900)

def setup():
    py5.size(500, 500)
    py5.color_mode(py5.HSB)
    populate_boxes()
    
    segments = (
        ((500, 0), (500, 500)),
        ((0, 0), (0, 500)),
    )
    # static bodies not being drawn
    for point_a, point_b in segments:
        s = pymunk.Segment(space.static_body, point_a, point_b, 1)
        s.elasticity = 1
        space.add(s)

def draw():
    py5.background(150)
    py5.no_stroke()
    for b in space.bodies:
        b.draw()
        
    for self in reversed(space.shapes):
        if self.body.position.y > py5.height + 10:
            space.remove(self)
            
    #print(len(space.shapes))
    
    space.step(1/py5.get_frame_rate()) # advance simulation step

    if py5.is_key_pressed and py5.key_code == py5.SHIFT:
        add_balls()


def populate_boxes():
    while len(space.shapes) < 22:
        x, y = randint(0, py5.width), randint(0, py5.width)
        if all(map(lambda self:  self.point_query((x, y)).distance > 0,
                   space.shapes)):
            create_box(x, y)
   
def add_balls():
    create_ball(py5.mouse_x + randint(0, 1), py5.mouse_y)
   
def create_box(x, y):
    body = DrawableBody(body_type=pymunk.Body.KINEMATIC)
    body.position = x, y
    w, h = choice((100, 90, 80, 110)), choice((10, 5, 15))
    box_poly = pymunk.Poly.create_box(body, (w, h))
    s = py5.create_shape()
    pts = box_poly.get_vertices()
    body.shape_args = pts
    body.a = w * h
    space.add(body, box_poly)


class DrawableBody(pymunk.Body):
    # 31 ELLIPSE ???
    # 20 POLYGON
    def draw(self):
        if len(self.shape_args) == 4:
            py5.fill(255)
            shp = py5.create_shape()
            with shp.begin_closed_shape():
                shp.vertices(self.shape_args)
        else:
            py5.fill(0)
            shp = py5.create_shape(*self.shape_args)
            
        with py5.push_matrix():
            py5.translate(self.position.x, self.position.y)
            py5.rotate(self.angle)
            py5.shape(shp)  


def create_ball(x, y):
    body = DrawableBody(mass=5, moment=10)
    body.position = x, y
    r = py5.random_int(1, 3) * 5
    ball = pymunk.Circle(body, radius=r)
    ball.elasticity = 0.2
    body.shape_args = (py5.ELLIPSE, 0, 0, r * 2, r * 2)
    body.a = r ** 2 * py5.PI
    space.add(body, ball)
def mouse_dragged():
    for shp in space.shapes:
         info = shp.point_query((py5.mouse_x, py5.mouse_y))
         if info.distance < 2:
             v = pymunk.Vec2d(py5.mouse_x - py5.pmouse_x,
                              py5.mouse_y - py5.pmouse_y)
             shp.body.position += v

def mouse_wheel(e):
    for shp in space.shapes:
        if is_box(shp):    
             info = shp.point_query((py5.mouse_x, py5.mouse_y))
             if info.distance < 2:
                 shp.body.angle += py5.radians(e.get_count())
       
def key_pressed():
    global space
    if py5.key == ' ':
        for shp in reversed(space.shapes):
            space.remove(shp)
            try:
                space.remove(shp.body)
            except:
                pass
        populate_boxes()
    elif py5.key == 's':
        py5.save_pickle(space, 'sim.pickle')
    elif py5.key == 'l':
        space = py5.load_pickle('sim.pickle')



def is_ball(obj): return isinstance(obj, pymunk.shapes.Circle)
def is_box(obj): return isinstance(obj, pymunk.shapes.Poly)     

py5.run_sketch()
