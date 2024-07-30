being_dragged = None

pts = [
    (100, 50),   # 0: vertex() initial anchor
    (150, 100),  # 1: pt de controle
    (250, 100),  # 2: vertex and anchor to next curve
    (250, 200),  # 3: pt de controle
    (150, 200),  # 4: vertex and anchor to next curve
    (50, 200),   # 5: pt de controle
    (50, 100),   # 6: final vertex
    ]

s = 2 # scale factor

def setup():
    size(800, 600)

def draw():
    scale(s)
    background(100)
    
    # gray thin lines to control points
    stroke_weight(1)
    stroke(200)
    for i, (x, y) in enumerate(pts):
        if i != 0 and i % 2 == 0: # even index, skip 0
            v0x, v0y = pts[i - 2]
            c1x, c1y = pts[i - 1]
            line(v0x, v0y, c1x, c1y)
            line(c1x, c1y, x, y)
    # the curves, thick and black
    stroke_weight(3)
    stroke(0)
    no_fill()

    with begin_shape():
        vertex(pts[0][0], pts[0][1])  # primeiro pt (índice 0)
        for (px, py), (x, y) in zip(pts[1::2], pts[2::2]):  
            # do segundo e terceiro pts (índices 1 e 2) em diante 
            quadratic_vertex(px, py, x, y)
    # the handles
    stroke_weight(1)
    for i, pt in enumerate(pts):
        x, y = pt
        if i == being_dragged:
            fill(200, 0, 0)
        elif dist(mouse_x, mouse_y, x, y) < 10:
            fill(255, 255, 0)
        else:
            fill(255)
        ellipse(x, y, 5, 5)
        t = f'{i}: {"vertex" if i == 0 else "control" if i % 2 else "quadratic"}'
        text(t, x + 5, y - 5)

def mouse_pressed():
    global being_dragged
    for i, pt in enumerate(pts):
        x, y = pt
        if dist(mouse_x / s, mouse_y / s, x, y) < 10:
            being_dragged = i
            break 

def mouse_released():
    global being_dragged
    being_dragged = None

def mouse_dragged():
    global pts
    global being_dragged
    if being_dragged is not None:
        x, y = pts[being_dragged]
        x += (mouse_x - pmouse_x) / s
        y += (mouse_y - pmouse_y) / s
        pts[being_dragged] = x, y 