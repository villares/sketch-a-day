from itertools import product

w = 20
th = w * sqrt(3) / 2    

def setup():
    size(990, 500)
    no_stroke()
    elements = product((-1, 0, 1), repeat=2)  # 9 grid positions
    on_offs = (((el, True), (el, False)) for el in elements)
    combos = list(product(*on_offs))
    print(f'Combinations: {len(combos)}')
    x = y = w
    translate(w / 2, w / 4)
    for combo in combos:
        for (xo, yo), state in combo:
            fill(state * 255)
            circle(x + xo * w / 3,
                   y + yo * w / 3,
                   w / 3)
        x += w * 1.5
        if x > width - w * 1.5:
            x = w
            y +=  w * 1.5

