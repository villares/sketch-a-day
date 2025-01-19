# Based on an example by Tristan Bunn: https://tabreturn.github.io/code/python/thonny/2021/06/21/thonny_and_py5.html

import py5
import py5_tools
   
import pymunk
from random import randint

# create a new space for your simulation
space = pymunk.Space()
space.gravity = (500, 900)

# create walls
m = 5
segment1 = pymunk.Segment(space.static_body, (-m, -m), (-m, 500 + m), 5)
segment1.elasticity = 1
segment2 = pymunk.Segment(space.static_body, (500  + m, -m), (500 + m, 500 + m), 5)
segment2.elasticity = 1
segment3 = pymunk.Segment(space.static_body, (-m, 500 + m), (500 + m, 500 + m), 5)
segment3.elasticity = 1

space.add(segment1, segment2, segment3)

balls = []

def setup():
    py5.size(500, 500)
    py5.color_mode(py5.HSB)
    py5_tools.animated_gif('out.gif', duration=0.05, count=100, period=0.05)

def draw():
    py5.background(150)

    # render all of the bodies
    py5.stroke(255)
    py5.stroke_weight(segment1.radius*2)
    py5.line(segment1.a.x, segment1.a.y, segment1.b.x, segment1.b.y)
    py5.line(segment2.a.x, segment2.a.y, segment2.b.x, segment2.b.y)
    py5.no_stroke()
    for ball in balls:
        py5.fill(0)
        py5.circle(ball.body.position.x, ball.body.position.y, ball.radius * 2)

    # advance the simulation one step
    space.step(1/py5.get_frame_rate())

def create_ball(x, y, radius=10):
    # create a ball
    body = pymunk.Body(mass=1, moment=10)
    body.position = x, y
    ball = pymunk.Circle(body, radius=radius)
    ball.elasticity = 0.5
    balls.append(ball)
    space.add(body, ball)
    
def key_pressed():
    if py5.key == ' ':
        for x in range(100, 401, 50):
            for y in range(100, 401, 50):
                create_ball(x + py5.random(-1, 1) - 75, y - py5.height / 4, randint(5, 10))

py5.run_sketch()

