# use Python from Thonny Env
"""A L shape_ attached with a joint and constrained to not tip over.

This example is also used in the Get Started Tutorial. 
"""

import random
import sys
import pymunk as pm

random.seed(1)
ticks_to_next_ball = 10
balls = []


def setup():
    size(600, 600)
    global space, wires
    print("Joints. Just wait and the L will tip over")
    space = pm.Space()
    space.gravity = (0.0, 700.0)
    wires = add_L(space)
    color_mode(HSB)
   
   
def add_L(space):
    """Add a inverted L shape with two joints"""
    rotation_center_body = pm.Body(body_type=pm.Body.STATIC)
    rotation_center_body.position = (300, 300)
    rotation_limit_body = pm.Body(body_type=pm.Body.STATIC)
    rotation_limit_body.position = (200, 300)
    body = pm.Body(10, 10000)
    body.position = (300, 300)
    l1 = pm.Segment(body, (-145, 0), (255.0, 0.0), 5)
    l2 = pm.Segment(body, (-145, 0), (-145.0, -45.0), 5)
    l1.friction = 1
    l2.friction = 1
    rotation_center_joint = pm.PinJoint(body, rotation_center_body, (0, 0), (0, 0))
    joint_limit = 25
    rotation_limit_joint = pm.SlideJoint(
        body, rotation_limit_body, (-100, 0), (0, 0), 0, joint_limit
    )
    space.add(l1, l2, body, rotation_center_joint, rotation_limit_joint)
    return l1, l2
  
  
def add_ball(space):
    """Add a ball to the given space at a random position"""
    mass = 1
    radius =random.randint(10, 20)
    inertia = pm.moment_for_circle(mass, 0, radius, (0, 0))
    body = pm.Body(mass, inertia)
    x = random.randint(120, 420)
    body.position = x, -50
    shp = pm.Circle(body, radius, (0, 0))
    shp.friction = 1
    space.add(body, shp)
  
  
def draw():
    global ticks_to_next_ball
    ticks_to_next_ball -= 1
    if ticks_to_next_ball <= 0:
        ticks_to_next_ball = 25
        add_ball(space)

    for obj in reversed(space.shapes):
        if is_ball(obj) and obj.body.position.y > 600:
            space.remove(obj, obj.body)
        
    background(200)

    for obj in space.shapes:
        if is_segment(obj):
            stroke(0)    
            stroke_weight(5)
            xo, yo = obj.body.position
            push_matrix()
            translate(xo, yo)
            rotate(obj.body.angle)
            # print(obj.a.x, obj.a.y, obj.b.x, obj.b.y)
            line(obj.a.x, obj.a.y, obj.b.x, obj.b.y)
            pop_matrix()
        elif is_ball(obj):
            no_stroke()
            # stroke_weight(1)
            fill(obj.radius * 10, 255, 255)
            circle(obj.body.position.x, obj.body.position.y, obj.radius * 2)
    
    stroke(255)
    fill(255)
    line(200, 328, 200, 300-28)
    circle(300, 300, 3)
    
    space.step(1 / get_frame_rate())


def is_ball(obj): return isinstance(obj, pm.shapes.Circle)
     
def is_segment(obj): return isinstance(obj, pm.shapes.Segment)
