import py5
import shapely
from shapely import Polygon

def setup():
    py5.size(500, 500)
    py5.no_fill()
    s = Polygon((
        (100, 100), (400, 100),
        (400, 400), (100, 400)
        ))
    py5.shape(s)
    for _ in range(90):
        s = shapely.affinity.rotate(s, 5).buffer(-5)
        py5.shape(s)
        

    


py5.run_sketch(block=False)
