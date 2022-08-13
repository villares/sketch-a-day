# based on https://twitter.com/uspinguim/status/1558050507721261056
from functools import cache

a, b = 220, 60
du, dv = 12, 24

def setup():
    size(500, 500, P3D)

def draw():
    lights()
    background(200)
    translate(width / 2, height / 2, -300)
    rotate_x(mouse_y / 100)
    rotate_y(mouse_x / 100)
    quads = toroid_quads(a, b, du, dv)
    with begin_shape(QUADS):
        vertices(quads)

@cache
def toroid_quads(a, b, du, dv):
    u_step = TWO_PI / du
    v_step = TWO_PI / dv
    pts = []
    v = 0
    while v < TWO_PI:
        u = 0
        while u < TWO_PI:
            x00 = (a + b * cos(u)) * sin(v)
            y00 = (a + b * cos(u)) * cos(v)
            z00 = b * sin(u)
            x01 = (a + b * cos(u)) * sin(v + v_step)
            y01 = (a + b * cos(u)) * cos(v + v_step)
            z01 = z00            
            x11 = (a + b * cos(u + u_step)) * sin(v + v_step)
            y11 = (a + b * cos(u + u_step)) * cos(v + v_step)
            z11 = b * sin(u + u_step)
            x10 = (a + b * cos(u + u_step)) * sin(v)
            y10 = (a + b * cos(u + u_step)) * cos(v)
            z10 = z11
            pts.extend((
                (x00, y00, z00),
                (x01, y01, z01),
                 (x11, y11, z11),
                 (x10, y10, z10),               
                ))
            u += u_step
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
             
        
    
    
    