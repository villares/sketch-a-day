
import py5
import shapely
from shapely import Point, Polygon
 
def setup():
    py5.size(400, 400)
    py5.background(128)
    sq = Polygon([(-50, -50), (50, -50), (50, 50), (-50, 50)])
    ca = Point(0, 100).buffer(100)
    cb = Point(100, 100).buffer(100)
    cc = Point(100, 0).buffer(100)
    ic = (ca & cc) - cb
    py5.no_stroke()
    for i in range(4):
        for j in range(4):
            py5.push_matrix()
            py5.translate(50 + i * 100, 50 + j * 100)    
            py5.fill(128)
            py5.stroke(100)
            py5.shape(sq)
            py5.fill(255 if (i+j)%2==0 else 0)
            c = shapely.affinity.translate(ic, 0, 0)
            py5.shape(c)
            for _ in range(3):
                c = shapely.affinity.rotate(c, 90, (0, 0))
                py5.shape(c)
            py5.pop_matrix()
                        
    py5.save_frame('out.png')

py5.run_sketch()



