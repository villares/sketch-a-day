from itertools import combinations, permutations, product
from random import shuffle
def setup():
    global grid1, grid, points
    size(600, 600)
    grid = list(product(range(120, width, 180), repeat=2))
    points = list(permutations(grid, 3))
    print(len(points)),
    frameRate(10)
    print(len(points))

def draw():
    background(200),
    fill(0)
    for x, y in grid:
        circle(x, y, 120)
    fill(255)
    r, g, b = points[frameCount % len(points)]
    fill(200, 0, 0)
    circle(r[0], r[1], 60)
    fill(0, 200, 0)
    circle(g[0], g[1], 60)
    fill(0, 0, 200)
    circle(b[0], b[1], 60)
  
              
    
