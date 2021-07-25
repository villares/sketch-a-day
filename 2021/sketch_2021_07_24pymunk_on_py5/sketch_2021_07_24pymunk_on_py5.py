# Based on an example by Tristan Bunn: https://tabreturn.github.io/code/python/thonny/2021/06/21/thonny_and_py5.html

import py5
   
import pymunk
from random import randint

# create a new space for your simulation
space = pymunk.Space()
space.gravity = (0, 900)

bars = []
balls = []

def setup():
    py5.size(500, 500)
    py5.color_mode(py5.HSB)

    segment1 = pymunk.Segment(space.static_body, (100, 450), (400, 450), 15)
    segment1.elasticity = 0.1
    segment2 = pymunk.Segment(space.static_body, (450, 150), (400, 450), 15)
    segment2.elasticity = 0.1
    segment3 = pymunk.Segment(space.static_body, (50, 150), (100, 450), 15)
    segment3.elasticity = 0.1
    space.add(segment1, segment2, segment3)
    bars.extend((segment1, segment2, segment3))
    

def draw():
    py5.background(150)

    # render all of the bodies
    py5.stroke(255)    
    for bar in bars:
        py5.stroke_weight(bar.radius*2)
        py5.line(bar.a.x, bar.a.y, bar.b.x, bar.b.y)
    py5.no_stroke()
    for ball in balls:
        py5.fill(ball.radius * 10, 255, 255)
        py5.circle(ball.body.position.x, ball.body.position.y, ball.radius * 2)

    # advance the simulation one step
    space.step(1/py5.get_frame_rate())

def create_ball(x, y):
    # create a ball
    body = pymunk.Body(mass=5, moment=10)
    body.position = x, y
    ball = pymunk.Circle(body, radius=randint(5, 25))
    ball.elasticity = 0.2
    balls.append(ball)
    space.add(body, ball)
    
def mouse_dragged():
    create_ball(py5.mouse_x, py5.mouse_y)

py5.run_sketch()
