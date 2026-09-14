
import py5
from shapely import Point

def setup():
    py5.size(400, 400)

    ca = Point(100, 200).buffer(100)
    cb = Point(200, 200).buffer(100)
    ic = ca & cb
    py5.fill(0)
    py5.shape(ca)
    py5.shape(cb)
    py5.fill(255)
    py5.shape(ic)
    
    py5.save_frame('out.png')

py5.run_sketch()



