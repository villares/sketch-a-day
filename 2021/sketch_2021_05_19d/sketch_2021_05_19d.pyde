from itertools import combinations, permutations, product
from random import shuffle
def setup():
    global grid1, grid2, g2c
    size(600, 600)
    # grid1 = list(product(range(120, width, 120), repeat=2))
    grid2 = list(product(range(120, width, 180), repeat=2))
    g2c = list(permutations(grid2, 3))
    # shuffle(g2c)
    frameRate(10) 
    print(len(g2c))

def draw():
    background(200),
    fill(0)
    for x, y in grid2:
        circle(x, y, 120)
    fill(255)
    r, g, b = g2c[frameCount % len(g2c)]
    fill(200, 0, 0)
    circle(r[0], r[1], 60)
    fill(0, 200, 0)
    circle(g[0], g[1], 60)
    fill(0, 0, 200)
    circle(b[0], b[1], 60)
  
              
    
