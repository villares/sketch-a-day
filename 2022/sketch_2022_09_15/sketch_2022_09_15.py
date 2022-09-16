from itertools import product, combinations

W = 40 # Width base-value for configs
EL_COLOR = 255
GRID_COLOR = 0
SCALE = 1

def setup():
    size(820 * SCALE, 700 * SCALE)
    scale(SCALE)
    no_stroke()
    # 16 grid positions
    elements = list(product((-1.5, -0.5, 0.5, 1.5), repeat=2))  
    # combinations (membership only counts, not order)
    combos = list(combinations(elements, 2))
    print(f'Configurations: {len(combos)}')
    
    x = y = W * 2
    for config in combos:
        no_stroke()
        fill(GRID_COLOR)
        for xo, yo in elements:
            circle(x + xo * W / 3,
                   y + yo * W / 3,
                   W / 12)
        fill(EL_COLOR)
        for xo, yo in config:
            circle(x + xo * W / 3,
                   y + yo * W / 3,
                   W / 6)
        stroke_weight(W / 10)
        stroke(EL_COLOR)
        (xa, ya), (xb, yb) = config
        line(x + xa * W / 3, y + ya * W / 3,
             x + xb * W / 3, y + yb * W / 3)
        
        x += W * 1.5
        if x > width / SCALE - W * 1.5:
            x = W * 2
            y +=  W * 1.5

        save_frame('sketch_2022_09_15.png')