


def setup():
    size(700, 700)
    no_stroke()
    fill(0)
    color_mode(HSB)
    start_polygons()
    
def start_polygons():
    global poligonos
    poligonos = [
    ((-300, -300), (300, -300), (300, 300), (-300, 300)),
    ]


def draw():
    background(0)
    translate(width / 2, height / 2)
    for s in poligonos:
        begin_shape()
        xc, yc = centroide(s)
        fill(64 + dist(xc, yc, 0, 0) % 128, 200, 200)
        f = 0.1  # map(mouseX, 0, width, 0, 1)
        for x, y in s:
            vertex(x + xc * f, y + yc * f)
        end_shape(CLOSE)


def dividir_quad(q):
    return q[:3], q[2:] + q[:1]


def dividir_tri(t):
    a, c, b = t
    ab = centroide((a, b))
    bc = centroide((b, c))
    ca = centroide((c, a))
    return (
        (ab, a, ca),
        (ab, b, bc),
        (ab, bc, c, ca),
    )


def centroide(s):
    xs, ys = zip(*s)
    return (sum(xs) / len(xs),
            sum(ys) / len(ys))


def key_pressed():
    if key == ' ':
        dividir_poligonos()
    elif key == ENTER:
        start_polygons()
    elif key == 's':
        save_frame('###.png')


def dividir_poligonos():
    novos_poligonos = []
    for p in poligonos:
        novos_poligonos.extend(dividir(p))
    poligonos[:] = novos_poligonos


def dividir(p):
    if len(p) == 4:
        return dividir_quad(p)
    else:
        return dividir_tri(p)

def dividir_tri(t):
    a, c, b = t
    ab = centroide((a, b))
    bc = centroide((b, c))
    ca = centroide((c, a))
    return (
        (ab, a, ca),
        (ab, b, bc),
        (ca, ab, bc, c),
        )

def dividir_tri(t):
    c, a, b = t
    ab = centroide((a, b))
    bc = centroide((b, c))
    ca = centroide((c, a))
    return (
        (a, ab, ca),
        (ab, b, bc),
        (ab, bc, c, ca),
        )
