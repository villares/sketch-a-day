import py5
from shapely import Polygon

margem = 2


def setup():
    py5.size(800, 800)
    py5.color_mode(py5.HSB)
    start_polygons()
    
def start_polygons(n=7):
    global poligonos
    W = py5.width - 2 * margem 
    poligonos = [
        ((0, 0), (W, 0), (W, W), (0, W)),
    ]
    for _ in range(n):
        dividir_poligonos()   
    
def draw():
    py5.background(0)
    py5.color_mode(py5.HSB)
    py5.translate(margem, margem)
    for shp in poligonos:
        #py5.stroke_weight(1.5)
        draw_shrinking_shape(shp)

def draw_shrinking_shape(shp):
    p = Polygon(shp)
    c = 0
    while p.area > 0:
        py5.stroke(96 + c % 64, 200, 128 + 64 * (c % 2))
        py5.fill(96 + c % 64, 200, 128 + 64 * (c % 2))
        py5.shape(py5.convert_shape(p))
        p = p.buffer(-2)
        c += 15
    

def dividir_quad(q):
    d1 = py5.dist(*q[0], *q[2])
    d2 = py5.dist(*q[1], *q[3])
    if d1 < d2: 
        return q[:3], q[2:] + q[:1]
    else:
        return q[1:4], q[3:] + q[:2]

def dividir_tri(t):
    b, c, a = t
    ab = centroide((a, b))
    bc = centroide((b, c))
    ca = centroide((c, a))
    ta, tb = dividir_quad((ca, ab, bc, c))
    return (
        (ab, bc, b),
        (ab, a, ca),
        ta, tb,
        )

def centroide(s):
    xs, ys = zip(*s)
    return (sum(xs) / len(xs),
            sum(ys) / len(ys))

def key_pressed():
    if py5.key == ' ':
        py5.save_frame('out.png')
       
def dividir_poligonos():
    novos_poligonos = []
    for i, p in enumerate(poligonos):
        if i % 2 == 0:
            novos_poligonos.extend(dividir(p))
        else:
            novos_poligonos.append(p)
    poligonos[:] = novos_poligonos


def dividir(p):
    if len(p) == 4:
        return dividir_quad(p)
    else:
        return dividir_tri(p)

py5.run_sketch()

