from itertools import product

w = 48

def setup(): 
    size(852, 852)
    background(150, 150, 200)
    no_stroke()
    elements = product((-0.5, 0.5), repeat=2)  # 4 grid positions
    on_offs = (((el, 0), (el, 85), (el, 170), (el, 255)) for el in elements)
    combos = list(product(*on_offs))
    print(f'Combinations: {len(combos)}')
    x = y = w
    translate(w / 3, w / 3)
    for combo in combos:
        for (xo, yo), state in combo:
            fill(state)
            square(x + xo * w / 3,
                   y + yo * w / 3,
                   w / 3)
        x += w 
        if x > width - w:
            x = w
            y +=  w 

