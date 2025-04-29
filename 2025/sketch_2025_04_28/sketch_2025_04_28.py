# py5 imported mode, check https://py5coding.org

import pymunk

drawing_dict = {}  # o que tem que desenhar

def setup():
    global space
    size(600, 600)
    space = pymunk.Space()
    space.gravity = 100, 900
    # parede xa, ya, xb, yb
    add_wall(100, 500, 500, 500)
    add_ball(100, 100, f=color(0, 0, 200))
    add_static_ball(200, 200, f=255)
    add_box(200, 200, 100, 50, f=0)
    add_static_box(300, 200, 100, 50, s=0)
    
def draw():  # py5's main loop
    background(100, 0, 200)  # R, G, B
    for item, (draw_func, kwargs) in list(drawing_dict.items()):
        draw_func(item, **kwargs)
        if item.body.position.y > height + 50:
            space.remove(item)
            del drawing_dict[item]
    # acrescenta loucamente bolinhas
    if is_key_pressed and key_code == SHIFT:     
        add_ball(mouse_x + random(-1, 1),
                 mouse_y, f=0)
    # advance the simulation
    space.step(1 / 60)
 
def add_ball(
    x, y, diameter=20, f=255
    ):
    radius = diameter / 2
    body = pymunk.Body(radius ** 2 / 10, 100)
    body.position = x, y
    shp = pymunk.Circle(body, radius, (0, 0))
    shp.friction = 0.99
    space.add(body, shp)
    drawing_dict[shp] = (
        draw_circle,
        {'s': None, 'f': f}
        )

def add_static_ball(
    x, y, diameter=20, f=0
    ):
    radius = diameter / 2
    shp = pymunk.Circle(space.static_body, radius, (x, y))
    shp.friction = 0.99
    space.add(shp)
    drawing_dict[shp] = (
        draw_circle,
        {'s': None, 'f': f}
        )

def add_wall(xa, ya, xb, yb):
    shp = pymunk.Segment(space.static_body,
                           (xa, ya), (xb, yb),
                           radius=1.5)
    shp.friction = 100.99
    space.add(shp)
    drawing_dict[shp] = (
        draw_static_segment,
        {'s': 128}
        )
    
def fill_and_stroke(f=255, s=0, weight=None):
    stroke_weight(weight or 1)
    if s is not None:
        stroke(s)
    else:
        no_stroke()
    if f is not None:
        fill(f)
    else:
        no_fill()
 
def draw_circle(shp, f=0, s=None):
    fill_and_stroke(f, s)
    circle(shp.body.position.x + shp.offset.x,
               shp.body.position.y + shp.offset.y,
               shp.radius * 2)

def draw_static_segment(shp, f=None, s=0, weight=3):
    fill_and_stroke(f, s, weight)
    line(shp.a.x, shp.a.y,
         shp.b.x, shp.b.y)
  
def add_box(x, y, w, h, s=None, f=0):
    mass = w * h
    moment = pymunk.moment_for_box(mass, (w, h))
    body = pymunk.Body(mass, moment)
    body.position = (x , y)
    shp = pymunk.Poly.create_box(body, (w, h))
    shp.friction = 100.99
    space.add(body, shp)
    drawing_dict[shp] = (
        draw_box,
        {'s': s, 'f': f}
    )

def add_static_box(x, y, w, h, s=None, f=128):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (x , y)
    shp = pymunk.Poly.create_box(body, (w, h))
    shp.friction = 100.99
    space.add(body, shp)
    drawing_dict[shp] = (
        draw_box,
        {'s': s, 'f': f}
    )

def draw_box(shp, f=255, s=None, weight=1):
    fill_and_stroke(f, s, weight) 
    with push_matrix():
        translate(shp.body.position.x, shp.body.position.y)
        rotate(shp.body.angle)
        pts = shp.get_vertices()
        with begin_closed_shape():
            vertices(pts)
  
def mouse_clicked():
    if is_key_pressed and key_code == CONTROL:
        add_static_ball(mouse_x + random(-1, 1),
                    mouse_y,
                    f=255)
    else:
        add_ball(mouse_x + random(-1, 1),
                 mouse_y,
                 diameter=30,
                 f=color(0, 255, 0))        
        

