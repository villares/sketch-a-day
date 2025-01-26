from shapely import Polygon
import py5

def setup():
    py5.size(600, 600)
    start()
    
def start():
    global ps
    pts = [(py5.random_int(10, 50) * 10,
            py5.random_int(10, 50) * 10) 
            for _ in range(10)]
    ps = [Polygon(pts)]
    
def draw():
    py5.background(230, 240, 240)
    py5.no_fill()
    for p in ps:
        py5.shape(py5.convert_cached_shape(p))
   
def key_pressed():
    global p
    if py5.key in ('+', '='):
        ps.append(ps[-1].buffer(10, cap_style='round'))
    elif py5.key == '-':
        ps.append(ps[-1].buffer(-10, cap_style='round'))
    elif py5.key == 's':
        py5.save_frame('out###.png')
    elif py5.key == ' ':
        start()
py5.run_sketch()