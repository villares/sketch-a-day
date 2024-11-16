import py5

from py5 import Py5Vector as Vector
    
def setup():
    py5.size(500, 500)
    py5.background(0, 0, 200)
    py5.translate(200, 100)
    py5.stroke_weight(5)
    current_pos = Vector(0, 0)
    heading = 0
    segment_size = 80
    pts = [current_pos]
    for i in range(15):
        if i % 2 == 0:
            heading += py5.radians(-45)
        else:
            heading += py5.radians(90)
        current_pos = current_pos + Vector.from_heading(heading) * segment_size
        pts.append(current_pos)
    draw_poly(pts)        

def draw_poly(pts):
    with py5.begin_closed_shape():
        py5.vertices(pts)

py5.run_sketch(block=False)
