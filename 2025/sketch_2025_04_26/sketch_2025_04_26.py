
import py5
import pymunk


paredes = []
inicio_nova_parede = None

CT_DEFAULT = 0
CT_SPECIAL = 1
CT_WALL = 2

def setup():
    global space
    py5.size(600, 600)
    pymunk.Segment.draw = draw_segment
    pymunk.Circle.draw = draw_circle

    space = pymunk.Space()
    space.gravity = 0, 900
    space.add_collision_handler(
        CT_SPECIAL, CT_DEFAULT
    ).pre_solve = color_collision
    acrescenta_parede(100, 500, 500, 500)

def color_collision(arbiter, space, data):
    s1, s2 = arbiter.shapes
    s2.collision_type=CT_SPECIAL
    s1.collision_type=CT_DEFAULT
    s2.fill= int(py5.color(255, 0, 0))
    s1.fill = 0
    return True

def acrescenta_bola(
    x, y, fill=0, collision_type=CT_DEFAULT
    ):
    corpo = pymunk.Body(10, 100)
    corpo.position = x, y
    forma = pymunk.Circle(corpo, 10, (0, 0))
    forma.friction = 0.99
    forma.stroke = None
    forma.fill = int(fill)
    forma.collision_type=collision_type
    space.add(corpo, forma)

def acrescenta_parede(xa, ya, xb, yb):
    forma = pymunk.Segment(space.static_body,
                           (xa, ya), (xb, yb),
                           radius=1.5)
    forma.collision_type = CT_WALL
    forma.friction = 100.99
    space.add(forma)
    paredes.append(forma)

def draw():  # fica repetindo
    py5.background(0, 0, 200)  # R, G, B
    for shp in space.shapes:
        shp.draw()
        if shp.body.position.y > py5.height + 50:
            space.remove(shp)
     # muitas bolas novas
    if py5.is_key_pressed and py5.key_code == py5.SHIFT:     
        acrescenta_bola(py5.mouse_x + py5.random(-1, 1),
                        py5.mouse_y)
    # mostra preview da parede sendo desenhada
    if inicio_nova_parede:
        py5.stroke(255, 0, 0) # linha vermelha        line(*inicio_nova_parede, mouse_x, mouse_y)
    # avança um passo da simulação
    space.step(1 / 60)
    
def draw_circle(self):
    r = self.radius
    pos = self.body.position
    if self.stroke is not None:
        py5.stroke(self.stroke)
    else:
        py5.no_stroke()
    if self.fill is not None:
        py5.fill(self.fill)
    else:
        py5.no_fill()
    py5.circle(pos.x, pos.y, r * 2)

    
def draw_segment(self):
    py5.stroke(128)
    py5.stroke_weight(3)
    py5.line(self.a.x, self.a.y,
         self.b.x, self.b.y)

def mouse_clicked():
    if py5.key_code == py5.CONTROL:
        f = py5.color(255, 255, 0)
        ct = CT_SPECIAL
    else:
        ct = CT_DEFAULT
        f = 0
    acrescenta_bola(py5.mouse_x + py5.random(-1, 1),
                    py5.mouse_y,
                    fill=f,
                    collision_type=ct)

def mouse_pressed():
    global inicio_nova_parede
    inicio_nova_parede = (py5.mouse_x, py5.mouse_y)
        
def mouse_released():
    global inicio_nova_parede
    if (inicio_nova_parede and
        py5.dist(*inicio_nova_parede,
                 py5.mouse_x, py5.mouse_y) > 5):
        inicio_x, inicio_y = inicio_nova_parede
        acrescenta_parede(inicio_x, inicio_y,
                          py5.mouse_x, py5.mouse_y)
        inicio_nova_parede = None
   
def key_pressed():
    global inicio_nova_parede, space, paredes
    # tecla DELETE apaga paredes
    if py5.key == py5.DELETE and inicio_nova_parede:
        inicio_nova_parede = None
    elif py5.key == py5.DELETE and paredes:
        ultima_parede = paredes.pop()
        space.remove(ultima_parede)
    # "c" limpa bolas
    elif py5.key in ('c', 'C'):
        for shp in space.shapes:
            if isinstance(shp, pymunk.Circle):
                space.remove(shp)
    # "s" salva estado da simulação
    elif py5.key == 's':
        py5.save_pickle((space, paredes), 'space.data')
        print('salvo')
    # "l" (de "load") recarrega estado salvo
    elif py5.key == 'l':
        if py5.Path('space.data').is_file():
            space, paredes = py5.load_pickle('space.data')

    print(f'objetos simulados: {len(space.shapes)}')

py5.run_sketch(block=False)
