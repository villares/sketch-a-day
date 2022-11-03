arrastando = None  # None quer dizer nenhum círculo sendo arrastado
handles = []  # lista com coordenadas e tamanhos dos círculos
poly = []
d = 10
n = 0

def setup():
    size(400, 400)
    stroke_weight(3)
    fill(0, 200)  # preenchimento translúcido
    reset()
    
def reset():
    handles[:] = []
    for _ in range(5):  # vamos sortear4 círculos
        x = random(d, width - d)
        y = random(d, height - d)
        handles.append((x, y))
    poly[:] = handles

def draw():
    background(0, 0, 200)
    no_fill()
    stroke(255)
    stroke_weight(1)
    with begin_shape():
        vertices(handles)
    stroke(0)
    stroke_weight(3)
    with begin_shape():
        vertices(poly)
    fill(0)
    for i, handle in enumerate(handles):
        x, y = handle
        if i == arrastando:
            stroke(200, 0, 0)
        else:
            stroke(255)
        ellipse(x, y, d, d)
    fill(255, 0, 0)

    poly[:] = handles
    for _ in range(n):
        iterate()

def iterate():
    new_points = [poly[0]]
    for a, b in zip(poly, poly[1:]):
        new_points.extend(rot_scale(poly, a, b)[1:])    
    poly[:] = new_points


def mouse_pressed():  # quando um botão do mouse é apertado
    global arrastando
    # vamos olhar um círculo por vez da lista `handles`
    for i, handle in enumerate(handles):  # i é o índice na lista
        x, y = handle
        dist_mouse_handle = dist(mouse_x, mouse_y, x, y)
        raio = d / 2
        if dist_mouse_handle < raio:  # se o mouse estiver dentro
            arrastando = i
            break  # interrompe o laço, não checa mais outros!

def  rot_scale(pts, pa, pb):
     (x0, y0), (xf, yf) = pa, pb
     d = dist(x0, y0, xf, yf)
     new_h = Py5Vector(xf - x0, yf - y0).heading
     vs = to_vectors(pts) # first pt is orgin; len(vs) == len(pts) - 1
     rot_scaled = rotate_vectors(scale_vectors(vs, d), new_h)
     # add (x0, y0) and translate others adding (x0, y0)
     return [(x0, y0)] + [(x0 + x, y0 + y) for x, y in rot_scaled]

def to_vectors(pts):
    x0, y0 = pts[0]
    return [Py5Vector(x - x0, y - y0) for x, y in pts[1:]]

def scale_vectors(vs, target_mag):
    s = target_mag / vs[-1].mag
    return [v * s for v in vs]

def rotate_vectors(vs, target_heading):
    rot = target_heading - vs[-1].heading
    return [v.rotate(rot) for v in vs]


def mouse_released():  # quando um botão do mouse é solto
    global arrastando
    arrastando = None
    #poly[:] = handles[:] = new_points

def mouse_dragged():  # quando o mouse é movido apertado
    if arrastando is not None:
        x, y = handles[arrastando]
        x += mouse_x - pmouse_x
        y += mouse_y - pmouse_y
        handles[arrastando] = (x, y)
        
def key_pressed():
    global n
    if key == ' ':
        reset()
    elif str(key) in '=+':
        n += 1
    elif key == '-':
        n -= 1
