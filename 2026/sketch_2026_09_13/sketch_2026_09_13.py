
import py5
import shapely
from shapely import Point, Polygon

def setup():
    py5.size(700, 400)
    
    ref = py5.load_image('piso.jpg')
    py5.image(ref, 400, 0, ref.width / 10, ref.height / 10)
    sq = Polygon([(50, 50), (150, 50), (150, 150), (50, 150)])
    ca = Point(100, 200).buffer(100)
    cb = Point(200, 200).buffer(100)
    cc = Point(200, 100).buffer(100)

    ic = (ca & cc) - cb
    py5.fill(0, 0, 100, 100)
    py5.shape(sq)
    py5.fill(0, 100)
    py5.shape(ca)
    py5.shape(cb)
    py5.shape(cc)
    py5.fill(255, 100)
    py5.shape(ic)
    py5.fill(0)
    py5.square(250, 275, 100)
    py5.fill(255)
    c = shapely.affinity.translate(ic, 200, 225)
    py5.shape(c)
    for _ in range(3):
        c = shapely.affinity.rotate(c, 90, (300, 325))
        py5.shape(c)
    
    py5.save_frame('out.png')

py5.run_sketch()



