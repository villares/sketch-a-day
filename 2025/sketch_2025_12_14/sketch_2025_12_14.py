import py5
from random import shuffle

grid = {}
to_check = [(0, 0)]
NBS = [
    (-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1)
    ]

def setup():
    py5.size(800, 800)

def draw():
    py5.translate(py5.width / 2, py5.height / 2)
    py5.scale(20)
    py5.stroke_weight(2 / 20)
    for (oi, oj), (ti, tj) in grid.items():
        py5.line(oi, oj, ti, tj)
    #print(grid,  to_check, py5.frame_count)

def key_pressed():
    while to_check:
        shuffle(to_check)
        new_to_check = []
        while to_check:
            #print(to_check)
            i, j = to_check.pop()
            for ni, nj in NBS:
                ti, tj = i + ni, j - nj
                if (ti, tj) not in grid and abs(ti) < 20 and abs(tj) < 20:
                    grid[ti, tj] = (i, j)
                    new_to_check.append((ti, tj))
        to_check[:] = new_to_check
    
py5.run_sketch()


