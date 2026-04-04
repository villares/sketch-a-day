# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org


import py5
import pymunk

space = pymunk.Space()
space.gravity = 0, 900

mass_scale = 0.1
walls = []
balls = []
boxes = []

object_creation = None

def setup():
    py5.size(600, 600)
    add_wall(50, 500, 550, 500)
    add_box(100, 100, 100, 50)
    add_box(200, 200, 100, 50, kinematic=False)
    #py5.frame_rate(30)
    
def draw():
    py5.background(200)
    # desenhar paredes
    py5.stroke_weight(10)
    py5.stroke(0)
    for wall in walls:
        py5.line(wall.a.x, wall.a.y, wall.b.x, wall.b.y)
    # desenhar bolinhas
    py5.no_stroke()
    py5.fill(0, 200, 0)
    for ball in balls[:]:   # andando por uma cópia da lista
        x = ball.body.position.x
        y = ball.body.position.y
        d = ball.radius * 2
        py5.circle(x, y, d)
        if y > py5.height + 20:
            space.remove(ball)
            space.remove(ball.body)
            balls.remove(ball)
    # desenhar caixas
    for box in boxes[:]:   # andando por uma cópia da lista
        py5.fill(box.cor)
        with py5.push_matrix():
            x, y = box.body.position.x, box.body.position.y
            py5.translate(x, y)
            py5.rotate(box.body.angle)
            py5.begin_shape()
            py5.vertices(box.get_vertices())
            py5.end_shape(py5.CLOSE)
        if y > py5.height + 20:
            space.remove(box)
            space.remove(box.body)
            boxes.remove(box)
    #print(len(space.shapes), len(space.bodies))
    # criando bolinhas
    if py5.is_key_pressed and py5.key_code == py5.SHIFT:
        add_ball(py5.mouse_x + py5.random(-1, 1),
                     py5.mouse_y, 10)
    # avançar simulação
    space.step(1 / 80)

def add_wall(xa, ya, xb, yb):
    body = space.static_body  # corpo estático compartilhado pelo spaço
    shape = pymunk.Segment(body, (xa, ya), (xb, yb), radius=5)
    shape.friction = 0.99
    space.add(shape)
    walls.append(shape)
    
def add_ball(x, y, diametro):
    raio = diametro / 2
    massa = py5.PI * raio ** 2 * mass_scale
    momento = pymunk.moment_for_circle(massa, 0, raio)
    body = pymunk.Body(massa, momento)
    body.position = x, y
    shp = pymunk.Circle(body, raio, (0, 0))
    space.add(body, shp)
    balls.append(shp)
    
def add_box(x, y, w, h, kinematic=True):
    if kinematic:
        body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
    else:
        massa = w * h * mass_scale
        momento = pymunk.moment_for_box(massa, (w, h))
        body = pymunk.Body(massa, momento)
    body.position = x, y
    shp = pymunk.Poly.create_box(body, (w, h))
    shp.cor = py5.color(100, 0, 0) if kinematic else py5.color(0, 100, 0)
    space.add(body, shp)
    boxes.append(shp)
    
def mouse_pressed():
    global object_creation
    if py5.key == 'k' and py5.is_key_pressed:
        object_creation = (py5.mouse_x, py5.mouse_y, 'k')
    elif py5.key == 'c' and py5.is_key_pressed:
        object_creation = (py5.mouse_x, py5.mouse_y, 'c')
    elif py5.key == 'w' and py5.is_key_pressed:
        object_creation = (py5.mouse_x, py5.mouse_y, 'w')
    elif py5.key == 'p' and py5.is_key_pressed:
        object_creation == ([], 'p')
      
def mouse_released():
    global object_creation
    match  object_creation:
        case inicial_x, inicial_y, kind:
            final_x = py5.mouse_x
            final_y = py5.mouse_y
            if kind in ('k', 'c'):
                w = abs(inicial_x - final_x)
                h = abs(inicial_y - final_y)
                x = (inicial_x + final_x) / 2
                y = (inicial_y + final_y) / 2
                add_box(x, y, w, h, kind == 'k')
            elif kind == 'w':
                add_wall(inicial_x, inicial_y, final_x, final_y)
        case pts, 'p':
            # TODO: add polygon
            print('Poly not implemented yet')
          
    object_creation = None
    
def mouse_dragged():
    if not py5.is_key_pressed:
        for shp in space.shapes:
            info = shp.point_query((py5.mouse_x, py5.mouse_y))
            if info.distance < 2:
                v = pymunk.Vec2d(py5.mouse_x - py5.pmouse_x,
                                 py5.mouse_y - py5.pmouse_y)
                shp.body.position += v
    elif py5.key == 'p':
        object_creation[0].append((py5.mouse_x, py5.mouse_y))
        
        
        
def mouse_wheel(e):
    for shp in space.shapes:
        info = shp.point_query((py5.mouse_x, py5.mouse_y))
        if info.distance < 2:
            shp.body.angle += py5.radians(e.get_count())
    

py5.run_sketch(block=False)




