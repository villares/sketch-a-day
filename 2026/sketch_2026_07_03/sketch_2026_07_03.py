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
    global debug
    #py5.ortho()
    py5.background(0)
    py5.stroke('gray')
    py5.translate(py5.width * 0.45, py5.height * 0.34, 150)
    py5.rotate_x(py5.radians(30)) #py5.mouse_y))
    py5.rotate_z(py5.radians(30))

    py5.translate(-py5.width / 2, -py5.height / 2)    
    py5.color_mode(py5.CMAP, 'viridis_r', 255)
    #py5.background(0)
    n = 8
    w =  int(py5.width / n)
    debug = set()
    for x in range(w):
        for y in range(w):
            r = f(x, y)
            debug.add(r)
            py5.fill(r * (255 / 5))
            box(x * n, y * n, n * (r + 1) / 2, n, n, n * (r + 1))

def box(x, y, z, w, h=None, d=None):
    h = h or w
    d = d or h
    with py5.push_matrix():
        py5.translate(x, y, z)
        py5.box(w, h, d)

def key_pressed():
    print(debug)
    py5.save_frame(f'out###-{py5.millis()}.png')


py5.run_sketch(block=False)