from __future__ import division
from random import choice
from itertools import product

# not very good

W = 80
grid = []
modules = dict()
ROWS = COLS = 10
OFFSET = 8

def setup():
    size(800, 800, P3D)
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
            # mmm = sorted(modules.keys(), key=lambda k:len(modules[k]), reverse=True)
            # new_element = mmm[escape % len(modules)]
            # new_element = mmm[escape % len(mmm)]
            new_element = choice(modules.keys())
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
    # translate(width / 2, height / 2, -400)
    # translate(0, 400, -200)
    # rotateX(frameCount / 100.0)
    # # translate(-width / 2, -height / 2)
    # translate(0, -400, 0)
    # print(frameCount)
    background(0)
    # grid = sorted(modules.keys()) * 100
    
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
    for x, y in module:
        for i in range(-2, 3):
            stroke( 128 + 64 * i, 128, 128 -64 * i)
        
            vxa = x * w + i * o if y == 0 or y == 3 else x * w
            vya = y * w + i * o if x == 0 or x == 3 else y * w
            push()
            translate(0, 0, i * o)
            circle(vxa, vya, 5)
            pop()
            vxb = 1.5 * w #xb * w + i * o if yb == 0 or yb == 3 else xb * w
            vyb = 1.5 * w #yb * w + i * o if xb == 0 or xb == 3 else yb * w            
            line(vxa, vya, i * o, vxb, vyb, i * o)
            
def h_flip(module):
    return tuple(tuple((3 - x, y) for x, y in segment)
                 for segment in module)
    
def d_flip(module):
    return tuple(tuple((y, x) for x, y in segment)
                 for segment in module)

def generate_modules():
    _a_ = ((1, 0), (2, 0))
    a_ = ((2, 0),)
    _a = ((1, 0),)
    a = (_a_, a_, _a, ())
    _b_ = ((1, 3), (2, 3))
    b_ = ((2, 3),)
    _b = ((1, 0),)
    b = (_b_, b_, _b, ())
    _c_ = ((0, 1), (0, 2))
    c_ = ((0, 1),)
    _c = ((0, 2),)
    c = (_c_, c_, _c, ())
    _d_ = ((0, 1), (0, 2))
    d_ = ((0, 1),)
    _d = ((0, 2),)
    d = (_d_, d_, _d, ())
    abcd = product(a, b, c, d)
    for i, p in enumerate(abcd):
        sides = bool(p[0]) + bool(p[1]) + bool(p[2]) + bool(p[3])
        if  sides >= 2: # and (p[2] or p[3]):
            modules[i] = p[0] + p[1] + p[2] + p[3]
    len(modules)
                       
 
                                                                                                                                               
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
    # for kv in good_right_options.items():
    #     print(kv)
    # print good_right_options
                
def edge_ys(m, ex):
    ys = []
    for x, y in m:
        if x == ex:
            ys.append(y)
    return tuple(ys)   

def edge_xs(m, ey):
    xs = []
    for x, y in m:
        if y == ey:
            xs.append(x)
    return tuple(xs)   
