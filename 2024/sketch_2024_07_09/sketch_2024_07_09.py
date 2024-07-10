well = {}
falling_piece = []

colors = {
    'r': color(200, 0, 0),  # red
    'g': color(0, 200, 0),  # green
    'b': color(0, 0, 200),  # blue
    'y': color(200, 200, 0),  # yellow
    'm': color(200, 0, 200),  # magenta
    'c': color(0, 200, 200),  # cian
    't': color(200, 200, 200),  # gray
    'w': 128  # well walls, dark gray
    }

pieces = (
    (((6, 0), 'g'), ((7, 0), 'g'), ((6, 1), 'g'), ((7, 1), 'g')), # O
    (((4, 0), 'b'), ((5, 0), 'b'), ((6, 0), 'b'), ((6, 1), 'b')), # J
    (((4, 1), 'y'), ((5, 1), 'y'), ((6, 1), 'y'), ((6, 0), 'y')), # L
    (((4, 0), 'r'), ((5, 0), 'r'), ((6, 0), 'r'), ((7, 0), 'r')), # I
    (((5, 0), 'c'), ((5, 1), 'c'), ((6, 1), 'c'), ((6, 2), 'c')), # S
    (((6, 0), 'm'), ((6, 1), 'm'), ((5, 1), 'm'), ((5, 2), 'm')), # N
    (((4, 0), 't'), ((5, 0), 't'), ((6, 0), 't'), ((5, 1), 't')), # T
)

W, H, s = 11, 20, 25   # Well Width, Well Height, single block size

def setup():
    size(525, 525)
    text_align(CENTER, CENTER)
    text_size(80)
    start()
    
def start():
    global game_over, score
    game_over, score = False, 0
    well.clear()
    for y in range(H):
        well[0, y] = 'w'
        well[W, y] = 'w'
    for x in range(W + 1):
        well[x, H] = 'w'
    new_falling_piece()
    loop() # reactivates draw if it is paused
    
def draw():
    global score
    background(0)
    for (x, y), b in list(well.items()) + falling_piece:
        fill(colors[b])
        square(x * s, y * s, s)
    fill(200)
    text(score, W * s + (width - W * s) / 2, s * 2)        
    if game_over:
         fill(255)
         text('GAME OVER',
              width / 2, height / 2)
         no_loop() # pause draw
    elif frame_count % 10 == 0:
        if check_move(falling_piece, 0, 1):
            move_falling_piece(0, 1)
        else:
            add_to_well()
            falling_piece[:] =[]
            new_falling_piece()
        r = check_filled_row()
        if r != -1:
            collapse_on_row(r)
            score += 1
 
def new_falling_piece():
    global game_over
    falling_piece[:] = random_choice(pieces)
    if not check_move(falling_piece):
        game_over = True
    
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

def collapse_on_row(r):
    # clear row r and move blocks down to it
    for row in range(r, -1, -1): # moving upwards, starting from row r
        clear_row(row) 
        for c in range(1, W):
            if b := well.get((c, row-1)):
                well[c, row] = b
    
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
    if key == ' ':
        start()
    elif key_code == LEFT and check_move(falling_piece, -1, 0):
        move_falling_piece(-1, 0)
    elif key_code == RIGHT and check_move(falling_piece, 1, 0):
        move_falling_piece(1, 0);
    elif key_code == DOWN and check_move(falling_piece, 0, 1):
        move_falling_piece(0, 1);
    elif key_code == UP and check_move(rp := rotated_falling_piece()):
            falling_piece[:] = rp