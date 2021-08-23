from random import choice

W = 90
grid = []
modules = dict()
ROWS = COLS = 10

def setup():
    size(900, 900)
    noFill()
    strokeWeight(2)
    generate_modules()
    generate_grid()
    
def generate_grid():
    grid[:] = []
    escape = 0
    while len(grid) < ROWS * COLS:
        i, j = index_to_grid(len(grid)) # me
        one_up = grid_to_index(i, j - 1)
        one_left = grid_to_index(i - 1, j)
        new_element = choice(choice(modules.keys()))
        horizontal_good = one_left < 0 or new_element in good_right_options[grid[one_left]]
        vertical_good = one_up < 0 or new_element in good_down_options[grid[one_up]]
        if horizontal_good and vertical_good:
           grid.append(new_element)
           escape = 0
        if escape > 100:
            break
        else:
            escape += 1
            
def draw():
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
                draw_module(modules[grid[k]])
            pop()
            k += 1
            
def keyPressed():
    if key == ' ':
        generate_grid()
    
def draw_module(module, o=12):
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
    modules['i'] = h_flip(h)
    modules['j'] = (a[0], a[-1], ((0, 2), (2, 0)))
    modules['k'] = (a[0], a[-1], ((2, 0), (3, 1)))
    
                                                                                
def grid_to_index(i, j):
    return i + j * COLS

def index_to_grid(k):
    i = k % COLS
    j = k // COLS
    return i, j
            
good_right_options = {
    'a': ['f', 'b', 'i'],
    'b': ['c', 'a', 'h', 'k'],
    'c': ['f', 'b', 'i'],
    'd': ['g', 'd', 'e', 'j'],
    'e': ['g', 'd', 'e', 'j'],
    'f': ['c', 'a', 'h', 'k'],
    'g': ['g', 'd', 'e', 'j'],
    'h': ['b', 'i', 'f'],
    'i': ['a', 'h', 'c'],
    'j': ['i', 'f', 'b'] ,
    'k': ['j', 'd', 'e', 'g'],
    }
          
good_down_options = {
    'a': ['a', 'b', 'g', 'j', 'k'],
    'b': ['a', 'b', 'g', 'j', 'k'],
    'c': ['f', 'e', 'h'],
    'd': ['f', 'e', 'h'],
    'e': ['c', 'd', 'i'],
    'f': ['c', 'd', 'i'],
    'g': ['a', 'b', 'g', 'j', 'k'],
    'h': ['c', 'i', 'd'],
    'i': ['f', 'h', 'e'],
    'j': ['f', 'e', 'h'],
    'k': ['f', 'e', 'h'],
    } 
       
