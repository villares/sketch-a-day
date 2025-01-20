import py5
from shapely import Polygon

margem = 10
color_offset = 0


def setup():
    py5.size(800, 800) 
    start_polygons()
    
def start_polygons(n=5):
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
        xc, yc = centroide(shp)
        x0, y0 = shp[0]
        w, h = py5.width, py5.height      
        draw_shrinking_shape(shp)
    

def draw_shrinking_shape(shp):
    p = Polygon(shp)
    c = 0
    while p.area > 0:
        py5.no_stroke()
        fc = py5.color(
            (color_offset + c % 45) % 255,
             240, 150 + 50 * (c % 2))
        py5.fill(fc)
        py5.shape(py5.convert_shape(p))
        p = p.buffer(-5)
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
    return (
        (ca, ab, bc, c),
        (ab, bc, b),
        (ab, a, ca),
    )

def centroide(s):
    xs, ys = zip(*s)
    return (sum(xs) / len(xs),
            sum(ys) / len(ys))

def key_pressed():
    global color_offset
    if py5.key == 's':
        py5.save_frame(f'{color_offset}.png')
    elif py5.key == ' ':
        color_offset += 255 / 5
    
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

