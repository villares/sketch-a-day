from itertools import product

w = 6

def setup(): 
    size(243 * 7 + 1, 81 * 7 + 1)
    no_smooth()
    rect_mode(CENTER)
    background(0)
    no_stroke()
    positions = product((-1, 0, 1), repeat=2)  # 9 grid positions
    options_per_position = (((pos, color(200, 0, 0)),
                             (pos, color(0, 200, 0)),
                             (pos, color(0, 0, 200))) for pos in positions)
    combos = sorted(product(*options_per_position))
    print(f'Combinations: {len(combos)}')
    translate(1, 1)
    x = y = w / 2
    for combo in combos:
        for (xo, yo), state in combo:
            fill(state)
            square(x + xo * w / 3,
                   y + yo * w / 3,
                   w / 3)
        x += w + 1
        if x > width:
            x = w / 2
            y +=  w + 1
    save_frame('out.png')
