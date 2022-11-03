arrastando = None  # None quer dizer nenhum círculo sendo arrastado
handles = []  # lista com coordenadas e tamanhos dos círculos
poly = []
new_points = []
d = 10


def setup():
    size(400, 400)
    stroke_weight(3)
    fill(0, 200)  # preenchimento translúcido
    for _ in range(5):  # vamos sortear4 círculos
        x = random(d, width - d)
        y = random(d, height - d)
        handles.append((x, y))
    poly[:] = handles

def draw():
    background(0, 0, 200)
    no_fill()
    stroke(0)
    with begin_shape():
        for x, y in poly:
            vertex(x, y)
    fill(0)
    for i, handle in enumerate(handles):
        x, y = handle
        if i == arrastando:
            stroke(200, 0, 0)
        else:
            stroke(255)
        ellipse(x, y, d, d)
    fill(255, 0, 0)
    x0, y0 = handles[0]
    for x, y in new_points:
        ellipse(x, y, d / 2, d / 2)

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

    

def grab_vectors(pts):
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
    poly[:] = handles[:] = new_points

def mouse_dragged():  # quando o mouse é movido apertado
    if arrastando is not None:
        x, y = handles[arrastando]
        x += mouse_x - pmouse_x
        y += mouse_y - pmouse_y
        handles[arrastando] = (x, y)
    if arrastando != len(handles) - 1:
        poly[:] = handles[:] 
    x0, y0 = handles[0][0], handles[0][1]
    xf, yf = handles[-1][0], handles[-1][1]
    d = dist(x0, y0, xf, yf)
    new_h = Py5Vector(xf - x0, yf - y0).heading
    vs = grab_vectors(poly)
    rot_scaled = rotate_vectors(scale_vectors(vs, d), new_h)
    new_points[:] = [(x0, y0)] + [(x0 + x, y0 + y) for x, y in rot_scaled]
