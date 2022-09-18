"""
Combinations of 2 arrows on a 3x3 grid, so that the arrows don't share starting or ending points: 1512
"""
from itertools import product, permutations, combinations

W = 20 # Width base-value for configs
EL_COLOR = 0
GRID_COLOR = 255
SCALE = 2

def setup():
    size(1670 * SCALE, 900 * SCALE)
    scale(SCALE)
    stroke_join(ROUND)
    no_stroke()

    positions = list(product((-1, 0, 1), repeat=2))  # 9 positions on a grid
    arrows = list(permutations(positions, 2))        # permutations (order counts)
    configs = list(combinations(arrows, 2))          # arrow pairs, no matter order 
    configs = [(a, b) for a, b in configs            # filter out arrows that...
               if len(set(a) | set(b)) == 4]         # ...have points in common

#     # wrong, this duplicates configs by picking the same 2 arrows in 2 ways
#     arrows = list(permutations(positions, 4))
#     configs = [((a, b), (c, d)) for a, b, c, d in arrows]
  
    print(f'Configurations: {len(configs)}')
    i = 1
    x = y = W * 2
    w = W / 3
    for arrows in configs:
        stroke(GRID_COLOR)
        stroke_weight(w / 3)
        push_matrix()
        translate(x, y)
        points([(xo * w, yo * w) for xo, yo in positions])
        stroke_weight(w/8)
        stroke(EL_COLOR)
        for arrow in arrows:
            (xa, ya), (xb, yb) = arrow
            draw_arrow(xa * w, ya * w,
                       xb * w, yb * w,
                       head_size=w/3)
        pop_matrix()
        x += W * 1.5
        if x > width / SCALE - W * 2:
            #print(i)
            x = W * 2
            y +=  W * 1.5
        i += 1
        save_frame('sketch_2022_09_18b.png')

def draw_arrow(xo, yo, xh, yh, head_size=5):
    dx, dy = xo - xh, yo - yh 
    body = sqrt(dx * dx + dy * dy)
    head_size = min(head_size, body / 2)
    ang = atan2(dy, dx) + PI
    xha = xh + cos(ang + HALF_PI / 2 + PI) * head_size
    yha = yh + sin(ang + HALF_PI / 2 + PI) * head_size
    xhb = xh + cos(ang - HALF_PI / 2 + PI) * head_size
    yhb = yh + sin(ang - HALF_PI / 2 + PI) * head_size
    line(xo, yo, xh, yh)  # corpo com tamanho fixo
    line(xh, yh, xha, yha)
    line(xh, yh, xhb, yhb)         
            