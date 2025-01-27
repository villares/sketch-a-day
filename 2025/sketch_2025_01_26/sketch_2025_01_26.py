from shapely import Polygon
import py5

def setup():
    py5.size(600, 600)
    start()
    
def start():
    global ps
    crossing = True
    while crossing:
        pts_a = [(py5.random_int(1, 20) * 10,
                  py5.random_int(1, 20) * 10) 
                  for _ in range(5)]
        pts_b = [(y, -x) for x, y in pts_a]
        pts = pts_a + pts_b
        p = Polygon(pts)
        p_mirror = Polygon([(-x, y) for x, y in pts])
        p_mirror = p_mirror.union(p)
        crossing = not p_mirror.is_simple
    ps = [p_mirror]
    
def draw():
    py5.background(230, 240, 240)
    py5.translate(py5.width / 2, py5.height / 2)
    py5.no_fill()
    for p in ps:
        py5.shape(py5.convert_cached_shape(p))
   
def shrink():
    p = ps[-1]
    new_p = p.buffer(-10, cap_style='round')
    print(new_p.area)
    while new_p.area > 0:
        ps.append(new_p)
        new_p = ps[-1].buffer(-10, cap_style='round')

def grow():
    p = ps[-1]
    new_p = p.buffer(10, cap_style='round')
    print(new_p.area)
    while new_p.area < 1000000:
        ps.append(new_p)
        new_p = ps[-1].buffer(10, cap_style='round')


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