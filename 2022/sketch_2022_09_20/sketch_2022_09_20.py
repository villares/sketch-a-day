"""
Combinations of 2 arrows on a 2x3 grid, so that the arrows don't share
starting or ending points: 180
"""
from itertools import product, permutations, combinations

W = 30 # Width base-value for configs
EL_COLOR = 0
GRID_COLOR = 255
SCALE = 5

def setup():
    size(1035 * SCALE, 980 * SCALE, P2D)
    scale(SCALE)
    stroke_cap(ROUND)
    no_fill()
    d60, r = radians(60), 1.5
    positions = [(r * cos(i * d60), r * sin(i * d60)) for i in range(6)]
    arrows = permutations(positions, 2)        # permutations (order counts)
    arrow_combos = combinations(arrows, 2)           # arrow pairs, no matter order 
    configs = [(a, b) for a, b in arrow_combos       # pick arrows that...
               if set(a) != set(b)]     # ...don't have both ends in common

    print(f'Configurations: {len(configs)}')
    i = 1
    x = y = W * 2
    w = W / 3
    for arrows in configs:
        stroke(GRID_COLOR)
        stroke_weight(w / 4)
        push_matrix()
        translate(x, y)
        points([(xo * w, yo * w) for xo, yo in positions])
        stroke_weight(w / 12)
        stroke(EL_COLOR)
        for arrow in arrows:
            (xa, ya), (xb, yb) = arrow
            draw_arrow(xa * w, ya * w,
                       xb * w, yb * w,
                       head_size=w/4,
                       shorten=int(w/2.5)
                       )
        pop_matrix()
        x += W * 1.5
        if x > width / SCALE - W * 1.5:
            #print(i)  # debug
            x = W * 2
            y +=  W * 1.5
        i += 1
    save_frame('sketch_2022_09_20.png')

def draw_arrow(xo, yo, xh, yh, head_size=5, shorten=0):
    """
    If shorten < 1, shortens a fraction of the body length,
    otherwise shorten itself is used as the length to shorten.
    """
    dx, dy = xo - xh, yo - yh
    ang = atan2(dy, dx) + PI
    body = sqrt(dx * dx + dy * dy)
    head_size = min(head_size, body / 2)
    if 0 < shorten < 1:
        to, th = shorten / 2, 1 - shorten / 2
        nxo, nyo = lerp(xo, xh, to), lerp(yo, yh, to)
        nxh, nyh = lerp(xo, xh, th), lerp(yo, yh, th)
        xo, yo, xh, yh = nxo, nyo, nxh, nyh
    else:
        nxo = xo + cos(ang) * shorten / 2
        nyo = yo + sin(ang) * shorten / 2
        nxh = xh + cos(ang) * -shorten / 2
        nyh = yh + sin(ang) * -shorten / 2
        xo, yo, xh, yh = nxo, nyo, nxh, nyh
    xha = xh + cos(ang + HALF_PI / 3 + PI) * head_size
    yha = yh + sin(ang + HALF_PI / 3 + PI) * head_size
    xhb = xh + cos(ang - HALF_PI / 3 + PI) * head_size
    yhb = yh + sin(ang - HALF_PI / 3 + PI) * head_size
    line(xo, yo, xh, yh)
    
    with begin_shape():
        vertex(xha, yha)
        vertex(xh, yh)
        vertex(xhb, yhb)        
            