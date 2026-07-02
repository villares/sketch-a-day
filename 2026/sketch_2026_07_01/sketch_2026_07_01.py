# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org

"""
inspired by https://freeradical.zone/@bitartbot/116696573113492478
f(x,y) = ((((y % 9) * (~y)) & (-(x & x))) ^ (~((-y) ^ (-y)))) % 6
Continued from sketch_2026_06_07
"""
import py5

def f(x, y):
    return (y % 9 * y & x ^ y) % 6

def setup():
    py5.size(800, 800, py5.P3D)
    py5.no_smooth()
    #py5.no_stroke()
    
def draw():
    py5.background(0)
    py5.stroke('gray')
    py5.translate(py5.width / 2, py5.height / 2, 200)
    py5.rotate_x(py5.radians(15))
    py5.translate(-py5.width / 2, -py5.height / 2)    
    py5.color_mode(py5.CMAP, 'magma', 255)
    #py5.background(0)
    n = 8
    w =  int(py5.width / n) 
    for x in range(w):
        for y in range(w):
            r = f(x, y) 
            py5.fill((r % 5) * (255/4))
            box(x * n, y * n, r * n, n)

def box(x, y, z, w, h=None, d=None):
    h = h or w
    d = d or h
    with py5.push_matrix():
        py5.translate(x, y, z)
        py5.box(w, h, d)

def key_pressed():
    py5.save_frame(f'out###-{py5.millis()}.png')


py5.run_sketch(block=False)