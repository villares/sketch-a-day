"""
d'aprés Vera Molnar "interruptions" (https://collections.vam.ac.uk/item/O1193775/interruptions-drawing-vera-molnar/)

using py5 (py5coding.org) in imported mode
"""

#from itertools import product

M = 20
rs = 24

def setup():
    size(1200, 800) #, PDF, f'{rs}.PDF')

def draw():
    background(250)
    stroke_weight(2)
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
                stroke(r * 100, 0, 100 - r * 100)
                if (x // M, y // M) not in interruptions or abs(r) > PI * 0.20:
                    line(0,-M, 0, +M)
    #save(f'{rs}.png')  
#    exit_sketch()

def key_pressed():
    global rs
    print(rs)
    if key == 's':
        save(f'{rs}.png')
    else:
        rs += 1
