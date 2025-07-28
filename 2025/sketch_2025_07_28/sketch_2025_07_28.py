from itertools import product

import py5
import shapely

from villares.arc_helpers import is_poly_self_intersecting
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
    
py5.run_sketch(block=False)