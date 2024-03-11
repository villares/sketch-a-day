COLS = FILS = 20
GRADE_VIZS = ((-1, -1), (0, -1), (1, -1),
              (-1,  0),          (1,  0),
              (-1,  1), (0,  1), (1,  1))

board = {}

def setup():
    size(800, 800)
    rect_mode(CENTER)
    text_align(CENTER, CENTER)
    global tam
    tam = width / COLS
    set_grid(lambda:0)

def set_grid(func=lambda:random_choice((0, 1))):
    for fila in range(FILS):
        for coluna in range(COLS):
            e = random_choice((0, 1))
            board[coluna, fila] = func()
            
def draw():
    mc, mf = mouse_to_board(mouse_x, mouse_y)
    for (coluna, fila), estado in board.items():
        y = tam / 2 + tam * fila
        x = tam / 2 + tam * coluna
        if estado == 1:
            fill(0)
        else:
            fill(255)
        if (coluna, fila) == (mc, mf):
            stroke(255, 0, 0)
            stroke_weight(3)
        else:
            no_stroke()
        square(x, y, tam)
        no_stroke()
        vizs = vizinhos(coluna, fila)
        for v, (vi, vj) in zip(vizs, GRADE_VIZS):
            if estado and not v:
                fill(100, 100, 200)
            elif not estado and v:
                fill(200, 200, 100)
            else:
                no_fill()
            square(x + vi * tam / 3,
                   y + vj * tam / 3,
                   tam / 3)
        #text(''.join(str(v) for v in vizs), x, y)
    
def vizinhos(coluna, fila, default='x'):
    return tuple(
        board.get((coluna + cv, fila + fv), default)
        for cv, fv in GRADE_VIZS
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
    coluna = int(x/ tam)
    fila = int(y / tam)
    return coluna, fila

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

