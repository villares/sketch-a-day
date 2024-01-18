# Based on an example by Tristan Bunn: https://tabreturn.github.io/code/python/thonny/2021/06/21/thonny_and_py5.html

import py5
import py5_tools
   
import pymunk
from random import randint

# create a new space for your simulation
space = pymunk.Space()
space.gravity = (0, 900)


balls = []

def setup():
    global segment1, segment2, segment3
    py5.size(1000, 1000)
    py5.color_mode(py5.HSB)
    w, h = py5.width, py5.height 
    #py5_tools.animated_gif('out.gif', duration=0.1, count=30, period=.1)
    segment1 = pymunk.Segment(space.static_body, (0, 0), (0, h), 15)
    segment1.elasticity = 0
    segment2 = pymunk.Segment(space.static_body, (w, 0), (w, h), 15)
    segment2.elasticity = 0
    segment3 = pymunk.Segment(space.static_body, (0, h-15), (w, h-15), 15)
    segment3.elasticity = 0

    space.add(segment1, segment2, segment3)


def draw():
    py5.background(150)

    # render all of the bodies
    py5.stroke(255)
    py5.stroke_weight(segment1.radius*2)
    py5.line(segment1.a.x, segment1.a.y, segment1.b.x, segment1.b.y)
    py5.line(segment2.a.x, segment2.a.y, segment2.b.x, segment2.b.y)
    py5.line(segment3.a.x, segment3.a.y, segment3.b.x, segment3.b.y)
    py5.no_stroke()
    for ball in balls:
        py5.fill(ball.radius * 8, 255, 255)
        py5.circle(ball.body.position.x, ball.body.position.y, ball.radius * 2)

    # advance the simulation one step
    space.step(0.02)

def create_ball(x, y):
    # create a ball
    body = pymunk.Body(mass=1, moment=10)
    body.position = x, y
    ball = pymunk.Circle(body, radius=4)
    ball.elasticity = 0.1
    balls.append(ball)
    space.add(body, ball)
    
def key_pressed():
    if py5.key == ' ':
        for x in range(50, 950, 9):
            for y in range(50, 950, 9):
                create_ball(x + py5.random(-1, 1), y)

py5.run_sketch(block=False)

