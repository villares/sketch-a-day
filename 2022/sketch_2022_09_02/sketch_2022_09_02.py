from itertools import permutations, combinations, product

def setup():
    size(600, 200)
    fill(0, 100)
    no_stroke()
    w = 25
    shapes = {
        't': lambda: triangle(x, y, x + w, y, x, y + w),
        's': lambda: square(x, y, w),
        'c': lambda: circle(x + w / 2 , y + w / 2, w)
        }
    
    x =  50
    y = 25
    permts = permutations('tsc', 2)
    for a, b in permts:
        shapes[a]()
        x += 30
        shapes[b]()
        x += 55

    x = 200
    y = 75
    combos = combinations('tsc', 2)
    for a, b in combos:
        shapes[a]()
        shapes[b]()
        x += 100

    x = 24
    y = 125
    color_mode(HSB)
    colors = [color(i * 32, 200, 200) for i in range(6)]
    prod = product('tsc', colors)
    for s, c in prod:
        fill(c)
        shapes[s]()
        x += 30
        
        