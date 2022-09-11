from itertools import product

w = 6

def setup(): 
    size(243 * 7 + 1, 81 * 7 + 1)
    no_smooth()
    rect_mode(CENTER)
    background(0)
    no_stroke()
    elements = product((-1, 0, 1), repeat=2)  # 4 grid positions
    on_offs = (((el, color(200, 0, 0)),
                (el, color(0, 200, 0)),
                (el, color(0, 0, 200))) for el in elements)
    combos = sorted(product(*on_offs), key=how_red)
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

def how_red(combo):
    return sum(red(c) * 10 + blue(c) for pos, c in combo)
        
    