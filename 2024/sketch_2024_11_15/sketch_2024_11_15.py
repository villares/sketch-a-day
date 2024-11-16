import py5

from py5 import Py5Vector as V

sqrt2 = py5.sqrt(2)
    
def setup():
    py5.size(500, 500)
    py5.background(0, 0, 200)
    py5.translate(200, 100)
    py5.stroke_weight(5)
    start = V(0, 0)
    heading = 0
    pts = [start]
    seg_size = 80
    for i in range(15):
        if i % 2 == 0:
            heading += py5.radians(-45)
        else:
            heading += py5.radians(90)
        seg = V.from_heading(heading) * seg_size
        start = start + seg
        pts.append(start)
    draw_poly(pts)        

def draw_poly(pts):
    with py5.begin_closed_shape():
        py5.vertices(pts)

py5.run_sketch(block=False)