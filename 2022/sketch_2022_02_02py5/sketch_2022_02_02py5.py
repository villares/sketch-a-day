import py5   
import pymunk
from random import randint

space = pymunk.Space() # create a new space for your simulation
space.gravity = (0, 900)

def setup():
    py5.size(500, 500)
    py5.color_mode(py5.HSB)
    populate_boxes()
    pymunk.Poly.draw = draw_box  # this is called "monkeypatching"
    pymunk.Circle.draw = draw_ball

def draw():
    py5.background(150)
    py5.no_stroke()
    for obj in space.shapes:
        obj.draw()
    space.step(1/py5.get_frame_rate()) # advance simulation step

def populate_boxes():
    for _ in range(100):
        create_box(randint(0, py5.width), randint(0, py5.width))
   
def create_box(x, y):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = x, y
    space.add(body, pymunk.Poly.create_box(body,
                                           (randint(10, 30), randint(10, 30))))
def draw_box(obj):
    py5.push_matrix()
    py5.translate(obj.body.position.x, obj.body.position.y)
    py5.rotate(obj.body.angle)
    pts = obj.get_vertices()
    py5.begin_shape()
    py5.fill((pts[0][0] * pts[0][1]) % 255, 200, 200)
    for x, y in pts:
        py5.vertex(x, y)
    py5.end_shape(py5.CLOSE)
    py5.pop_matrix()

def create_ball(x, y):
    body = pymunk.Body(mass=5, moment=10)
    body.position = x, y
    ball = pymunk.Circle(body, radius=5)
    ball.elasticity = 0.2
    space.add(body, ball)

def draw_ball(obj):
    py5.fill(0) #(obj.radius * 10, 255, 255)
    py5.circle(obj.body.position.x, obj.body.position.y, obj.radius * 2)  

def mouse_dragged(): create_ball(py5.mouse_x, py5.mouse_y)

def key_pressed():
    for obj in reversed(space.shapes):
        if is_ball(obj) or is_box(obj):
            space.remove(obj)
    populate_boxes()

def is_ball(obj): return isinstance(obj, pymunk.shapes.Circle)
def is_box(obj): return isinstance(obj, pymunk.shapes.Poly)     

py5.run_sketch()
