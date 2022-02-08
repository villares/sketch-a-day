import py5   
import pymunk
from random import randint, sample, choice

space = pymunk.Space() # create a new space for your simulation
space.gravity = (0, 400)
PIN_DIST_MARGIN = 50
BALL_MARGIN = 300
BALL_RADIUS = 5

def setup():
    global initial_shape_count
    py5.size(700, 700)
    py5.color_mode(py5.HSB)
    #pymunk.Poly.draw = draw_pin  # this is called "monkeypatching"
    pymunk.Circle.draw = draw_ball
    pymunk.Segment.draw = draw_seg
    mw, mh = py5.width, py5.height
    segments = [
        ((-10, 0), (-10, mh)), 
        ((mw + 10, 0), (mw + 10, mh)),
        ((-10, mh), (mw + 10, mh)),
    ] 
    for point_a, point_b in segments:
        s = pymunk.Segment(space.static_body, point_a, point_b, 10)
        s.elasticity = 1
        s.friction =  1
        space.add(s)
    for point_a, point_b in (((x, mh), (x, mh * 0.60))
                             for x in range(0, mw + 1, 12)):
        s = pymunk.Segment(space.static_body, point_a, point_b, 0.5)
        s.elasticity = 0.1
        s.friction =  1
        space.add(s)
    initial_shape_count = len(space.shapes)
    populate_pins()

def draw():
    py5.background(150)
    py5.no_stroke()
    for obj in space.shapes:
        obj.draw()
    if py5.is_key_pressed and py5.key_code == py5.SHIFT:
        add_balls()
    if py5.is_mouse_pressed and py5.mouse_y < 50:
        add_balls(py5.mouse_x, py5.mouse_y)
    # remove objets that fall bellow
    for obj in reversed(space.shapes):
        if obj.body.position.y > py5.height + 10:
            space.remove(obj)
    space.step(0.9/py5.get_frame_rate() ) # advance simulation step


def populate_pins():
    def good_placement(obj):
        return not is_pin(obj) or obj.point_query((x, y)).distance > 20
    for x in range(PIN_DIST_MARGIN, py5.width - PIN_DIST_MARGIN, 30):
        for y in range(100, int(py5.height * 0.50), 30):
            create_pin(x, y, BALL_RADIUS)
   
def create_pin(x, y, radius):
    body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
    body.position = x, y
    pin = pymunk.Circle(body, radius)
    pin.hue = None
    space.add(body, pin)

def add_balls(x=None, y=5):
    if x is None:
        for x in range(BALL_MARGIN, py5.width - BALL_MARGIN, 5):
            h = py5.remap(x, BALL_MARGIN, py5.width - BALL_MARGIN, 0, 255)
            create_ball(x, y, h)
    else:
        h = py5.remap(x, 0, py5.width, 0, 255)
        create_ball(x + randint(0, 1), y, h)

def create_ball(x, y, h=0):
    body = pymunk.Body(mass=5, moment=10)
    body.position = x, y
    ball = pymunk.Circle(body, radius=BALL_RADIUS)
    ball.elasticity = 0.1
    ball.friction = 0.5
    ball.hue = h
    space.add(body, ball)
   
def draw_ball(obj):
    if obj.hue is not None:
        py5.fill(obj.hue, 200, 200) #(obj.radius * 10, 255, 255)
    else:
        py5.fill(0)
    py5.circle(obj.body.position.x, obj.body.position.y, obj.radius * 2)  

def draw_seg(obj): 
    py5.push()
    py5.stroke(255)    
    py5.stroke_weight(obj.radius*2)
    py5.line(obj.a.x, obj.a.y, obj.b.x, obj.b.y)  
    py5.pop()
    
def mouse_dragged():
    for obj in space.shapes:
         info = obj.point_query((py5.mouse_x, py5.mouse_y))
         if info.distance < 2:
             v = pymunk.Vec2d(py5.mouse_x - py5.pmouse_x,
                          py5.mouse_y - py5.pmouse_y)
             obj.body.position += v

def key_pressed():
    if py5.key == ' ':
        for obj in reversed(space.shapes):
            if is_ball(obj):
                space.remove(obj)
        populate_pins()

def is_ball(obj): return isinstance(obj, pymunk.shapes.Circle)

py5.run_sketch()