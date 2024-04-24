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
    for point_a, point_b in segments:
        s = DrawableSegment(space.static_body, point_a, point_b, 1)
        s.elasticity = 1
        space.add(s)

def draw():
    py5.background(150)
    py5.no_stroke()
    for self in space.shapes:
        self.draw()
    if py5.is_key_pressed and py5.key_code == py5.SHIFT:
        add_balls()
    if py5.is_mouse_pressed and py5.mouse_button == py5.RIGHT:
        add_balls()
    for self in reversed(space.shapes):
        if self.body.position.y > py5.height + 10:
            space.remove(self)
    print(len(space.shapes))
    space.step(1/py5.get_frame_rate()) # advance simulation step



def populate_boxes():
    while len(space.shapes) < 22:
        x, y = randint(0, py5.width), randint(0, py5.width)
        if all(map(lambda self:  self.point_query((x, y)).distance > 0,
                   space.shapes)):
            create_box(x, y)
   
def add_balls():
    create_ball(py5.mouse_x + randint(0, 1), py5.mouse_y)
   
def create_box(x, y):
    body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
    body.position = x, y
    w, h = choice((100, 90, 80, 110)), choice((10, 5, 15))
    box_poly = DrawablePoly.create_box(body, (w, h))
    space.add(body, box_poly)


class DrawablePoly(pymunk.Poly):
    def draw(self):
        py5.push_matrix()
        py5.translate(self.body.position.x, self.body.position.y)
        py5.rotate(self.body.angle)
        pts = self.get_vertices()
        py5.begin_shape()
        py5.fill((pts[0][0] * pts[0][1]) % 255, 200, 200)
        for x, y in pts:
            py5.vertex(x, y)
        py5.end_shape(py5.CLOSE)
        py5.pop_matrix()
        
    def create_box(*args):
        return pymunk.Poly.create_box(*args)

def create_ball(x, y):
    body = pymunk.Body(mass=5, moment=10)
    body.position = x, y
    ball = DrawableCircle(body, radius=5)
    ball.elasticity = 0.2
    space.add(body, ball)

class DrawableCircle(pymunk.Circle):
    def draw(self):
        py5.fill(0) #(self.radius * 10, 255, 255)
        py5.circle(self.body.position.x, self.body.position.y, self.radius * 2)  

class DrawableSegment(pymunk.Segment):
    def draw_seg(self):
        with py5.push():
            py5.stroke(255)    
            py5.stroke_weight(self.radius*2)
            py5.line(self.a.x, self.a.y, self.b.x, self.b.y)  
    
def mouse_dragged():
    for self in space.shapes:
    #   if is_box(self):    
         info = self.point_query((py5.mouse_x, py5.mouse_y))
         if info.distance < 2:
             v = pymunk.Vec2d(py5.mouse_x - py5.pmouse_x,
                              py5.mouse_y - py5.pmouse_y)
             self.body.position += v

def mouse_wheel(e):
    for self in space.shapes:
        if is_box(self):    
             info = self.point_query((py5.mouse_x, py5.mouse_y))
             if info.distance < 2:
                 self.body.angle += py5.radians(e.getCount())
       
def key_pressed():
    if py5.key == ' ':
        for self in reversed(space.shapes):
            if is_ball(self) or is_box(self):
                space.remove(self)
        populate_boxes()

def is_ball(self): return isinstance(self, pymunk.shapes.Circle)
def is_box(self): return isinstance(self, pymunk.shapes.Poly)     

py5.run_sketch()
