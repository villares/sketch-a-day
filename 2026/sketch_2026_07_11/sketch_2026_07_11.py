# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org

# zoom & pan transformation values
zpt = {'x': 100, 'y': -50, 'scale': 1, 'amount': 0}  

import py5
from functools import cache

tilt = 60
w = 8
a = 23
b = 23
c = 9

@cache
def f(x, y):
    return (((y % a) * b) & (x & y)) % c

def setup():
    py5.size(800, 800, py5.P3D)
    py5.no_smooth()
    py5.color_mode(py5.CMAP, 'plasma', 255)
    #py5.no_cursor()
    
def draw():
    py5.ortho()
    #py5.lights()
    py5.background('black')
    with py5.push_matrix():
        py5.translate(zpt['x'], zpt['y'])
        py5.scale(zpt['scale'])
        py5.stroke_weight(1 / zpt['scale'])
        #py5.stroke('gray')
        py5.translate(py5.width * 0.45, py5.height * 0.3, -350)
        py5.rotate_x(py5.radians(tilt)) #py5.mouse_y))
        py5.rotate_z(py5.radians(tilt))
        py5.translate(-py5.width / 2, -py5.height / 2)    
        #py5.background(0)
        n =  int(py5.width / w) * 2
        for x in range(n):
            for y in range(n):
                r = f(x, y)
                py5.fill(r * (255 / (c-1)))
                box(x * w, y * w, w * (r + 1), w, w, w)

def box(x, y, z, w, h=None, d=None):
    h = h or w
    d = d or h
    with py5.push_matrix():
        py5.translate(x, y, z)
        py5.box(w, h, d)

def key_pressed():
    global tilt
    if py5.key == 's':
        py5.save_frame(f'out###-{py5.millis()}.png')
    elif py5.key == 'a':
        tilt += 5
    elif py5.key == 'z':
        tilt -= 5

def mouse_wheel(e):
    xrd = (py5.mouse_x - zpt['x']) / zpt['scale']
    yrd = (py5.mouse_y - zpt['y']) / zpt['scale']
    zpt['amount'] -= e.get_count()
    zpt['scale'] = 1.1 ** zpt['amount']
    zpt['x'] = int(py5.mouse_x - xrd * zpt['scale'])
    zpt['y'] = int(py5.mouse_y - yrd * zpt['scale'])

def mouse_dragged():
    zpt['x'] += py5.mouse_x - py5.pmouse_x
    zpt['y'] += py5.mouse_y - py5.pmouse_y


py5.run_sketch(block=False)