from itertools import product

w = 20 # width base-value for 

def setup():
    size(990, 500)
    no_stroke()
    
    elements = product((-1, 0, 1), repeat=2)  # 9 grid positions
    on_offs = (((el, True), (el, False)) for el in elements)
    configs = list(product(*on_offs))
    print(f'Configurations: {len(configs)}')
    
    x = y = w
    translate(w / 2, w / 4)
    for config in configs:
        for (xo, yo), state in config:
            fill(state * 255)
            circle(x + xo * w / 3,
                   y + yo * w / 3,
                   w / 3)
        x += w * 1.5
        if x > width - w * 1.5:
            x = w
            y +=  w * 1.5

