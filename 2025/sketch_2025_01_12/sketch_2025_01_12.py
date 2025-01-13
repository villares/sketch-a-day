import py5

margem = 10

def setup():
    py5.size(800, 800) 
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
        xc, yc = centroide(shp)
        x0, y0 = shp[0]
        w, h = py5.width, py5.height
        d = py5.dist(xc, yc, x0, y0)
        c = py5.color(32 + (yc * 1.5) % 128,
                      255 - d,
                      192 + xc % 64,
                      )        
        py5.fill(c)
        py5.stroke(0)
        py5.stroke_weight(1.5)
        py5.begin_shape()
        py5.vertices(shp)
        py5.end_shape(py5.CLOSE)
    

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
    if py5.key == ' ':
        py5.save_frame('out.png')
       
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

