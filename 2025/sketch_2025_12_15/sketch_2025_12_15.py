from random import shuffle

import py5
import numpy as np

grid = {}  # the nodes dict key_pos_tuple: value_origin_tuple  
to_check = []
NBS = [  # the possible jumps (neighbors)
    (-2, 0), (2, 0), (0, -2), (0, 2),
    (1, 1), (1, -1), (-1, 1), (-1, -1)
    ]
step = 20 # scale factor, distance between nodes
LIMIT = 20 # limit size of graph, pos smaller than width / 2 / step 

def setup():
    py5.size(800, 800)

def draw():
    py5.background(200)
    py5.translate(py5.width / 2, py5.height / 2)
    py5.stroke_weight(2)
    edges = np.array([(ki, kj, vi, vj) for (ki, kj), (vi, vj)
                      in grid.items()])
    py5.lines(edges * step)
    py5.stroke_weight(5)
    nodes = np.array(tuple(grid.keys()))
    py5.points(nodes * step)

def key_pressed():
    if py5.key == 'p':
        py5.save_frame('###.png')
    elif py5.key == ' ':
        py5.background(200)
        grid.clear()
        to_check.append((0, 0))
        while to_check:
            shuffle(to_check)
            new_to_check = []
            while to_check:
                i, j = to_check.pop()
                for ni, nj in NBS:
                    ti, tj = i + ni, j - nj  # target neighbor
                    if (abs(ti) < LIMIT and abs(tj) < LIMIT
                        and (ti, tj) not in grid):
                        grid[ti, tj] = (i, j)
                        new_to_check.append((ti, tj))
            to_check[:] = new_to_check
    
py5.run_sketch(block=False)


