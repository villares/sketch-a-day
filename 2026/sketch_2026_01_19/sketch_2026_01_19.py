from itertools import product

import py5

pts = []
MARGIN = 50
N = 16

def setup():
    py5.size(800, 800)
    py5.stroke_weight(3)
    py5.stroke(255)
    py5.no_fill()
    w = (py5.width - MARGIN * 2) / N
    xs = [w / 2 + MARGIN + i * w + py5.random(-5, 5)
           for i in range(N)]
    ys = [w / 2 + MARGIN + i * w + py5.random(-5, 5)
       for i in range(N)]
    pts.extend(product(xs, ys))
    pts[:] = py5.random_permutation(pts)

def draw():
    py5.background(0)
    with py5.begin_closed_shape():
        py5.curve_vertices(pts)
    
py5.run_sketch(block=False)
        
