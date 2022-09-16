from itertools import product, permutations

W = 40 # Width base-value for configs
EL_COLOR = 0
GRID_COLOR = 255
SCALE = 1

def setup():
    size(1540 * SCALE, 700 * SCALE)
    scale(SCALE)
    stroke_join(ROUND)
    no_stroke()
    # 16 grid positions
    elements = list(product((-1.5, -0.5, 0.5, 1.5), repeat=2))  
    # permutations (order counts)
    configs = list(permutations(elements, 2))
    print(f'Configurations: {len(configs)}')
    
    x = y = W * 2
    for config in configs:
        no_stroke()
        fill(GRID_COLOR)
        for xo, yo in elements:
            circle(x + xo * W / 3,
                   y + yo * W / 3,
                   W / 8)
        fill(EL_COLOR)
        xo, yo = config[0]
        circle(x + xo * W / 3,
               y + yo * W / 3,
               W / 8)
        stroke_weight(W / 24)
        stroke(EL_COLOR)
        (xa, ya), (xb, yb) = config
        arrow(x + xa * W / 3, y + ya * W / 3,
             x + xb * W / 3, y + yb * W / 3,
             head_size=W / 6)
        
        x += W * 1.5
        if x > width / SCALE - W * 1.5:
            x = W * 2
            y +=  W * 1.5

        save_frame('sketch_2022_09_16.png')


def arrow(xo, yo, xh, yh, head_size=5):
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
            