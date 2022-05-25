import py5


def setup():
    py5.size(700, 700)
    py5.no_stroke()
    py5.color_mode(py5.HSB)
    start_polygons()


def start_polygons():
    global poligonos, cores
    poligonos = [
        ((-300, -300), (300, -300), (300, 300), (-300, 300)),
    ]
    
    

def draw():
    py5.background(0)
    py5.translate(py5.width / 2, py5.height / 2)
    h = 0
    for s in poligonos:
        py5.begin_shape()
        xc, yc = centroide(s)
        w, h = py5.width, py5.height
        c = py5.color(64 + py5.dist(xc, yc,
                                    py5.mouse_x - w / 2,
                                    py5.mouse_y - h / 2) % 128,
                  64 + py5.dist(xc, yc, -w / 4, -h / 4) % 128,
                  64 + py5.dist(xc, yc, w / 4, h / 4) % 128
                  )
        py5.fill(c)
        py5.stroke(c)
        f = 0  # map(mouseX, 0, width, 0, 1)
        for x, y in s:
            py5.vertex(x + xc * f, y + yc * f)
        py5.end_shape(py5.CLOSE)


def dividir_quad(q):
#     if py5.random(100) > 30:
#         return q[:3], q[2:] + q[:1]
#     else:
        return q[1:4], q[3:] + q[:2]

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
    if py5.key == ' ':
        dividir_poligonos()
    elif py5.key == py5.ENTER:
        start_polygons()
    elif py5.key == 's':
        py5.save_frame('###.png')


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

# 
# def dividir_tri(t):
#     c, a, b = t
#     ab = centroide((a, b))
#     bc = centroide((b, c))
#     ca = centroide((c, a))
#     return (
#         (a, ab, ca),
#         (ab, b, bc),
#         (ab, bc, c, ca),
#     )


py5.run_sketch()
