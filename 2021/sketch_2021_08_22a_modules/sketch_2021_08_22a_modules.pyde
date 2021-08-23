from __future__ import division
from random import choice

W = 100
grid = []
modules = dict()
ROWS = COLS = 8
OFFSET = 13

def setup():
    size(800, 800)
    noFill()
    strokeWeight(3)
    generate_modules()
    check_connetions()
    generate_grid()
    
def generate_grid():
    grid[:] = []
    while len(grid) != ROWS * COLS:
        grid[:] = [choice(modules.keys())]
        escape = 0
        mmm = list(modules.keys())
        while len(grid) < ROWS * COLS:
            i, j = index_to_grid(len(grid)) # me
            one_up = grid_to_index(i, j - 1)
            one_left = grid_to_index(i - 1, j)
            new_element = choice(modules.keys())
            # new_element = mmm[escape % len(mmm)]
            horizontal_good = i == 0 or new_element in good_right_options[grid[one_left]]
            vertical_good = j == 0 or new_element in good_down_options[grid[one_up]]
            if horizontal_good and vertical_good:
                grid.append(new_element)
                escape = 0
            if escape > 10000:
                break
            else:
                escape += 1
                
def draw():
    # print(frameCount)
    background(0)
    k = 0
    for j in range(ROWS):
        for i in range(COLS):
            push()
            translate(i * W, j * W)
            if k < len(grid):
                if keyPressed:
                    stroke(255)
                    strokeWeight(0.5)
                    rect(0, 0, W, W)
                    text(grid[k], W / 2, W / 2)
                draw_module(modules[grid[k]], OFFSET)
            pop()
            k += 1
            
def keyPressed():
    if key == ' ':
        generate_grid()
    
def draw_module(module, o=5):
    w = W / 3
    for segment in module:
        for i in range(-2, 3):
            stroke(128 + 64 * i, 255, 128 - 64 * i)
            beginShape()
            for x, y in segment:
                vx = x * w + i * o if y == 0 or y == 3 else x * w
                vy = y * w + i * o if x == 0 or x == 3 else y * w
                vertex(vx, vy)
            endShape()
            
def h_flip(module):
    return tuple(tuple((3 - x, y) for x, y in segment)
                 for segment in module)
    
def d_flip(module):
    return tuple(tuple((y, x) for x, y in segment)
                 for segment in module)

def generate_modules():
    a = (
        ((1, 0), (0, 1)),
        ((2, 0), (1, 3)),
        ((3, 2), (2, 3)),
        )
    modules['a'] = a
    modules['b'] = h_flip(a)
    modules['c'] = (a[0], a[-1])
    modules['d'] = d_flip(a)
    modules['e'] = h_flip(d_flip(a))
    modules['f'] = h_flip((a[0], a[-1]))
    modules['g'] = h_flip((a[0], a[-1])) + (a[0], a[-1])
    h = (
        ((2, 0), (0, 1)),
        ((1, 3), (3, 2)),
        )    
    modules['h'] = h
    modules['dh'] = d_flip(h)
    modules['i'] = h_flip(h)
    modules['di'] = d_flip(h_flip(h))
        
    modules['j'] = (a[0], a[-1], ((0, 2), (2, 0)))
    modules['dj'] = d_flip((a[0], a[-1], ((0, 2), (2, 0))))
    modules['hj'] = h_flip((a[0], a[-1], ((0, 2), (2, 0))))
    modules['dhj'] = d_flip(h_flip((a[0], a[-1], ((0, 2), (2, 0)))))
    
    modules['k'] = (a[0], a[-1], ((2, 0), (3, 1)))
    modules['l'] = h_flip((a[0], a[-1], ((2, 0), (3, 1))))
    modules['m'] = h_flip((a[0], a[-1], ((2, 0), (3, 1))))
    modules['n'] = d_flip((a[0], a[-1], ((2, 0), (3, 1))))
    modules['o'] = d_flip((a[0], a[-1], ((2, 0), (3, 1))))
    modules['n'] = h_flip(d_flip((a[0], a[-1], ((2, 0), (3, 1)))))
    modules['o'] = h_flip(d_flip((a[0], a[-1], ((2, 0), (3, 1)))))
    
                                                                                
def grid_to_index(i, j):
    return i + j * COLS

def index_to_grid(k):
    i = k % COLS
    j = k // COLS
    return i, j
            

def check_connetions():
    global good_right_options, good_down_options
    good_right_options = {}
    good_down_options = {}
    for m in modules.keys():
        good_right_options[m] = []
        good_down_options[m] = []
        for om in modules.keys():
            reys = edge_ys(modules[m], 3)  # right edge Ys
            leys = edge_ys(modules[om], 0)  # left edge Ys
            if reys == leys:
                good_right_options[m].append(om)
            bexs = edge_xs(modules[m], 3)  # bottom edge Xs
            texs = edge_xs(modules[om], 0)  # top edge Xs
            if bexs == texs:
                good_down_options[m].append(om)
    print good_right_options
    print good_right_options
                
def edge_ys(m, ex):
    ys = []
    for segment in m:
        for x, y in segment:
            if x == ex:
                ys.append(y)
    return tuple(ys)   

def edge_xs(m, ey):
    xs = []
    for segment in m:
        for x, y in segment:
            if y == ey:
                xs.append(x)
    return tuple(xs)   
