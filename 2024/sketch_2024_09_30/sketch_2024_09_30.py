from itertools import product, combinations

import py5  # check out https://github.com/py5coding 

# ideas... 1-Truchets - 6 possible modules, 2 x 2 -> 6 ** 4 -> 1296  
#          2-Lines on a reduced 5 x 5 grid (21 points)

S = 200 # scale
M = 100 # margin
edges = [frozenset([(0, 1), (1, 2)])]

def setup():
    global grid, edges
    py5.size(600, 600)    
    grid = list(product(range(3), repeat=2))


def draw():
    py5.translate(M, M)
    py5.stroke(0)
    py5.stroke_weight(5)
    py5.points((x * S, y * S) for x, y in grid)
    py5.stroke(255)
    py5.stroke_weight(3)
    py5.lines((ax * S, ay * S, bx * S, by * S)
              for (ax, ay), (bx, by) in edges)
                
    
    
        
py5.run_sketch(block=False)
        
        




