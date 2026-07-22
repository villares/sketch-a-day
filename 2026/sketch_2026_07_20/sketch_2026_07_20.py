# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org

# zoom & pan transformation values
zpt = {'x': 0, 'y': 0, 'scale': 1, 'amount': 0}  

cores_a = (
    '#fec31c',
    '#f15628',
    '#d1212b',
    )
cores_b = (
    '#21a5a8',
    '#1f79ac',
    '#174a92',
    )
cores_t = cores_a + cores_b

import py5
from functools import cache

tilt = 0
modo = 0

@cache
def f(x, y):
    return (y % 9 * y & x ^ y) % 6

def setup():
    global out
    py5.size(960, 540, py5.P3D)
    py5.no_smooth()
    py5.no_cursor()
    #py5.no_stroke()
#    out = py5.create_graphics(1920, 1080, py5.P3D)
#     py5.launch_repeating_thread(
#         saver, name='saver', time_delay=0.1)

def draw():
    
    py5.ortho()
    #py5.lights()
    py5.background('black')
    with py5.push_matrix():
        py5.translate(zpt['x'], zpt['y'])
        py5.scale(zpt['scale'])
        py5.stroke_weight(1 / zpt['scale'])
        py5.stroke('gray')
        py5.translate(py5.width * 0.45, py5.height * 0.3, -350)
        py5.rotate_x(py5.radians(tilt)) #py5.mouse_y))
        py5.rotate_z(py5.radians(tilt))
        py5.translate(-py5.width / 2, -py5.height / 2)    
        #py5.color_mode(py5.CMAP, 'viridis', 255)
        #py5.background(0)
        n = 8
        w =  int(py5.width / n)
        for x in range(w):
            for y in range(w):
                r = f(x, y)
                if modo == 0:
                    py5.fill(py5.color(cores_t[r]))
                if modo == 1:
                    t = py5.remap(py5.mouse_y,
                                  0, py5.height, 0, 1)
                    a = py5.color(cores_a[r % 3])
                    b = py5.color(cores_b[r % 3])
                    cor = py5.lerp_color(a, b, t)
                    py5.fill(cor)
                if modo == 2:
                    t = py5.remap(py5.mouse_y,
                                  0, py5.height, 0, 1)
                    if r < 3:
                        a = py5.color(cores_a[r % 3])
                        b = py5.color(cores_b[r % 3])
                        cor = py5.lerp_color(a, b, t)
                    else:
                        cor = py5.color(cores_t[r])
                    py5.fill(cor)
                box(x * n, y * n, n * (r + 1) / 3, n, n, n / 2)

def box(x, y, z, w, h=None, d=None):
    h = h or w
    d = d or h
    with py5.push_matrix():
        py5.translate(x, y, z)
        py5.box(w, h, d)

def key_pressed():
    global tilt, modo

    if py5.key == 'a':
        tilt += 5
    if py5.key == 'z':
        tilt -= 5
    if py5.key == 'm':
        modo = (modo + 1) % 3
    if py5.key == 'p':
        py5.save_frame('####.png')


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