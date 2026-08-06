# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org

import py5
import shapely

shapes = []

def setup():
    py5.size(600, 600)
    global un
    shapes.extend((
       shapely.LineString(((100, 100), (200, 100), (200, 200))), 
       shapely.LineString(((100, 200), (200, 200), (200, 300))), 
       shapely.LineString(((200, 100), (300, 100), (300, 200))), 
       shapely.LineString(((200, 200), (300, 200), (300, 300))), 
       shapely.LinearRing(((300, 300), (200, 300),
                           (200, 400), (400, 400))),
       shapely.LineString(((100, 100), (100, 200))), 
    ))
    un = shapely.unary_union(shapes)
    
def draw():
    py5.background(200)
    py5.stroke_weight(3)
    for shp in shapes:
        py5.stroke(py5.random_int(255), py5.random_int(255), py5.random_int(255)) 
        py5.shape(shp)
    py5.stroke(0)
    for u in un.geoms:
        py5.translate(2, 5)
        print(u)
        py5.shape(u)

def key_pressed():
    if py5.key == 's':
        py5.save_frame('###.png')

py5.run_sketch(block=False)
