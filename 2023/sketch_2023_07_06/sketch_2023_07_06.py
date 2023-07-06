from itertools import product
from random import choice, sample, seed
import py5
from inputs import InputInterface


s = 1
w = 100

colors = (
    py5.color(0),
    py5.color(150,0, 0),
    py5.color(255)
    )
    
def key_pressed():
    inputs.key_pressed()
    
def key_released():
    inputs.key_released()

def setup():
    global inputs
    py5.size(1200, 600)
    inputs = InputInterface()

def draw():
    py5.background(0)
    global a1, a2, a3, a4
    a1 = int(inputs.analog_read(1) / 100)
    a2 = int(inputs.analog_read(2) / 2)
    a3 = int(inputs.analog_read(3))
    a4 = int(inputs.analog_read(4))
    seed(a1)
    w = a2 + 3
    rx = (1 + py5.sin(py5.frame_count / (1 + a3 / 10))) / 2
    ry = (1 + py5.cos(py5.frame_count / (1 + a3 / 10))) / 2
    x = y = 0
    while True:
        colors3 = sample(colors, 3)
        n = choice((3, 4, 5, 6, 7))
        rai, rbi = sample((w / 2, w, w * 2), 2)
        raf, rbf = sample((w / 2, w, w * 2), 2)
        ra = py5.lerp(rai / 5, raf / 5, rx)
        rb = py5.lerp(rbi / 5, rbf / 5, ry)
        draw_combo(x, y, w, n, colors3, ra, rb)
        x += w
        if x >= py5.width:
            x = 0
            y += w
        if y > py5.height:
            break

    inputs.update(display=False)


def draw_combo(x, y, w, n, colors3, ra, rb):
    a, b, c = colors3
    with py5.push_matrix():
        if rb < ra:
            ra, rb = rb, ra
        py5.translate(x, y)
        py5.fill(a)
        py5.rect(0, 0, w, w)
        py5.no_stroke()
        py5.fill(b)
        star(w / 2, w / 2, ra, rb, n * choice((1, 2)))
        py5.fill(c)
        star(w / 2, w / 2, rb, ra, n := n * choice((1, 2)),
             py5.PI / n * choice((0, 1)))


def star(x, y, radius_a, radius_b, n_points, rot=0):
    step = py5.TWO_PI / n_points
    py5.begin_shape()
    for i in range(n_points + 1):
        ang = i * step + rot
        sx = py5.cos(ang) * radius_a
        sy = py5.sin(ang) * radius_a
        cx = py5.cos(ang + step / 2.) * radius_b
        cy = py5.sin(ang + step / 2.) * radius_b
        if i == 0:
            py5.vertex(x + cx, y + cy)
        else:
            py5.quadratic_vertex(x + sx, y + sy, x + cx, y + cy)
    py5.end_shape()

    
def make_stars(s):
    py5.random_seed(s)
    return [(150 + py5.random_int(6) * 50, x, y) for i, (x, y)
                 in enumerate(product(range(150, 451, 50), repeat=2))]

def get_colors(s):
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

    def __call__(self, *args):
        rb = self.func(self.ns, *args)
        if self.t > 0.99:
            return rb
        ra = self.func(self.s, *args)
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
    if py5.key == 'p':
       py5.save_frame(f'{py5.frame_count}.png')
    elif str(py5.key) in '0123':
        angles.update_s(py5.key)

    inputs.key_pressed()
    
def key_released():
    inputs.key_released()


py5.run_sketch()

