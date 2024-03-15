COLS = FILS = 20
GRADE_VIZS = ((-1, -1), (0, -1), (1, -1),
              (-1,  0),          (1,  0),
              (-1,  1), (0,  1), (1,  1))

GRADE_DIAG = ((-1, -1),  (1, -1),
              (-1,  1),  (1,  1))

GRADE_ORTO = ((0, -1), (-1,  0),
              (1,  0), (0,  1))

board = {}

def setup():
    size(800, 800)
    no_smooth()
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
    background(240)
    mc, mf = mouse_to_board(mouse_x, mouse_y)
    for (coluna, fila), estado in board.items():
        y = tam / 2 + tam * fila
        x = tam / 2 + tam * coluna
        stroke_weight(1)
        if (coluna, fila) == (mc, mf):
            fill(200)
        else:
            no_fill()
        stroke(200)
        square(x, y, tam)
    
    for (coluna, fila), estado in board.items():
        y = tam / 2 + tam * fila
        x = tam / 2 + tam * coluna
        stroke_weight(tam / 4)
        vizs = vizinhos(coluna, fila)
        if estado:
            for v, (vi, vj) in zip(vizs, GRADE_VIZS):
                stroke(100, 100, 200)           
#                 if v and (vi, vj) in GRADE_DIAG:   
#                     line(x, y, x + vi * tam / 2,
#                                y + vj * tam / 2)
                if not v and (vi, vj) in GRADE_DIAG:   
                    line(x + vi * tam / 2 - vj * tam / 2,
                         y + vj * tam / 2 + vi * tam / 2,
                         x + vi * tam / 2 + vj * tam / 2,
                         y + vj * tam / 2 - vi * tam / 2,)

            for v, (vi, vj) in zip(vizs, GRADE_VIZS):
                stroke(100, 200, 100)
                if v and (vi, vj) in GRADE_ORTO:   
#                     line(x - vi * tam / 2 - vj * tam / 2,
#                          y - vj * tam / 2 + vi * tam / 2,
#                          x + vi * tam / 2 - vj * tam / 2,
#                          y + vj * tam / 2 + vi * tam / 2)
#                     line(x - vi * tam / 2 + vj * tam / 2,
#                          y - vj * tam / 2 - vi * tam / 2,
#                          x + vi * tam / 2 + vj * tam / 2,
#                          y + vj * tam / 2 - vi * tam / 2)
                    pass
                if not v and (vi, vj) in GRADE_ORTO:
                    line(x + vi * tam / 2 - vj * tam / 2,
                         y + vj * tam / 2 + vi * tam / 2,
                         x + vi * tam / 2 + vj * tam / 2,
                         y + vj * tam / 2 - vi * tam / 2,)
                    
    
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

