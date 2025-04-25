# Código para py5 "imported mode" precisa de um "sketch runner"
# Saiba mais em: https://abav.lugaralgum.com/como-instalar-py5/

import pymunk

space = pymunk.Space()
space.gravity = 0, 900

bolinhas = []  
paredes = []
inicio_nova_parede = None

def setup():
    size(600, 600)
    acrescenta_parede(100, 500, 500, 500)
    
def acrescenta_bola(x, y):
    corpo = pymunk.Body(10, 100)
    corpo.position = x, y
    forma = pymunk.Circle(corpo, 10, (0, 0))
    forma.friction = 0.99
    space.add(corpo, forma)
    bolinhas.append(forma)

def acrescenta_parede(xa, ya, xb, yb):
    forma = pymunk.Segment(space.static_body,
                           (xa, ya), (xb, yb),
                           radius=1.5)
    forma.friction = 100.99
    space.add(forma)
    paredes.append(forma)

def draw():  # fica repetindo
    background(0, 0, 200)  # R, G, B
    for bola in bolinhas.copy():
        r = bola.radius
        pos = bola.body.position
        no_stroke()
        fill(0)
        circle(pos.x, pos.y, r * 2)
        # remover bolas que cairam pra baixo da tela
        if pos.y > height + 50:
            bolinhas.remove(bola)
            space.remove(bola)
    # desenhar linhas-parede (simplifiquei!)
    for parede in paredes:
        stroke(128)
        stroke_weight(3)
        line(parede.a.x, parede.a.y,
             parede.b.x, parede.b.y)
    # muitas bolas novas
    if is_key_pressed and key_code == SHIFT:     
        acrescenta_bola(mouse_x + random(-1, 1), mouse_y)
    # mostra preview da parede sendo desenhada
    if inicio_nova_parede:
        stroke(255, 0, 0) # linha vermelha
        line(*inicio_nova_parede, mouse_x, mouse_y)
    # avança um passo da simulação
    space.step(1 / 60)
    
def mouse_pressed():
    global inicio_nova_parede
    if key_code == CONTROL:
        acrescenta_bola(mouse_x + random(-1, 1), mouse_y)
    else:
        inicio_nova_parede = (mouse_x, mouse_y)
        
def mouse_released():
    global inicio_nova_parede
    if (inicio_nova_parede and
        dist(*inicio_nova_parede, mouse_x, mouse_y) > 5):
        inicio_x, inicio_y = inicio_nova_parede
        acrescenta_parede(inicio_x, inicio_y,
                          mouse_x, mouse_y)
        inicio_nova_parede = None
   
def key_pressed():
    global inicio_nova_parede, space, bolinhas, paredes
    # tecla DELETE apaga paredes
    if key == DELETE and inicio_nova_parede:
        inicio_nova_parede = None
    elif key == DELETE and paredes:
        ultima_parede = paredes.pop()
        space.remove(ultima_parede)
    # "c" limpa bolas
    elif key == 'c' or key == 'C':
        for bola in bolinhas.copy():
            bolinhas.remove(bola)
            space.remove(bola)
    # "s" salva estado da simulação
    elif key == 's':
        save_pickle((space, bolinhas, paredes), 'space.data')
        print('salvo')
    # "l" (de "load") recarrega estado salvo
    elif key == 'l':
        if Path('space.data').is_file():
            space, bolinhas, paredes = load_pickle('space.data')

    print(f'objetos simulados: {len(space.shapes)}')
