"""
This example lets you dynamically create static walls and dynamic balls
Based on https://github.com/viblo/pymunk/blob/master/pymunk/examples/balls_and_lines.py
"""

import py5
import pymunk
from pymunk import Vec2d

X, Y = 0, 1

### Physics collision types
COLLTYPE_DEFAULT = 0
COLLTYPE_MOUSE = 1
COLLTYPE_BALL = 2

### Physics stuff
space = pymunk.Space()
space.gravity = 0.0, 900.0
run_physics = True

## Balls
balls = []

### Static lines
line_point1 = None
static_lines = []

def setup():
    global mouse_body
    py5.size(600, 600)
    ### Mouse
    mouse_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
    mouse_shape = pymunk.Circle(mouse_body, 3, (0, 0))
    mouse_shape.collision_type = COLLTYPE_MOUSE
    space.add(mouse_body, mouse_shape)
    space.add_collision_handler(
        COLLTYPE_MOUSE, COLLTYPE_BALL
    ).pre_solve = mouse_coll_func

def draw():
    ### Update physics
    if run_physics:
        dt = 1.0 / 60.0
        for x in range(1):
            space.step(dt)
    ### Draw stuff
    py5.background('white')
    py5.fill(0)
    py5.text("LMB: Create ball\n"
             "LMB + Shift: Create many balls\n"
             "RMB: Drag to create wall, release to finish\n"
             "Space: Pause physics simulation", 10, 20)
    for ball in balls:
        r = ball.radius
        v = ball.body.position
        rot = ball.body.rotation_vector
        p = int(v.x), int(v.y)
        p2 = p + Vec2d(rot.x, -rot.y) * r * 0.9
        py5.no_fill()
        py5.stroke('blue')
        py5.circle(v.x, v.y, r * 2)
        py5.stroke('red')
        py5.line(v.x, v.y, p2.x, p2.y)
    if line_point1 is not None:
        py5.line(line_point1.x, line_point1.y,
                 py5.mouse_x, py5.mouse_y)
    for line in static_lines:
        body = line.body
        pv1 = body.position + line.a.rotated(body.angle)
        pv2 = body.position + line.b.rotated(body.angle)
        py5.stroke('lightgray')
        py5.line(pv1.x, pv1.y, pv2.x, pv2.y)
    mouse_body.position = Vec2d(py5.mouse_x, py5.mouse_y)
    py5.window_title(f'fps: {py5.get_frame_rate():1.1f}') 
    if py5.is_key_pressed and py5.key_code == py5.SHIFT:
        body = pymunk.Body(10, 100)
        body.position = py5.mouse_x, py5.mouse_y
        shape = pymunk.Circle(body, 10, (0, 0))
        shape.friction = 0.5
        shape.collision_type = COLLTYPE_BALL
        space.add(body, shape)
        balls.append(shape)
 
def mouse_coll_func(arbiter, space, data):
    """Simple callback that increases the radius of circles touching the mouse"""
    s1, s2 = arbiter.shapes
    s2.unsafe_set_radius(s2.radius + 0.15)
    return False

def key_pressed():
     if py5.key == 'p':
        py5.save_frame('####-balls_and_lines.png')
        
def mouse_pressed():
    global line_point1
    if py5.mouse_button == py5.LEFT and not py5.is_key_pressed:
        body = pymunk.Body(10, 100)
        body.position = py5.mouse_x, py5.mouse_y
        shape = pymunk.Circle(body, 10, (0, 0))
        shape.friction = 0.5
        shape.collision_type = COLLTYPE_BALL
        space.add(body, shape)
        balls.append(shape)
    elif py5.mouse_button == py5.RIGHT or py5.is_key_pressed and py5.key_code == py5.CONTROL:
        if line_point1 is None:
            line_point1 = Vec2d(py5.mouse_x, py5.mouse_y)


def mouse_released():
    global line_point1
    if line_point1 is not None:
        line_point2 = Vec2d(py5.mouse_x, py5.mouse_y)
        shape = pymunk.Segment(
            space.static_body, line_point1, line_point2, 0.0
        )
        shape.friction = 0.99
        space.add(shape)
        static_lines.append(shape)  
        line_point1 = None

def key_pressed():
    global run_physics
    if py5.key == ' ':
        run_physics = not run_physics

py5.run_sketch(block=False)
