from itertools import product, combinations

import py5  # check out https://github.com/py5coding 

# ideas... 1-Truchets
#          2-Lines on a reduced 5 x 5 grid (21 points)

W = 200

def setup():
    global grid, edges
    py5.size(600, 600)    
    grid = list(product(range(100, 501, W), repeat=2))
    edges = [frozenset([(100, 300), (300, 500)])]
    
def draw():
    py5.stroke(0)
    py5.stroke_weight(5)
    py5.points(grid)
    py5.stroke(255)
    py5.stroke_weight(3)
    py5.lines((ax, ay, bx, by) for (ax, ay), (bx, by) in edges)
                
    
    
        
py5.run_sketch(block=False)
        
        




