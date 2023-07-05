from itertools import product
import py5

s = ns = 0 # random seed
rx = ry = tx = ty = ntx = nty = 0.02
t = 1

def setup():
    global boxes, angles
    py5.size(600, 600, py5.P3D)
    boxes = SGenerator(0, make_boxes)
    angles = SGenerator(0, get_angles)


def draw():
    py5.background(0)
    #py5.ortho()   
    rx, ry = angles()    
    
    py5.translate(py5.width / 2, py5.height / 2, -py5.height / 2)
    py5.rotate_y(ry)
    py5.rotate_x(rx)
    py5.translate(-py5.width / 2, -py5.height / 2,  -py5.height / 2)
    
    for b in boxes():
        xyzbox(*b)

    SGenerator.update_t()
    ms = py5.mouse_x // 20
    boxes.update_s(ms)
        
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

def get_angles(s):
    angles_dict = {
        '1': (py5.HALF_PI + 0.3, py5.HALF_PI + 0.3),
        '2': (py5.PI, 0),
        }
    return angles_dict.get(s, (0, 0))


class SGenerator:
    generators = []
    
    def __init__(self, first_seed, func):
        self.func = func
        self.s = self.ns = first_seed
        self.t = 0        
        SGenerator.generators.append(self)

    def __call__(self):
        rb = self.func(self.ns)
        if self.t > 0.99:
            return rb
        ra = self.func(self.s)
        return lerp_tuple(ra, rb, self.t)
               
    def update_s(self, us):
        if self.t > 0.99 and us != self.ns:
            self.s = self.ns
            self.ns = us
            self.t = 0
       
    @classmethod
    def update_t(cls):
        for g in cls.generators:
            g.t = py5.lerp(g.t, 1, 0.1)

def key_pressed():
    if py5.key == 's':
       py5.save_frame(f'{py5.frame_count}.png')
    elif str(py5.key) in '0123':
        angles.update_s(py5.key)

py5.run_sketch()

