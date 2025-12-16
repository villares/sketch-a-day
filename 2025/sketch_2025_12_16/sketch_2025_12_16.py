from random import shuffle, seed

import py5
import numpy as np

NBS = [  # the possible jumps (neighbors)
    (-2, 0), (2, 0), (0, -2), (0, 2),
    #(-1, 0), (1, 0), (0, -1), (0, 1), 
    (1, 1), (1, -1), (-1, 1), (-1, -1)
    ]
STEP = 16 # scale factor, distance between nodes
LIMIT = 25 # limit size of graph, allows pos smaller than width / 2 / STEP 

grid = {}  # the nodes dict key_pos_tuple: value_origin_tuple  
to_check = []  # the growing nodes

def setup():
    py5.size(800, 800)
    generate()
    
def generate():
    grid.clear()

    to_check.append((0, 0))
    while to_check:
        shuffle(to_check)
        new_to_check = []
        s =  py5.frame_count #+ len(to_check) // LIMIT
        #seed(s)
        print(s)
        nbs = NBS.copy()            
        shuffle(nbs)
        while to_check:
            i, j = to_check.pop()
            for ni, nj in nbs[:6]:
                ti, tj = i + ni, j - nj  # target neighbor
                if (abs(ti) < LIMIT and abs(tj) < LIMIT
                    and (ti, tj) not in grid):
                    grid[ti, tj] = (i, j)
                    new_to_check.append((ti, tj))
        to_check[:] = new_to_check

def draw():
    py5.background(200)
    py5.translate(py5.width / 2, py5.height / 2)
    py5.stroke_weight(2)
    edges = np.array([(ki, kj, vi, vj) for (ki, kj), (vi, vj)
                      in grid.items()])
    py5.lines(edges * STEP)
    py5.stroke_weight(5)
    nodes = np.array(tuple(grid.keys()))
    py5.points(nodes * STEP)

def key_pressed():
    if py5.key == 'p':
        py5.save_frame('###.png')
    elif py5.key == ' ':
        generate()
    
py5.run_sketch(block=False)


