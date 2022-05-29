import py5


def setup():
    py5.size(800, 800)
    py5.no_stroke()
    py5.color_mode(py5.HSB)
    start_polygons()
    

def start_polygons():
    global poligonos, cores
    poligonos = [
        ((-300, -300), (300, -300), (300, 300), (-300, 300)),
    ]
    
    

def draw():
    py5.background(200)
    py5.translate(py5.width / 2, py5.height / 2)
    h = 0
    for s in poligonos:
        py5.begin_shape()
        xc, yc = centroide(s)
        w, h = py5.width, py5.height
        c = py5.color(64 + py5.dist(xc, yc, -w / 4, -h / 4) % 128,
                      255,
                      64 + py5.dist(xc, yc, w / 4, h / 4) % 128)
        py5.fill(c)
        py5.text_size(16)
        f = 0.3  # map(mouseX, 0, width, 0, 1)
        for i, (x, y) in enumerate(s):
            py5.vertex(x + xc * f, y + yc * f)
            py5.text_align(py5.CENTER, py5.CENTER)
            ox = 5 if xc < x else -5
            oy = 5 if yc < y else -5
            py5.text(i, x + xc * f + ox, y + yc * f + oy)
        py5.end_shape(py5.CLOSE)

def dividir_quad(q):
    d1 = py5.dist(*q[0], *q[2])
    d2 = py5.dist(*q[1], *q[3])
    if d1 < d2: # or q[0][1] < 0: 
        return q[:3], q[2:] + q[:1]
    else:
        return q[1:4], q[3:] + q[:2]

def dividir_tri(t):
    c, a, b = t
    ab = centroide((a, b))
    bc = centroide((b, c))
    ca = centroide((c, a))
    return (
        (ab, a, ca),
        (ab, b, bc),
         (ca, ab, bc, c),
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

py5.run_sketch()
