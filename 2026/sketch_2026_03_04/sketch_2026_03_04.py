import py5
import numpy as np
 
CELL_SIZE = 4
NBS_OFFSETS = (  # the 16 neighbors 
    (-1, -1), ( 0, -1), (1, -1), (-1, 0),
    ( 1,  0), (-1,  1), (0,  1), ( 1, 1),
    (-2, -2), ( 0, -4), (2, -2), (-4, 0),
    ( 4,  0), (-2,  2), (0,  4), ( 2, 2),    
)
LOWER = 4
HIGHER = 6
BORN = 4

def setup():
    global board, next_board, COLS, ROWS, positions
    py5.size(800, 800)
    py5.no_smooth()
    py5.color_mode(py5.CMAP, 'plasma', len(NBS_OFFSETS))
    COLS = int(py5.width // CELL_SIZE)
    ROWS = int(py5.height // CELL_SIZE)
    board = np.random.uniform(0, 1, size=(ROWS, COLS)) < 0.5
    next_board = np.zeros_like(board)
    positions = np.array([
        [(col * CELL_SIZE + CELL_SIZE / 2, row * CELL_SIZE + CELL_SIZE / 2)
        for col in range(COLS)]
        for row in range(ROWS)
    ])
    
def draw():
    py5.background('black')
    calc_live_nbs_count_board() # vectorized count strategy
    py5.stroke_weight(CELL_SIZE)
    py5.stroke_cap(py5.PROJECT)
    for nn in range(17):
        py5.stroke(nn)
        py5.points(positions[board & (nbs_count_board == nn)])
    
    if py5.frame_count % 6 == 0:
        advance_board_a_step()
        py5.window_title(str(round(py5.get_frame_rate(), 1)))           

def calc_live_nbs_count_board():  # harder to explain I think
    global nbs_count_board
    nbs_count_board = np.zeros_like(board, dtype=int) # note result is int array
    # rolling the board according to the offsets, the neighbors align on top
    for ro, co in NBS_OFFSETS:
        rolled = np.roll(np.roll(board, ro, axis=0), co, axis=1)
        nbs_count_board += rolled # and are added

def advance_board_a_step():
    next_board[:] = board  # this will carry on some 2-nbs & 3-nbs cells!
    lonely = nbs_count_board < LOWER
    crowded = nbs_count_board > HIGHER
    born = nbs_count_board == BORN
    next_board[lonely + crowded] = False  # kills cels
    next_board[born] = True               # adds new cells
    board[:] = next_board  # substitutes
    

def key_pressed():
    if py5.key == ' ':
        board[:] = np.random.uniform(0, 1, size=(ROWS, COLS)) < 0.5
    elif py5.key == 'p':
        py5.save_frame('####.png')

py5.run_sketch(block=False)
