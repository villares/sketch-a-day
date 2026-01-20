from itertools import product

import py5
import shapely

pts = []
MARGIN = 50
N = 16
R = 0

def setup():
    py5.size(800, 800)
    py5.stroke_join(py5.ROUND)
    py5.no_fill()
    w = (py5.width - MARGIN * 2) / N
    xs = [w / 2 + MARGIN + i * w + py5.random(-1, 1) * R
           for i in range(N)]
    ys = [w / 2 + MARGIN + i * w + py5.random(-1, 1) * R
       for i in range(N)]
    pts.extend(product(xs, ys))
    pts[:] = py5.random_permutation(pts)
    p = shapely.Polygon(pts)
  

def draw():
    py5.background(0)
    py5.stroke(255)
    py5.stroke_weight(2)
    with py5.begin_closed_shape():
        py5.curve_vertices(pts)
        #py5.vertices(pts)
    py5.stroke(255, 0, 0)
    py5.stroke_weight(4)
    py5.points(pts)
    
def key_pressed():
    py5.save_frame('out.png')
    
py5.run_sketch(block=False)
        
