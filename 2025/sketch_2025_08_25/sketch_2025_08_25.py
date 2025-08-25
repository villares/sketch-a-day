import py5
from shapely import Polygon, Point

def setup():
    py5.size(400, 400)
    py5.stroke_join(py5.ROUND)
    
def draw():
    py5.background(200)
    pts = ((100, 100), (300, 100),
           (py5.mouse_x, py5.mouse_y))
    xs, ys = zip(*pts)
    cx = sum(xs) / len(xs)
    cy = sum(ys) / len(ys)
    tri = Polygon(pts)
    py5.no_fill()
    py5.stroke_weight(1)
    py5.stroke(0, 200, 0)
    py5.shape(Point(cx, cy).buffer(5))
    py5.stroke(0, 0, 200)
    py5.shape(tri.envelope.buffer(2))
    py5.shape(tri.envelope.centroid.buffer(5))
    py5.stroke_weight(3)
    py5.stroke(0)
    py5.shape(tri)
    py5.fill(0)
    py5.shape(tri.centroid.buffer(2))

py5.run_sketch(block=False)