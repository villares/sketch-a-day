# Based on py5 + pymunk example by @tabreturn
# https://tabreturn.github.io/code/python/thonny/2021/06/21/thonny_and_py5.html

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
    segments = (
        ((0, 500), (500, 500)),
        ((0, 0), (0, 500)),
        ((500, 0), (500, 500)),
        ((250, 100), (100, 400)),
        ((250, 100), (400, 400)),
        ((100, 400), (400, 400)),
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