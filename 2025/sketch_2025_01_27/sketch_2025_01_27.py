from itertools import product

from shapely import Polygon
import py5

B = 6

def setup():
    py5.size(600, 600)
    py5.stroke_weight(1.5)
    py5.stroke_join(py5.ROUND)
    start()
    grow()
    shrink()
    grow()
    
def start():
    global ps
    pa = Polygon([(x, y) for x, y
                 in product(range(-200, 201, 100),
                            repeat=2)]).buffer(1)
    pb = Polygon([(-x, -y) for x, y
                 in product(range(-200, 201, 100),
                            repeat=2)]).buffer(1)
    ps = [pa.union(pb)]
    
def draw():
    py5.background(0, 0, 150)
    py5.translate(py5.width / 2, py5.height / 2)
    for i, p in enumerate(ps):
        py5.no_fill()
        py5.stroke(py5.color(255) if i % 2
                   else py5.color(0))
        py5.shape(py5.convert_cached_shape(p))
   
def shrink():
    p = ps[-1]
    new_p = p.buffer(-B, cap_style='round')
    print(new_p.area)
    while new_p.area > 0:
        ps.append(new_p)
        new_p = ps[-1].buffer(-B, cap_style='round')

def grow():
    p = ps[-1]
    new_p = p.buffer(B, cap_style='round')
    print(new_p.area)
    while new_p.area < 1000000:
        ps.append(new_p)
        new_p = ps[-1].buffer(B, cap_style='round')

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