import py5
import numpy as np
import py5_tools


NBS = [  # the possible jumps (neighbors)
    (-2, 0), (2, 0), (0, -2), (0, 2),
    (1, 1), (1, -1), (-1, 1), (-1, -1)
    ]
STEP = 16 # scale factor, distance between nodes
LIMIT = 25 # limit size of graph, allows pos smaller than width / 2 / STEP 
# START = [ (5, 5), (-5, 5), (5, -5), (-5, -5)]

grid = {}  # the nodes dict key_pos_tuple: value_origin_tuple  
to_check = []  # the growing nodes
paths = []
seed = 4
rotation = 180
rotation_on = True

def setup():
    global osb
    py5.size(800, 800, py5.P3D)
    py5.color_mode(py5.HSB)
    osb = py5.create_graphics(py5.width, py5.height)
    f = py5.create_font('Tomorrow Bold', 210)
    osb.begin_draw()
    osb.background(0)
    osb.text_font(f)
    osb.text_align(py5.CENTER, py5.CENTER)
    osb.text('FELIZ\nNATAL', 400, 400)
    osb.load_pixels()
    white = py5.color(255)
    black = py5.color(0)
    transparent = 0
    osb.pixels[:] = [transparent if px == white else black
                     for px in osb.pixels ]
    osb.update_pixels()
    osb.end_draw()                      
    generate()
    py5_tools.animated_gif(
        'out.gif',
        frame_numbers=range(1, 361, 10),
        duration=0.3
   )
    
def generate():
    global start
    py5.random_seed(seed)
    grid.clear()
    start = [(py5.random_int(-20, 20),
              py5.random_int(-20, 20))
             for _ in range(10)]
    to_check[:] = start
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

def dist_origin(t):
    return py5.dist(*t, 0, 0)

def calc_paths():
    # WIP: I think this is not working right yet
    paths.clear()
    visited = set()
    for node in sorted(grid.keys(),
                       key=dist_origin,
                       reverse=True):
        if node not in visited:
            z = 0
            visited.add(node)
            paths.append([node + (0,)])
            while node not in start:
                node = grid[node]
                visited.add(node)
                paths[-1].append(node + (z,))
                z += 1
    paths.sort(key=len)
    print(f'paths: {len(paths)}')

def draw():
    global rotation
    py5.ortho()
    py5.background(0)
    py5.stroke_weight(3)
    py5.no_fill()
    py5.translate(py5.width / 2, py5.height / 2, 0)
    py5.rotate_x(py5.radians(rotation))
    if rotation_on:
        rotation += 1
    for path in paths:
        py5.translate(0, 0, 0.05)
        edges = np.array(path)
        py5.stroke(len(path)* 10, 200, 255, 255)
        with py5.push_matrix(), py5.begin_shape():
            py5.translate(0, 0, -len(path) * STEP)
            py5.vertices(edges * STEP)
    #py5.image_mode(py5.CENTER)
    py5.image(osb, -400, -400)

def key_pressed():
    global seed, rotation_on
    if py5.key == 'p':
        py5.save_frame('###.png')
    elif py5.key == 'r':
        rotation_on = not rotation_on
    elif py5.key == ' ':
        seed += 1
        generate()
    
py5.run_sketch(block=False)
