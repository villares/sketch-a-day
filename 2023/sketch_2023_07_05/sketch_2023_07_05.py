from itertools import product
import py5

def setup():
    global boxes, angles
    py5.size(600, 600, py5.P3D)
    boxes = LState(make_boxes, 'boxes')
    angles = LState(get_angles)

def draw():
    py5.background(0)
    py5.ortho()   
    rx, ry = angles()    
    
    py5.translate(py5.width / 2, py5.height / 2, -py5.height / 2)
    py5.rotate_y(ry)
    py5.rotate_x(rx)
    py5.translate(-py5.width / 2, -py5.height / 2,  -py5.height / 2)
    
    for b in boxes():
        xyzbox(*b)
    ms = py5.mouse_x // 20
    LState.update((boxes, ms))  # updates "global t" and boxes.update(ms)
        
def xyzbox(x, y, z, w=50):
    with py5.push_matrix():
        py5.stroke(255)
        py5.fill(x / 2 - 50, y / 2 - 50, z / 2 - 50)
        py5.translate(x , y, z)
        py5.box(w)
    
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

class LState:
    """Lerpable State Objects"""
    ls_objects = {}
    
    def __init__(self, func, name=None, first_seed=0):
        self.func = func
        self.name = name or len(self.ls_objects)
        self.s = self.ns = first_seed
        self.t = 0        
        self.ls_objects[self.name] = self

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
    def update(cls, *args, **kwargs):
        for g in cls.ls_objects.values():
            g.t = py5.lerp(g.t, 1, 0.1)
        for obj, v in args:
            obj.update_s(v)
        for k, v in kwargs.items():
            cls.ls_objects[k].update_s(v)

# LState class depends on this
def lerp_tuple(a, b, t):   
    return tuple(lerp_tuple(ca, cb, t) if isinstance(ca, tuple)
             else py5.lerp(ca, cb, t)             
             for ca, cb in zip(a, b))

def key_pressed():
    if py5.key == 's':
       py5.save_frame(f'{py5.frame_count}.png')
    elif str(py5.key) in '0123':
        angles.update_s(py5.key)

py5.run_sketch()

