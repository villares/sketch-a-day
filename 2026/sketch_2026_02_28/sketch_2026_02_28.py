import py5
import numpy as np
 
CELL_SIZE = 20
NBS_OFFSETS = (  # the 8 neighbors 
    (-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)   
)

def setup():
    global board, COLS, ROWS
    py5.size(800, 800)
    py5.color_mode(py5.CMAP, 'viridis', 8)
    py5.text_align(py5.CENTER, py5.CENTER)
    py5.text_font(py5.create_font('Source Code Pro', CELL_SIZE - 6))
    COLS = py5.width // CELL_SIZE
    ROWS = py5.height // CELL_SIZE
    board = np.random.uniform(0, 1, size=(ROWS, COLS)) < 0.5
         
def draw():
    calc_live_nbs_count_board() # harder to explain… vectorized count strategy
    for col in range(COLS):
        for row in range(ROWS):
            alive = board[row, col]
            #ln = live_neighbours(row, col)  # easier to explain?
            ln = nbs_count_board[row, col]   # lookig at the nbs count array
            if alive:   # note order row-y, col-x
                py5.fill(ln)
            else:
                py5.fill('black')
            py5.square(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE)
            if alive:
                py5.fill('black')
            else:
                py5.fill('white')
            py5.text(str(ln),
                     col * CELL_SIZE + CELL_SIZE / 2,
                     row * CELL_SIZE + CELL_SIZE / 2)
            
def live_neighbours(row, col):  # easier to explain? possibly
    return sum(
        board[(row + ro) % ROWS, (col + co) % COLS]
        for ro, co in nbs_offsets
    )

def calc_live_nbs_count_board():  # harder to explain I think
    global nbs_count_board
    nbs_count_board = np.zeros_like(board, dtype=int) # note result is int array
    # rolling the board according to the offsets, the neighbors align on top
    for ro, co in NBS_OFFSETS:
        rolled = np.roll(np.roll(board, ro, axis=0), co, axis=1)
        nbs_count_board += rolled # and are added

def key_pressed():
    if py5.key == ' ':
        board[:] = np.random.uniform(0, 1, size=(ROWS, COLS)) < 0.5
    elif py5.key == 'p':
        py5.save_frame('####.png')

py5.run_sketch(block=False)
