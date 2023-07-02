from itertools import product

import py5


s = 0 # random seed

def setup():
    py5.size(500, 500, py5.P3D)
    
def draw():
    py5.background(0)
    py5.ortho()
    py5.random_seed(s)    
    boxes_pos = [(x, y, py5.random_int(9) * 50) for i, (x, y)
                 in enumerate(product(range(50, 451, 50), repeat=2))]
    py5.translate(py5.width / 2, py5.height / 2, -py5.height / 2)
    py5.rotate_y(py5.mouse_x / 10)
    py5.rotate_x(py5.mouse_y / 10)
    py5.translate(-py5.width / 2, -py5.height / 2)
    for p in boxes_pos:
        xyzbox(*p)
        
def xyzbox(x, y, z, w=50):
    with py5.push_matrix():
         py5.translate(x , y, z)
         py5.box(w)

def key_pressed():
    global s
    py5.save_frame(f'{s}.png')
    s += 1

py5.run_sketch()


