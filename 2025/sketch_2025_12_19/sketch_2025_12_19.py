import py5
import numpy as np

# # you need to run the following 2 lines just once
# import py5_tools
# py5_tools.processing.download_library("PeasyCam")

from peasy import PeasyCam

NBS = [  # the possible jumps (neighbors)
    (-2, 0), (2, 0), (0, -2), (0, 2),
    (1, 1), (1, -1), (-1, 1), (-1, -1)
    ]
STEP = 16 # scale factor, distance between nodes
LIMIT = 25 # limit size of graph, allows pos smaller than width / 2 / STEP 

grid = {}  # the nodes dict key_pos_tuple: value_origin_tuple  
to_check = []  # the growing nodes
paths = []
seed = 2

def setup():
    py5.size(800, 800, py5.P3D)
    py5.color_mode(py5.HSB)
    generate()
    cam = PeasyCam(py5.get_current_sketch(), 200)
    
def generate():
    py5.random_seed(seed)
    grid.clear()
    to_check.append((0, 0)) # starting node ate the center
    while to_check:
        #shuffle(to_check)
        new_to_check = []
        nbs =  py5.random_permutation(NBS)
        to_check[:] = py5.random_permutation(to_check)
        while to_check:
            i, j = to_check.pop()
            for ni, nj in nbs[:6]:
                ti, tj = i + ni, j - nj  # target neighbor
                if (abs(ti) < LIMIT and abs(tj) < LIMIT
                    and (ti, tj) not in grid):
                    grid[ti, tj] = (i, j)
                    new_to_check.append((ti, tj))
        to_check[:] = new_to_check
    calc_paths()


def calc_paths():
    # WIP: I think this is not working right yet
    paths.clear()
    visited = set()
    for node in sorted(grid.keys()):
        if node not in visited:
            z = 0
            visited.add(node)
            paths.append([node + (0,)])
            while node != (0, 0):
                node = grid[node]
                visited.add(node)
                paths[-1].append(node + (z,))
                z += 1
    paths.sort(key=len)
    print(f'paths: {len(paths)}')

def draw():
    py5.background(250)

# # you'll need these if not using PeasyCam
#     py5.translate(py5.width / 2, # - STEP,
#                   py5.height / 2,
#                   ) # center origin
#     py5.rotate_x(py5.radians(30))
#     py5.rotate_y(py5.radians(30))

    py5.translate(0, 0, -400)
    py5.stroke_weight(2)
    py5.no_fill()
    for path in paths:
        edges = np.array(path)
        py5.stroke(len(path)* 10, 200, 150, 100)
        #py5.translate(0.02, 0)
        #py5.translate(0, 0, 1)
        with py5.begin_shape():
            py5.vertices(edges * STEP) 

    py5.stroke_weight(4)
    py5.stroke(0)
    nodes = np.array(tuple(grid.keys()))
    py5.points(nodes * STEP)


def key_pressed():
    global seed
    if py5.key == 'p':
        py5.save_frame('###.png')
    elif py5.key == ' ':
        seed += 1
        generate()
    
py5.run_sketch(block=False)
