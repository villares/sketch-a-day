try:
    from functools import cache
except ImportError:
    from functools import lru_cache as cache  # for python 3.8
# based on https://twitter.com/uspinguim/status/1558050507721261056

a, b = 220, 60
du, dv = 36, 72

def setup():
    size(500, 500, P3D)
    stroke_weight(3)    

def draw():
    background(200)
    translate(width / 2, height / 2, -300)
    rotate_x(QUARTER_PI)
    tpts = toroid_points(a, b, du, dv)
    points(tpts)

@cache
def toroid_points(a, b, du, dv):
    u_step = TWO_PI / du
    v_step = TWO_PI / dv
    pts = []
    v = 0
    while v < TWO_PI:
        u = 0
        while u < TWO_PI:
            x = (a + b * cos(u)) * sin(v)
            y = (a + b * cos(u)) * cos(v)
            z = b * sin(u)
            pts.append((x, y, z))
            u += u_step
        v += v_step
    return pts

def key_pressed():
    global a, b, du, dv
    if key == CODED:
        if key_code == LEFT: du -= 1 if du > 1 else 0
        elif key_code == RIGHT: du += 1
        elif key_code == DOWN: dv -= 1 if dv > 1 else 0
        elif key_code == UP: dv += 1
    elif key == 'a': a -= 5
    elif key == 'd': a += 5
    elif key == 's': b -= 5
    elif key == 'w': b += 5             
             
        
    
    
    