# Based on an example by Tristan Bunn: https://tabreturn.github.io/code/python/thonny/2021/06/21/thonny_and_py5.html

import py5
import pymunk
from random import randint

# create a new space for your simulation
space = pymunk.Space()
space.gravity = (0, 900)

def setup():
    py5.size(500, 500)
    py5.color_mode(py5.HSB)
#    py5.rect_mode(py5.CENTER)

    segment1 = pymunk.Segment(space.static_body, (0, 450), (500, 450), 15)
    segment1.elasticity = 0.1
    segment1.friction = 0.8
#     segment2 = pymunk.Segment(space.static_body, (450, 150), (400, 450), 15)
#     segment2.elasticity = 0.1
#     segment3 = pymunk.Segment(space.static_body, (50, 150), (100, 450), 15)
#     segment3.elasticity = 0.1
#     objects.extend((segment1, segment2, segment3))
#     space.add(segment1, segment2, segment3)
    space.add(segment1)

def draw():
    py5.background(150)

    # render all of the objects
    for obj in space.shapes:
        if isinstance(obj, pymunk.shapes.Segment):
            py5.stroke(255)    
            py5.stroke_weight(30)
            py5.line(obj.a.x, obj.a.y, obj.b.x, obj.b.y)
        elif isinstance(obj, pymunk.shapes.Circle):
            py5.no_stroke()            
            py5.fill(obj.radius * 10, 255, 255)
            py5.circle(obj.body.position.x, obj.body.position.y, obj.radius * 2)
        elif isinstance(obj, pymunk.shapes.Poly):
            py5.stroke(255)
            py5.stroke_weight(1)
            py5.fill(0, 0, 255, 100)
            py5.begin_shape()
            xo, yo = obj.body.position
            py5.push_matrix()
            py5.translate(xo, yo)
            py5.rotate(obj.body.angle)
            pts = obj.get_vertices()
            py5.begin_shape()
            for x, y in pts:
                py5.vertex(x, y)
            py5.end_shape(py5.CLOSE)
            #py5.square(0, 0, 50)
            py5.pop_matrix()

    # advance the simulation one step
    space.step(1/py5.get_frame_rate())


def create_ball(x, y):
    # create a ball
    body = pymunk.Body(mass=5, moment=100)
    body.position = x, y
    shape = pymunk.Circle(body, radius=randint(5, 25))
    shape.elasticity = 0.01
    shape.friction = 0.6
    space.add(body, shape)

def create_box(x, y, size=50):
    body = pymunk.Body(mass=5, moment=100)
    body.position = x, y
    body.tamanho = size
    shape = pymunk.Poly.create_box(body, (size, size))
    shape.elasticity = 0.01
    shape.friction = 0.6
    space.add(body, shape)

def mouse_pressed():
    if py5.mouse_button == py5.LEFT:
        create_ball(py5.mouse_x, py5.mouse_y)
    else:
        create_box(py5.mouse_x, py5.mouse_y)

py5.run_sketch()
