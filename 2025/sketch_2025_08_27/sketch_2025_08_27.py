from itertools import product, permutations, combinations

import py5
from py5_tools import animated_gif
from shapely import Polygon, MultiPolygon, LineString, MultiLineString
from shapely import unary_union

def setup():
    global perms
    py5.size(17 * 80, 12 * 80)
    #animated_gif('out.gif', duration=1, frame_numbers=range(1, 21))
    py5.stroke_join(py5.ROUND)
    # 362880 permutations of 9 points
    grid = list(product((-1, 0, 1), repeat=2))   
    perms = set()  # 280 equivalent "tri shapes"
    for a, b, c, d, e, f, g, h, i in permutations(grid, 9):
       perms.add(
           frozenset((
               frozenset((a, b, c)),
               frozenset((d, e, f)),
               frozenset((g, h, i)),
           ))
       )
    print(len(perms))
    # filter out degenerate triangle / colinear points
    perms = [
        (ta, tb, tc) for ta, tb, tc in perms
        if Polygon(ta).area and Polygon(tb).area and Polygon(tc).area 
        ]
    print(len(perms))
    perms.sort(key=lambda p: (unary_union((
        Polygon(p[0]), Polygon(p[1]),Polygon(p[2]))).area))
            
def draw():
    py5.background(240)
    py5.no_fill()
    p = 0
    s = 80
    w = 35
    for r in range(12):
        for c in range(17):
            x = s / 2 + s * c
            y = s / 2 + s * r
            draw_comp(p, x, y, w)
            p += 1
            
def draw_comp(p, x, y, w):
    with py5.push_matrix():
        py5.translate(x, y)
        py5.scale(w)
        tri = perms[p]
        for poly, angle in zip(tri, (py5.HALF_PI / 2, py5.HALF_PI, 0)):
            #py5.stroke(c)
            hatched_poly(
                poly,
                angle=angle,
                spacing=0.06
                )

def hatched_poly(poly, angle=0, holes=[], spacing=5):
    if not isinstance(poly, (Polygon, MultiPolygon)):
        poly = Polygon(poly, holes)
    py5.stroke_weight(0.03)    
    py5.shape(py5.convert_shape(poly))
    py5.stroke_weight(0.01)    
    hatch = generate_hatch(poly, angle=angle,spacing=spacing)
    py5.shape(py5.convert_shape(hatch))
 
def generate_hatch(poly, angle=0, spacing=5, holes=[]):
    if not isinstance(poly, (Polygon, MultiPolygon)):
        poly = Polygon(poly, holes)
    elif poly.area == 0:
        return MultiLineString()
    diagonal = py5.dist(*poly.bounds)  # diagonal length
    #print(poly.bounds, diagonal, poly.area)
    num = int(diagonal / spacing)
    V = py5.Py5Vector
    centroid = V(poly.envelope.centroid.x, poly.envelope.centroid.y)
    a = V(-diagonal / 2, -diagonal / 2).rotate(angle) + centroid
    b = V(-diagonal / 2, +diagonal / 2).rotate(angle) + centroid
    c = V(+diagonal / 2, -diagonal / 2).rotate(angle) + centroid
    d = V(+diagonal / 2, +diagonal / 2).rotate(angle) + centroid
    lines = [LineString((V.lerp(a, b, i / num), V.lerp(c, d, i / num)))
             for i in range(num + 1)]
    return MultiLineString(lines).intersection(poly)

def key_pressed():
    py5.save('out.png')

py5.run_sketch(block=False)

