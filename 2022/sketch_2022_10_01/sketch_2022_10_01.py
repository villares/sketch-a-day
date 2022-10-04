import py5

pontos = []
starting_points = [(300, 450), (500, 450), (400, 276)]

def setup():
    py5.size(800, 800)
    py5.stroke_weight(3)
    #py5.no_fill()
    pontos.extend(starting_points)
    
def draw():
    py5.background(240, 240, 220)
    py5.fill(255, 64)
    with py5.begin_closed_shape():
        py5.curve_vertex(*pontos[-1])
        py5.curve_vertices(pontos)
        py5.curve_vertex(*pontos[0])
        py5.curve_vertex(*pontos[1])
    
def key_pressed():
    if py5.key == ' ':
        pontos[:] = processar(pontos + [pontos[0]])[:-1]
    elif py5.key == 'r':
        pontos[:] = starting_points
     
def processar(pts):
    new_pts = []
    for a, b in zip(pts[:-1], pts[1:]):
        va = py5.Py5Vector(a)
        vb = py5.Py5Vector(b)
        vd = (va - vb).rotate(py5.HALF_PI) / 2   
        mp = (va + vb) / 2
        new_pts.append(a)
        new_pts.append(tuple(mp + vd))
    new_pts.append(pts[-1])
    return new_pts
    
py5.run_sketch(block=False)