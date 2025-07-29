from itertools import product

import py5
import shapely

from villares.arc_helpers import arc_pts, arc_corner, arc_filleted_poly, p_arc

import villares.arc_helpers
villares.arc_helpers.DEBUG = True

grid = list(product(range(150, 800, 250), repeat=2))

def setup():
    py5.size(800, 800)
    py5.stroke_join(py5.ROUND)
    make_pts()
    
def make_pts():
    global pts
    self_intersecting = True
    while self_intersecting:
        pts = py5.random_sample(grid, 5, replace=False)
        self_intersecting = is_poly_self_intersecting(pts)
        
def draw():
    py5.background(240, 240, 200)
    py5.stroke_weight(10)
    py5.stroke(255)
    py5.points(grid)
    py5.no_fill()
    py5.stroke_weight(8)
    py5.stroke(0)

    
    pts[2] = py5.mouse_x, py5.mouse_y
    shp = shapely.Polygon(pts)
    py5.shape(shp)
    py5.stroke_weight(3)
    py5.stroke(0, 0, 200)
    arc_filleted_poly(pts, radius=50)
    py5.stroke_weight(3)
    py5.stroke(0, 255, 0)
    vs = arc_filleted_poly(pts, radius=50, arc_func=arc_pts)
    py5.points(vs)
    py5.fill(0)
    py5.text_size(20)
    py5.text('Testig arc_filleted_poly()', 20, 50)
    py5.text(f"""{pts}
shapely based is_poly_self_intersecting: {is_poly_self_intersecting(pts)}
""", 20, py5.height - 90)
    
def is_poly_self_intersecting(pts):
    return not shapely.Polygon(pts).is_simple

def key_pressed():
    py5.save_frame('###.png')
    make_pts()
    
py5.run_sketch(block=False)