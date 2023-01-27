"""
d'aprés Vera Molnar "interruptions" (https://collections.vam.ac.uk/item/O1193775/interruptions-drawing-vera-molnar/)

using py5 (py5coding.org) in imported mode
"""

from itertools import product

M = 12
rs = 26

def setup():
    size(800, 800)

def draw():
    background(0)
    stroke(200)
    #background(250, 250, 250)
    random_seed(rs)
    margin = M * 3
    interruptions = []
    for _ in range(10):
        w = random_int(1, 7)
        h = random_int(1, 5) 
        x = random_int(3, width // M - 3 - w)
        y = random_int(3, height // M - 3 - h)
        interruptions.extend(product(range(x, x + w), range(y, y + h)))        
    for y in range(margin, height - margin, M):
        for x in range(margin, width - margin, M):
            with push_matrix():
                translate(x, y)
                r = radians(random(-3, 3) * 30 * random(-1, 1))
                rotate(r)
                if (x // M, y // M) not in interruptions or abs(r) > PI * 0.20:
                    line(0,-M, 0, +M)
                    
def key_pressed():
    global rs
    print(rs)
    if key == 's':
        save(f'{rs}.png')
    else:
        rs += 1
