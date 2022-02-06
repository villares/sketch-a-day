# Based on py5 + pymunk example by @tabreturn
# https://tabreturn.github.io/code/python/thonny/2021/06/21/thonny_and_py5.html

import py5   
import pymunk
from random import randint
# create a new space for your simulation
space = pymunk.Space()
space.gravity = (0, 900)
bars = []
objects = []

def setup():
    py5.size(500, 500)
    py5.color_mode(py5.HSB)
    segments = (
        ((0, 500), (500, 500)),
        ((0, 0), (0, 500)),
        ((500, 0), (500, 500)),
        ((250, 450), (100, 150)),
        ((250, 450), (400, 150)),
        ((100, 150), (400, 150)),
    )
    for point_a, point_b in segments:
        s = pymunk.Segment(space.static_body, point_a, point_b, 1)
        s.elasticity = 0.1
        space.add(s)
        bars.append(s)

def draw():
    py5.background(150)
#     py5.stroke(255)    
#     for bar in bars:
#         py5.stroke_weight(bar.radius*2)
#         py5.line(bar.a.x, bar.a.y, bar.b.x, bar.b.y)
    py5.no_stroke()
    for obj in objects: # space.shapes:
        if is_box(obj):
            py5.no_stroke()
            xo, yo = obj.body.position
            py5.push_matrix()
            py5.translate(xo, yo)
            py5.rotate(obj.body.angle)
            pts = obj.get_vertices()
            py5.begin_shape()
            py5.fill((pts[0][0] * pts[0][1]) % 255, 200, 200)
            for x, y in pts:
                py5.vertex(x, y)
            py5.end_shape(py5.CLOSE)
            py5.pop_matrix()
        #py5.fill(ball.radius * 10, 255, 255)
        #py5.circle(ball.body.position.x, ball.body.position.y, ball.radius * 2)  
    space.step(1/py5.get_frame_rate()) # advance simulation step

   
def create_box(x, y):
    body = pymunk.Body(mass=5, moment=100)
    body.position = x, y
    w, h = randint(10, 30), randint(10, 30)
    b = pymunk.Poly.create_box(body, (w, h), radius=2)
    b.elasticity = 0.01
    b.friction = 0.6
    space.add(body, b)
    objects.append(b)

# def create_ball(x, y):
#     # create a ball
#     body = pymunk.Body(mass=5, moment=10)
#     body.position = x, y
#     ball = pymunk.Circle(body, radius=randint(5, 25))
#     ball.elasticity = 0.2
#     objects.append(ball)
#     space.add(body, ball)

def mouse_dragged():
    if py5.frame_count % 2 == 0:
        create_box(py5.mouse_x, py5.mouse_y)

def key_pressed():
    while objects:
        b = objects.pop()
        space.remove(b)

def is_ball(obj): return isinstance(obj, pymmnk.shapes.Circle)
def is_box(obj): return isinstance(obj, pymunk.shapes.Poly)     
def is_segment(obj): return isinstance(obj, pymunk.shapes.Segment)

py5.run_sketch()
