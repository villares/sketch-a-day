from itertools import product

from shapely import Polygon
import py5

def setup():
    py5.size(600, 600)
    py5.color_mode(py5.HSB)
    start()
    
def start():
    global ps
    p = Polygon([(x, y) for x, y
                 in product(range(-200, 201, 100),
                            repeat=2)]).buffer(0)
    ps = [p]
    
def draw():
    #py5.background(230, 240, 240)
    py5.translate(py5.width / 2, py5.height / 2)
    for p in ps:
        py5.no_fill()
        py5.stroke(p.area % 255, 200, 200, 32)
        py5.shape(py5.convert_cached_shape(p))
   
def shrink():
    p = ps[-1]
    new_p = p.buffer(-10, cap_style='round')
    print(new_p.area)
    while new_p.area > 0:
        new_p = ps[-1].buffer(-10, cap_style='round')
        ps[-1] = ps[-1].difference(new_p)
        ps.append(new_p)
        

def grow():
    p = ps[-1]
    new_p = p.buffer(10, cap_style='round')
    while new_p.area < 1000000:
        new_p = ps[-1].buffer(10, cap_style='round')
        ps.append(new_p.difference(ps[-1]))


def key_pressed():
    if py5.key == 's':
        py5.save_frame('out###.png')
    elif py5.key == ' ':
        start()
    elif py5.key == 'a':
        shrink()
    elif py5.key == 'z':
        grow()
        
py5.run_sketch(block=False)