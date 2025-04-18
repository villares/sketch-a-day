from random import choice
from itertools import product

import py5

W = 10   # cell size
nbs = (  # neighbourhood 
    (-1, -1), (0, -1), (1, -1),
    (-1,  0),          (1,  0),
    (-1,  1), (0,  1), (1,  1)
    )
board = {}  # empty dict
live_nbs_count = {}
debug = False
play = False
sample = 10 # smaller is faster

def setup():
    global cols, rows
    py5.size(800, 600)
    cols = int(py5.width / W)
    rows = int(py5.height / W)
    clear_board()
    py5.no_stroke()
    py5.color_mode(py5.HSB)
    
def clear_board():
    for col, row in product(range(cols), range(rows)):
        board[col, row] = 0
    nbs_count_update()
    
def random_board():
    for col, row in product(range(cols), range(rows)):
        board[col, row] = choice([0, 1])
    nbs_count_update()

def nbs_count_update():
    for col, row in product(range(cols), range(rows)):
        live_nbs_count[col, row] = sum(
            board[(col + dc) % cols, (row + df) % rows]
            for dc, df in nbs)
    
def step():
    global board
    next_board = {}
    for (col, row), state in board.items():
        live_nbs = live_nbs_count[col, row]
        # death by loneliness
        if state == 1 and live_nbs < 2:
            next_board[col, row] = 0
        # death by overcrowding
        elif state == 1 and live_nbs > 3:
            next_board[col, row] = 0
        # birth
        elif state == 0 and live_nbs == 3:
            next_board[col, row] = 1
        # keep same
        else:
            next_board[col, row] = state
    board = next_board
    nbs_count_update()
  
def draw():
    for (col, row), state in board.items():
        x, y = col * W, row * W
        live_nbs = live_nbs_count[col, row]
        if state == 1:
            py5.fill(live_nbs * 32, 200, 200)
        elif live_nbs == 3: # state == 0 but with become alive next.
            py5.fill(64)
        else: # state == 0
            py5.fill(0)
        py5.square(x, y, W)
        if debug:
            py5.fill(255)
            py5.text_align(py5.CENTER, py5.CENTER)
            py5.text(live_nbs, x + W / 2, y + W / 2)
        
    if play and (py5.frame_count % sample) == 0:
        step()
  
def key_pressed():
    global play
    if py5.key == 'c':
        clear_board()
    elif py5.key == 'r':
        random_board()
    elif py5.key == ' ':
        play = not play
        
py5.run_sketch(block=False)