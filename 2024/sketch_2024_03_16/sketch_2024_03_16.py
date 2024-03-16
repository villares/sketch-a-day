COLS = ROWS = 40
GRID_NBS = ((-1, -1), (0, -1), (1, -1),
            (-1,  0),          (1,  0),
            (-1,  1), (0,  1), (1,  1))

GRID_DIAG = ((-1, -1), ( 1, -1), (-1, 1), (1, 1))
GRID_ORTO = (( 0, -1), (-1,  0), ( 0, 1), (1, 0))

board = {}

def setup():
    size(800, 800)
    rect_mode(CENTER)
    text_align(CENTER, CENTER)
    global tam
    tam = width / COLS
    set_grid(lambda:0)

def set_grid(func=lambda:random_choice((0, 1))):
    for row in range(ROWS):
        for col in range(COLS):
            e = random_choice((0, 1))
            board[col, row] = func()
            
def draw():
    background(240)
    mc, mf = mouse_to_board(mouse_x, mouse_y)
    for (col, row), cell_state in board.items():
        y = tam / 2 + tam * row
        x = tam / 2 + tam * col
        if cell_state == 1:
            no_stroke
        else:
            stroke(220)
        if (col, row) == (mc, mf):
            stroke(255, 0, 0)
        no_fill()
        square(x, y, tam - 2)
        no_stroke()
        nbs = calc_nbs(col, row)
        if cell_state:
            for v, (vi, vj) in zip(nbs, GRID_NBS):
                if (vi, vj) in GRID_ORTO and not v:
                    fill(100, 100, 200)
                else:
                    no_fill()
                circle(x + vi * tam / 3,
                       y + vj * tam / 3,
                       tam / 3)
            for v, (vi, vj) in zip(nbs, GRID_NBS):
                if (vi, vj) in GRID_DIAG and not v:
                    fill(100, 200, 100)
                    circle(x + vi * tam / 3,
                           y + vj * tam / 3,
                           tam / 3)
                if (vi, vj) in GRID_DIAG and v:
                    fill(200, 100, 100)
                    circle(x + vi * tam / 3,
                           y + vj * tam / 3,
                           tam / 3)
                
            
            
        #text(''.join(str(v) for v in nbs), x, y)
    
def calc_nbs(col, row, default='x'):
    return tuple(
        board.get((col + cv, row + fv), default)
        for cv, fv in GRID_NBS
        )

def azulejo(x, y, tam, rot):
    push_matrix() # guarda coordenadas atuais
    translate(x, y) # muda o 0, 0
    rotate(rot)
    fill(255)
    square(0, 0, tam)
    fill(0)
    triangle(tam / 2, -tam / 2,
             tam / 2,  tam / 2,
            -tam / 2,  tam / 2)
    pop_matrix() # volta coordenadas anteriores

def mouse_to_board(x, y):
    col = int(x/ tam)
    row = int(y / tam)
    return col, row

def mouse_released():
    mc, mf = mouse_to_board(mouse_x, mouse_y)
    board[mc, mf] ^= 1

def key_pressed():
    if key == 's':
        save_frame('###.png' )
    elif key == 'r':
        set_grid()
    elif key == '0':
        set_grid(lambda:0)        
    elif key == '1':
        set_grid(lambda:1)        


