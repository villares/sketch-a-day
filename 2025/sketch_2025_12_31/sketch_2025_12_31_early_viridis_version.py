import py5
import numpy as np
import py5_tools

# # you need to run the following line just once
# py5_tools.processing.download_library("PeasyCam")
from peasy import PeasyCam

NBS = [  # the possible jumps (neighbors)
    (-1, 0), (1, 0), (0, -1), (0, 1),
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
white = py5.color('white')
nodes = set()


def setup():
    py5.size(800, 800, py5.P3D)
    py5.color_mode(py5.CMAP, 'viridis_r', 255)
    #py5.stroke_cap(py5.PROJECT)
    #py5.hint(py5.ENABLE_STROKE_PERSPECTIVE)
    #py5.hint(py5.ENABLE_DEPTH_SORT)
    cam = PeasyCam(py5.get_current_sketch(), 600)
    py5_tools.animated_gif(
        'out2.gif',
        frame_numbers=range(1, 361, 10),
        duration=0.3
   )
    global osb
    osb = py5.create_graphics(py5.width, py5.height)
    f = py5.create_font('Tomorrow Bold', 250)
    osb.begin_draw()
    osb.background('black')
    osb.fill(white)
    osb.text_font(f)
    osb.text_align(py5.CENTER, py5.CENTER)
    osb.text('2026', 400, 400)
    #osb.text('FELIZ\n2026', 400, 400)
    osb.end_draw()
    generate()

def draw():
    global rotation, seed
    #py5.ortho()
    py5.scale(1, 1, -1)
    py5.background('black')
    py5.no_fill()
    py5.rotate_x(py5.radians(rotation))
    if rotation_on:
        rotation += 1
    for path in paths:
        py5.stroke_weight(STEP / 3)
        #mx, my, mz = np.array(min(path, key=lambda v: v[2]))
        py5.stroke(len(path) * 10 % 255)
        with py5.begin_shape():
            py5.vertices(np.array(path) * STEP)
    py5.translate(0, 0, -4)
    py5.stroke(1)
    py5.stroke_weight(STEP)
    py5.points(np.array(tuple(nodes)) * STEP)
    #print(mv, type(mv), STEP, type(STEP))
    #py5.image(osb, 0, 0)
    if rotation % 36 == 0:
        seed += 1
        generate()

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
    paths.clear()
    nodes.clear()
    visited = set()
    for x, y in sorted(grid.keys(),
                       key=dist_origin,
                       reverse=True):        
        if (x, y) not in visited:
            z = 0
            check_text(x, y, z)
            visited.add((x, y))
            paths.append([(x, y, 0)])
            while (x, y) not in start:
                x, y = grid[x, y]
                visited.add((x, y))
                paths[-1].append((x, y, z))
                z += 1
    paths.sort(key=len)
    for path in paths:
        for x, y, z in path:
            check_text(x, y, z)
    print(f'paths: {len(paths)}')
    
def check_text(x, y, z):
    if (x, y, z) not in nodes:
        px = osb.get_pixels(x * STEP + py5.width // 2, y * STEP + py5.height // 2)
        if px == white:
            nodes.add((x, y, z))

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

