import py5
import numpy as np
 
CELL_SIZE = 16
NBS_OFFSETS = (  # the 8 neighbors 
    (-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)   
)

def setup():
    global board, next_board, COLS, ROWS
    py5.size(800, 800)
    py5.color_mode(py5.CMAP, 'viridis', 8)
    py5.text_align(py5.CENTER, py5.CENTER)
    py5.text_font(py5.create_font('Source Code Pro', CELL_SIZE - 6))
    COLS = py5.width // CELL_SIZE
    ROWS = py5.height // CELL_SIZE
    board = np.random.uniform(0, 1, size=(ROWS, COLS)) < 0.5
    next_board = np.zeros_like(board)
         
def draw():
    calc_live_nbs_count_board() # harder to explain… vectorized count strategy
    for col in range(COLS):
        for row in range(ROWS):
            alive = board[row, col]
            ln = nbs_count_board[row, col]   # lookig at the nbs count array
            if alive:   # note order row-y, col-x
                py5.fill(ln)
            else:
                py5.fill('black')
            py5.square(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE)
            if alive:
                if ln in (2, 3):
                    py5.fill('white')
                else:
                    py5.fill('black')
            elif ln == 3:
                py5.fill(ln) 
            else:
                py5.fill('black') # will disappear on black background
            py5.text(str(ln),
                     col * CELL_SIZE + CELL_SIZE / 2,
                     row * CELL_SIZE + CELL_SIZE / 2)
    if py5.frame_count % 2 == 0:
        advance_board_a_step()
            

def calc_live_nbs_count_board():  # harder to explain I think
    global nbs_count_board
    nbs_count_board = np.zeros_like(board, dtype=int) # note result is int array
    # rolling the board according to the offsets, the neighbors align on top
    for ro, co in NBS_OFFSETS:
        rolled = np.roll(np.roll(board, ro, axis=0), co, axis=1)
        nbs_count_board += rolled # and are added

def advance_board_a_step():
    next_board[:] = board  # this will carry on some 2-nbs & 3-nbs cells!
    lonely = nbs_count_board < 2
    crowded = nbs_count_board > 3
    born = nbs_count_board == 3
    next_board[lonely + crowded] = False  # kills cels
    next_board[born] = True               # adds new cells
    board[:] = next_board  # substitutes
    

def key_pressed():
    if py5.key == ' ':
        board[:] = np.random.uniform(0, 1, size=(ROWS, COLS)) < 0.5
    elif py5.key == 'p':
        py5.save_frame('####.png')

py5.run_sketch(block=False)
