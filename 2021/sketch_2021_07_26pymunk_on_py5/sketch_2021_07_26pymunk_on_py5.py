# use Python from Thonny Env
"""A L shape attached with a joint and constrained to not tip over.

This example is also used in the Get Started Tutorial. 
"""

import random
import sys

# import pygame
import py5

import pymunk
# import pymunk.pygame_util

random.seed(1)
ticks_to_next_ball = 10
balls = []

def add_ball(space):
    """Add a ball to the given space at a random position"""
    mass = 1
    radius =random.randint(10, 20)
    inertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
    body = pymunk.Body(mass, inertia)
    x = random.randint(120, 420)
    body.position = x, -50
    shape = pymunk.Circle(body, radius, (0, 0))
    shape.friction = 1
    space.add(body, shape)
    return shape


def add_L(space):
    """Add a inverted L shape with two joints"""
    rotation_center_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    rotation_center_body.position = (300, 300)

    rotation_limit_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    rotation_limit_body.position = (200, 300)

    body = pymunk.Body(10, 10000)
    body.position = (300, 300)
    l1 = pymunk.Segment(body, (-145, 0), (255.0, 0.0), 5)
    l2 = pymunk.Segment(body, (-145, 0), (-145.0, -45.0), 5)
    l1.friction = 1
    l2.friction = 1
    rotation_center_joint = pymunk.PinJoint(body, rotation_center_body, (0, 0), (0, 0))
    joint_limit = 25
    rotation_limit_joint = pymunk.SlideJoint(
        body, rotation_limit_body, (-100, 0), (0, 0), 0, joint_limit
    )

    space.add(l1, l2, body, rotation_center_joint, rotation_limit_joint)
    return l1, l2
    

def setup():
    py5.size(600, 600)
    global space, lines
    print("Joints. Just wait and the L will tip over")
    space = pymunk.Space()
    space.gravity = (0.0, 700.0)
    lines = add_L(space)
    py5.color_mode(py5.HSB)
    
    
def draw():
    global ticks_to_next_ball
    ticks_to_next_ball -= 1
    if ticks_to_next_ball <= 0:
        ticks_to_next_ball = 25
        ball_shape = add_ball(space)

    for obj in reversed(space.shapes):
        if is_ball(obj) and obj.body.position.y > 600:
            space.remove(obj, obj.body)
        
    py5.background(200)

    for obj in space.shapes:
        if is_segment(obj):
            py5.stroke(0)    
            py5.stroke_weight(5)
            xo, yo = obj.body.position
            py5.push_matrix()
            py5.translate(xo, yo)
            py5.rotate(obj.body.angle)
            # print(obj.a.x, obj.a.y, obj.b.x, obj.b.y)
            py5.line(obj.a.x, obj.a.y, obj.b.x, obj.b.y)
            py5.pop_matrix()
        elif is_ball(obj):
            py5.no_stroke()
            # py5.stroke_weight(1)
            py5.fill(obj.radius * 10, 255, 255)
            py5.circle(obj.body.position.x, obj.body.position.y, obj.radius * 2)
    
    py5.stroke(255)
    py5.fill(255)
    py5.line(200, 328, 200, 300-28)
    py5.circle(300, 300, 3)
    
    space.step(1 / py5.get_frame_rate())


def is_ball(obj):
    return isinstance(obj, pymunk.shapes.Circle)
     
def is_segment(obj):
    return isinstance(obj, pymunk.shapes.Segment)

if __name__ == "__main__":
    py5.run_sketch()