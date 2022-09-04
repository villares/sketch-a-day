from itertools import permutations, combinations, product

def setup():
    size(1160, 880)
    translate(40, 20)
    no_stroke()
    rect_mode(CENTER)
    w = 15
    th = w * sqrt(3) / 2
    shapes = {
        't': lambda: triangle(x - w / 2, y + th / 2,
                              x + w / 2, y + th / 2,
                              x, y - th / 2),
        's': lambda: square(x, y, w * 0.85),
        'c': lambda: circle(x, y, w)
        }
    color_mode(HSB)
    colors = [color(16 + i * 64, 255, 150) for i in range(3)]
    prods = list(product('tsc', colors))
    
    x = y = w
    permts = list(permutations(prods, 3))
    print(f'Permutations: {len(permts)}')
    for p in permts:
        for s, c in p:
            fill(c)
            shapes[s]()
            x += w
        x += w
        if x > width - 5 * w:
            x = w
            y += 2 * w
