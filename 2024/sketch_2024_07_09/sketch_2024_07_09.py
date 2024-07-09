well = {}
piece = []
game_over = False
cores = {
    'r': color(200, 0, 0),  # red
    'g': color(0, 200, 0),  # green
    'b': color(0, 0, 200),  # azul
    'y': color(290, 200, 0),  # azul
    'w': 128  # cinza
    }

pieces = (
    (((2, 0), 'r'),    # O
     ((3, 0), 'r'),
     ((2, 1), 'r'),
     ((3, 1), 'r')),
    (((2, 0), 'b'),    # J
     ((3, 0), 'b'),
     ((4, 0), 'b'),
     ((4, 1), 'b')),
    (((2, 0), 'g'),    # L
     ((3, 0), 'g'),
     ((4, 0), 'g'),
     ((4, -1), 'g')),
    (((2, 0), 'y'),    # I
     ((3, 0), 'y'),
     ((4, 0), 'y'),
     ((5, 0), 'y')),

)
W = 11
H = 20
s = 25

def setup():
    size(525, 525)
    for y in range(H):
        well[0, y] = 'w'
        well[W, y] = 'w'
    for x in range(W + 1):
        well[x, H] = 'w'
    new_piece()
    
def draw():
    background(0)
    for (x, y), b in list(well.items()) + piece:
        fill(cores[b])
        square(x * s, y * s, s)
        
    if game_over:
         fill(255)
         text_align(CENTER, CENTER)
         text_size(80)
         text('GAME OVER',
              width / 2, height / 2)
         
    elif frame_count % 10 == 0:
        if check_move(0, 1):
            move_piece(0, 1)
        else:
            add_to_well()
            piece[:] =[]
            new_piece()
        r = check_filled_row()
        if r != -1:
            collapse_row(r)
 
def new_piece():
    global game_over
    piece[:] = random_choice(pieces)
    if not check_move(0,0):
        game_over = True
    
def add_to_well():
    for (x, y), b in piece:
        well[x, y] = b
        
def check_move(h, v):
    for (x, y), _ in piece:
        if well.get((x + h, y + v)):
            return False
    return True

def move_piece(h, v):
    piece[:] = (((x + h, y + v), b) for (x, y), b in piece)

def check_filled_row():
    for r in range(H):
        row = 0
        for c in range(W):
            if well.get((c, r)):
                row += 1
        if row == W:
            print(row, r)
            return r
    return -1

def clear_row(r):
    for c in range(1, W):
        if (c, r) in well:
            del well[c, r]

def collapse_row(r):
    for row in range(r, -1, -1):
        clear_row(row)
        for c in range(1, W):
            if b := well.get((c, row-1)):
                well[c, row] = b
    
def piece_centroid(p):
    positions = ((x, y) for (x, y), _ in p)
    coords = tuple(zip(*positions))
    max_x, max_y = map(max, coords)
    min_x, min_y = map(min, coords)
    return (max_x + min_x) / 2, (max_y + min_y) / 2

def rotate_piece():
    cx, cy = piece_centroid(piece)
    ttop = (((x - cx, y - cy), b) for (x, y), b in piece) # translated to origin piece
    piece[:] = (((-y + cx, x + cy), b) for (x, y), b in ttop)

def key_pressed():
    if key_code == LEFT and check_move(-1, 0):
        move_piece(-1, 0)
    elif key_code == RIGHT and check_move(1, 0):
        move_piece(1, 0);
    elif key_code == UP and check_move(1, 0):
        rotate_piece();
        

