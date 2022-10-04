import py5
from math import sin, cos, tau

pontos = []
starting_points = [(420 + 150 * cos(i * tau / 3), 420 + 150 * sin(i * tau / 3))
                    for i in range(3)]

def setup():
    py5.size(840, 840, py5.P3D)
    py5.stroke_weight(3)
    py5.no_fill()
    py5.color_mode(py5.HSB)
    pontos.extend(starting_points)
    
def draw():
    py5.background(240)
    py5.translate(py5.width /2 , py5.height / 2)
    py5.rotate_x(py5.HALF_PI / 2)
    py5.translate(-py5.width /2 , -py5.height / 2, 300)
    pts = pontos[:]
    for i in range(10):
        py5.stroke(i * 24, 200, 200)
        with py5.begin_closed_shape():
            py5.curve_vertex(*pts[-1])
            py5.curve_vertices(pts)
            py5.curve_vertex(*pts[0])
            py5.curve_vertex(*pts[1])
        py5.translate(0, 0, -40)
        pts[:] = processar(pts)
    
def key_pressed():
    if py5.key == ' ':
        pontos[:] = processar(pontos)
    elif py5.key == 'r':
        pontos[:] = starting_points
     
def processar(pts):
    src_pts = pts + [pts[0]]
    for a, b in zip(src_pts[:-1], src_pts[1:]):
        va = py5.Py5Vector(a)
        vb = py5.Py5Vector(b)
        vd = (va - vb).rotate(py5.HALF_PI) * 0.50   
        mp = (va + vb) / 2
        yield a
        yield tuple(mp + vd)
    
py5.run_sketch(block=False)