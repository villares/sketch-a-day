from itertools import product
import py5

s = ns = 0 # random seed
rx = ry = tx = ty = ntx = nty = 0.02
t = 1

def setup():
    py5.size(600, 600, py5.P3D)
    
def draw():
    global s, ns, t, tx, ty

    py5.background(0)
    #py5.ortho()
    boxes_a = make_boxes(s)
    boxes_b = make_boxes(ns)

    rx = py5.lerp(tx, ntx, t)    
    ry = py5.lerp(ty, nty, t)    
    
    py5.translate(py5.width / 2, py5.height / 2, -py5.height / 2)
    py5.rotate_y(ry)
    py5.rotate_x(rx)
    py5.translate(-py5.width / 2, -py5.height / 2,  -py5.height / 2)
    for pa, pb in zip(boxes_a, boxes_b):
        xyzbox(*lerp_tuple(pa, pb, t))

    t = py5.lerp(t, 1, 0.1)

    ms = py5.mouse_x // 20
    if t > 0.99 and ms != ns:
        s = ns
        ns = ms
        t = 0
        tx, ty = ntx, nty # avoid rotation change

        
def xyzbox(x, y, z, w=50):
    with py5.push_matrix():
        py5.stroke(255)
        py5.fill(x / 2 - 50, y / 2 - 50, z / 2 - 50)
        py5.translate(x , y, z)
        py5.box(w)

def lerp_tuple(a, b, t):   
    return tuple(lerp_tuple(ca, cb, t) if isinstance(ca, tuple)
                 else py5.lerp(ca, cb, t)             
                 for ca, cb in zip(a, b))
    
def make_boxes(s):
    py5.random_seed(s)
    return [(150 + py5.random_int(6) * 50, x, y) for i, (x, y)
                 in enumerate(product(range(150, 451, 50), repeat=2))]

# class SGenerator:
#     t = 0
#     generators = []
#     
#     def __init__(self, first_seed, func):
#         self.s = self.ns = first_seed
#         
#         SGenerator.generators.append(self)
        
def key_pressed():
    global s, ns, tx, ty, ntx, nty, t
    t = 0
    if py5.key == 's':
       # py5.save_frame(f'{s}.png')
        s = ns
        ns += 1
        tx, ty = ntx, nty
    elif py5.key == '1':
        tx, ty = ntx, nty
        ntx =  nty = py5.HALF_PI + 0.3
        
    elif py5.key == '2':
        tx, ty = ntx, nty
        ntx = nty = 0
    elif py5.key == '3':
        tx, ty = ntx, nty
        nty, ntx = py5.PI, 0

py5.run_sketch()

