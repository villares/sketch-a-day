# based on https://twitter.com/uspinguim/status/1558050507721261056
try:
    from functools import cache
except ImportError:
    from functools import lru_cache as cache  # for python 3.8

a, b = 220, 60
du, dv = 12, 24

def setup():
    size(500, 500, P3D)
    color_mode(HSB)
    smooth()

def draw():
    lights()
    background(0)
    translate(width / 2, height / 2, -300)
    rotate_x(mouse_y / 100)
    rotate_y(mouse_x / 100)
    quads = toroid_quads(a, b, du, dv)
    fill(0, 0, 290)
    with begin_shape(QUADS):
        for i, q in enumerate(quads):
            fill(remap(i, 0, len(quads), 0 , 255), 200, 200)
            vertices(q)

@cache
def toroid_quads(a, b, du, dv):
    u_step = TWO_PI / du
    v_step = TWO_PI / dv
    pts = []
    v = 0
    sin_v, cos_v = sin(v), cos(v)
    for _ in range(dv):
        sin_next_v, cos_next_v = sin(v + v_step), cos(v + v_step)
        u = 0
        sin_u, cos_u = sin(u), cos(u)
        for _ in range(du):
            sin_next_u, cos_next_u = sin(u + u_step), cos(u + u_step)
            x00 = (a + b * cos_u) * sin_v
            y00 = (a + b * cos_u) * cos_v
            z00 = b * sin_u
            x01 = (a + b * cos_u) * sin_next_v
            y01 = (a + b * cos_u) * cos_next_v
            z01 = z00            
            x11 = (a + b * cos_next_u) * sin_next_v
            y11 = (a + b * cos_next_u) * cos_next_v
            z11 = b * sin_next_u
            x10 = (a + b * cos_next_u) * sin_v
            y10 = (a + b * cos_next_u) * cos_v
            z10 = z11
            pts.append((
                (x00, y00, z00),
                (x01, y01, z01),
                (x11, y11, z11),
                (x10, y10, z10),               
               ))
            sin_u, cos_u = sin_next_u, cos_next_u
            u += u_step
        sin_v, cos_v = sin_next_v, cos_next_v
        v += v_step
    return pts

def key_pressed():
    global a, b, du, dv
    if key == CODED:
        if key_code == LEFT: du -= 1 if du > 3 else 0
        elif key_code == RIGHT: du += 1
        elif key_code == DOWN: dv -= 1 if dv > 3 else 0
        elif key_code == UP: dv += 1
    elif key == 'a': a -= 5
    elif key == 'd': a += 5
    elif key == 's': b -= 5
    elif key == 'w': b += 5             
             
        
    
    
    