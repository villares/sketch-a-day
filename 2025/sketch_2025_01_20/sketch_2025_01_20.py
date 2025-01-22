import py5

well = {}  # a dictionary for the walls and already fallen pieces
falling_piece = []   # will contain ((x,y), color) tuples, the component blocks of a piece
pieces = (
    [((x, y), (0, 200, 0)) for x, y in ((6, 0), (7, 0), (6, 1), (7, 1))], # O
    [((x, y), (0, 0, 200)) for x, y in ((4, 0), (5, 0), (6, 0), (6, 1))], # J
    [((x, y), (200, 200, 0)) for x, y in ((4, 1), (5, 1), (6, 1), (6, 0))], # L
    [((x, y), (200, 0, 0)) for x, y in ((4, 0), (5, 0), (6, 0), (7, 0))], # I
    [((x, y), (0, 200, 200)) for x, y in ((5, 0), (5, 1), (6, 1), (6, 2))], # S
    [((x, y), (200, 0, 200)) for x, y in ((6, 0), (6, 1), (5, 1), (5, 2))], # N
    [((x, y), (200,)) for x, y in ((4, 0), (5, 0), (6, 0), (5, 1))], # T
)

W, H, s = 16, 20, 25   # Well Width, Well Height, single block size
frame_sample = 12  # a smaller number makes it faster, a bigger number makes it slower

def setup():
    py5.size(425, 525, py5.P3D)
    start()
    
def start():
    global stopped, score
    score = 0
    stopped = False
    well.clear()
    for y in range(H):  # Set vertical well walls
        well[0, y] = (128,)
        well[W, y] = (128,)
    for x in range(W + 1):  # Set bottom of well
        well[x, H] = (128,)
    new_falling_piece()
    py5.loop() # reactivates draw if it is paused
    
def draw():
    global score
    py5.translate(s / 2 , s / 2)
    py5.background(0)
    for (x, y), block_color in list(well.items()) + falling_piece:
        py5.fill(*block_color)
        my_box(x * s, y * s, s)
    py5.fill(200)
    if stopped:
         py5.no_loop() # pause draw
    elif py5.frame_count % frame_sample == 0:
        if check_move(falling_piece, 0, 1):
            move_falling_piece(0, 1)
        else:
            add_to_well()
            new_falling_piece()
        r = check_filled_row()
        if r != -1:
            collapse_on_row(r)
            score += 1
 
def my_box(x, y, w):
    with py5.push_matrix():
        py5.translate(x, y)
        py5.box(w)
 
def new_falling_piece():
    global stopped
    falling_piece[:] = py5.random_choice(pieces)
    if not check_move(falling_piece):
        stopped = True
    
def add_to_well():
    for (x, y), b in falling_piece:
        well[x, y] = b

def check_move(p, h=0, v=0):
    for (x, y), _ in p:
        if well.get((x + h, y + v)):
            return False
    return True

def move_falling_piece(h, v):
    falling_piece[:] = (((x + h, y + v), b) for (x, y), b in falling_piece)

def check_filled_row():
    for r in range(H):
        filled_blocks = 0
        for c in range(W):
            if well.get((c, r)):
                filled_blocks += 1
        if filled_blocks == W:
            return r  # return first filled row found
    return -1 # no filled row

def clear_row(r):
    for c in range(1, W):
        if (c, r) in well:
            del well[c, r]

def collapse_on_row(row):
    # clear passed row and move blocks down to it
    for r in range(row, -1, -1): # moving upwards, starting from passed row
        clear_row(r) 
        for c in range(1, W):
            if b := well.get((c, r - 1)): # get block from 1 row up
                well[c, r] = b  
    
def rounded_falling_piece_centroid():
    positions = ((x, y) for (x, y), _ in falling_piece)
    coords = tuple(zip(*positions))
    max_x, max_y = map(max, coords)
    min_x, min_y = map(min, coords)
    return (max_x + min_x) // 2, (max_y + min_y) // 2

def rotated_falling_piece():
    cx, cy = rounded_falling_piece_centroid() # causes y displacement of -1 offset later...
    # translated to origin falling piece copy
    ttofpc = (((x - cx, y - cy), b) for (x, y), b in falling_piece) 
    return tuple(((y + cx, -x + cy + 1), b) for (x, y), b in ttofpc) # note y + 1 offset

def key_pressed():
    if py5.key == ' ':
        start()
    elif py5.key_code == py5.LEFT and check_move(falling_piece, -1, 0):
        move_falling_piece(-1, 0)
    elif py5.key_code == py5.RIGHT and check_move(falling_piece, 1, 0):
        move_falling_piece(1, 0);
    elif py5.key_code == py5.DOWN and check_move(falling_piece, 0, 1):
        move_falling_piece(0, 1);
    elif py5.key_code == py5.UP and check_move(rp := rotated_falling_piece()):
        falling_piece[:] = rp

py5.run_sketch()
        