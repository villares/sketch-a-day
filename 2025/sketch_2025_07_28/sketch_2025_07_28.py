from itertools import product

import py5
import shapely

from villares.arc_helpers import arc_pts, arc_corner, arc_filleted_poly

grid = list(product(range(150, 800, 250), repeat=2))

def setup():
    py5.size(800, 800)
    py5.stroke_join(py5.ROUND)
    py5.no_loop()
    
def draw():
    py5.background(240, 240, 200)
    py5.stroke_weight(10)
    py5.stroke(255)
    py5.points(grid)
    py5.no_fill()
    py5.stroke_weight(8)
    py5.stroke(0)
    self_intersecting = True
    while self_intersecting:
        pts = py5.random_sample(grid, 5, replace=False)
        self_intersecting = is_poly_self_intersecting(pts)
    shp = shapely.Polygon(pts)
    py5.shape(shp)
    py5.stroke_weight(5)
    py5.stroke(0, 0, 200)
    arc_filleted_poly(pts, radius=50)
#     with py5.begin_closed_shape():
#         for i, p in enumerate(pts[:-1]):
#             pp = pts[i -1]
#             np = pts[i + 1]
#             arc_corner(p, pp, np, 50)
    py5.fill(0)
    py5.text_size(20)
    py5.text('Testig arc_filleted_poly()', 20, 50)
    py5.text(f"""{pts}
shapey is_simple: {shp.is_simple}
shapely is_valid: {shp.is_valid}
my naïve is_poly_self_intersecting: {is_poly_self_intersecting(pts)}
""", 20, py5.height - 90)
    
    
def key_pressed():
    py5.save_frame('###.png')
    py5.redraw()
    

def is_poly_self_intersecting(poly_points):
    edges = pairwise(poly_points) + [(poly_points[-1], poly_points[0])]
    for a, b in edges[::-1]:
        for c, d in edges[2::]:
            # test only non consecutive edges
            if (a != c) and (b != c) and (a != d):
                if simple_intersect(a, b, c, d):
                    return True
    return False

def pairwise(iterable):
    from itertools import tee
    "s -> (s0, s1), (s1, s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return list(zip(a, b))

def ccw(*args):
    """Returns True if the points are arranged counter-clockwise in the plane"""
    if len(args) == 1:
        a, b, c = args[0]
    else:
        a, b, c = args
    return (b[0] - a[0]) * (c[1] - a[1]) > (b[1] - a[1]) * (c[0] - a[0])

def simple_intersect(*args):
    """Returns True if line segments intersect."""
    if len(args) == 2:    
        (a1, b1), (a2, b2) = args[0], args[1]
    else:
        a1, b1, a2, b2 = args
    return ccw(a1, b1, a2) != ccw(a1, b1, b2) and ccw(a2, b2, a1) != ccw(a2, b2, b1)


    
py5.run_sketch(block=False)