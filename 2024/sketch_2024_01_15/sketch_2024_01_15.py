# Based on an example by Tristan Bunn: https://tabreturn.github.io/code/python/thonny/2021/06/21/thonny_and_py5.html

import py5
   
import pymunk
from random import randint

# create a new space for your simulation
space = pymunk.Space()
space.gravity = (0, 900)

# create a valley-like floor
segment1 = pymunk.Segment(space.static_body, (0, 0), (0, 500), 5)
segment1.elasticity = 1
segment2 = pymunk.Segment(space.static_body, (500, 0), (500, 500), 5)
segment2.elasticity = 1
segment3 = pymunk.Segment(space.static_body, (0, 500), (500, 500), 5)
segment3.elasticity = 1

space.add(segment1, segment2, segment3)

balls = []

def setup():
    py5.size(500, 500)
    py5.color_mode(py5.HSB)

def draw():
    py5.background(150)

    # render all of the bodies
    py5.stroke(255)
    py5.stroke_weight(segment1.radius*2)
    py5.line(segment1.a.x, segment1.a.y, segment1.b.x, segment1.b.y)
    py5.line(segment2.a.x, segment2.a.y, segment2.b.x, segment2.b.y)
    py5.no_stroke()
    for ball in balls:
        py5.fill(ball.radius * 8, 255, 255)
        py5.circle(ball.body.position.x, ball.body.position.y, ball.radius * 2)

    # advance the simulation one step
    space.step(1/py5.get_frame_rate())

def create_ball(x, y):
    # create a ball
    body = pymunk.Body(mass=1, moment=10)
    body.position = x, y
    ball = pymunk.Circle(body, radius=randint(5, 25))
    ball.elasticity = 0.5
    balls.append(ball)
    space.add(body, ball)
    
def key_pressed():
    if py5.key == ' ':
        for x in range(100, 401, 50):
            for y in range(100, 401, 50):
                create_ball(x + py5.random(-1, 1), y)

py5.run_sketch()

