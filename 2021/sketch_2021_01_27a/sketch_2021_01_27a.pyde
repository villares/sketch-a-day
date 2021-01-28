from itertools import product, permutations

BORDER = 100
SIZE = 60

def setup():
    size(500, 740)
    background(0)
    grid = list(product(range(BORDER, width - BORDER + 1, SIZE),
                        range(BORDER, height - BORDER + 1, SIZE)))    
    
    perms = list(permutations((0, 64, 128, 128 + 64, 255), 3))
    print(len(perms), len(grid))
    
    for i, (x, y) in enumerate(grid):
        if i < len(perms):
            for j, ca in enumerate(perms[i]):
                cb = perms[i][(j + 1) % 3]
                for k in range(10):
                    t = k / 9.0
                    cc = lerpColor(ca, cb, t)
                    fill(cc); noStroke()
                    circle(x, y, SIZE - k * 2 - j * 20) 
