from itertools import product

import py5

s = 17 # random seed
rx = ry = tx = ty = 0

def setup():
    py5.size(600, 600, py5.P3D)
    
def draw():
    global rx, ry
    py5.background(0)
    py5.ortho()
    py5.random_seed(s)
    boxes_pos = []
    zy = []
    zx = []
    for x, y in product(range(150, 451, 100), repeat=2):
        z = None
        while z is None or (z, x) in zx or (z, y) in zy:
            z = 150 + py5.random_int(3) * 100
        boxes_pos.append((x, y, z))
        zy.append((z, y))
        zx.append((z, x))
        
    py5.translate(py5.width / 2, py5.height / 2, -py5.height / 2)
    py5.rotate_y(ry)
    py5.rotate_x(rx)
    py5.translate(-py5.width / 2, -py5.height / 2,  -py5.height / 2)
    for p in boxes_pos:
        xyzbox(*p)

    rx = py5.lerp(rx, tx, 0.1)    
    ry = py5.lerp(ry, ty, 0.1)    
    
        
def xyzbox(x, y, z, w=100):
    with py5.push_matrix():
        py5.stroke(255)
        py5.fill(x / 2 - 50, y / 2 - 50, z / 2 - 50)
        py5.translate(x , y, z)
        py5.box(w)

def mouse_dragged():
    global tx, ty
    ty += py5.radians(py5.mouse_x - py5.pmouse_x)
    tx += py5.radians(py5.mouse_y - py5.pmouse_y)

def key_pressed():
    global s, tx, ty
    if py5.key == 's':
        py5.save_frame(f'{s}.png')
        s += 1
    elif py5.key == '1':
        tx = ty = py5.HALF_PI
    elif py5.key == '2':
        tx = ty = 0
    elif py5.key == '3':
        ty = py5.HALF_PI
        tx = 0
    elif py5.key == '4':
        ty = 0
        tx = py5.QUARTER_PI


py5.run_sketch()