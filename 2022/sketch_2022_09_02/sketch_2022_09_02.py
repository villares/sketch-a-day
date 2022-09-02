from itertools import permutations, combinations

def setup():
    size(600, 200)
    no_fill()
    stroke_weight(2)
    stroke_join(ROUND)
    shapes = {
        't': lambda: triangle(x, y, x + w, y, x, y + w),
        's': lambda: square(x, y, w),
        'c': lambda: circle(x + w / 2 , y + w / 2, w)
        }
    w = 25
    x = y = 50
    permts = permutations('tsc', 2)
    for a, b in permts:
        shapes[a]()
        x += 30
        shapes[b]()
        x += 55

    combos = combinations('tsc', 2)
    x = 200
    y = 125
    for a, b in combos:
        shapes[a]()
        shapes[b]()
        x += 100