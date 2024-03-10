COLS = FILS = 10
GRADE_VIZS = ((-1, -1), (0, -1), (1, -1),
              (-1,  0),          (1,  0),
              (-1,  1), (0,  1), (1,  1))

board = {}

def setup():
    size(600, 600)
    rect_mode(CENTER)
    text_align(CENTER, CENTER)
    set_grid()

def set_grid():
    for fila in range(FILS):
        for coluna in range(COLS):
            e = random_choice((0, 1))
            board[coluna, fila] = e
            
def draw():
    tam = width / COLS
    for (coluna, fila), estado in board.items():
        y = tam / 2 + tam * fila
        x = tam / 2 + tam * coluna
        if estado == 1:
            fill(0)
        else:
            fill(255)
        if is_key_pressed and key == ' ':
            stroke(255, 0, 0)
            #stroke(get_graphics()._instance.fillColor)
        else:
            no_stroke()
        square(x, y, tam)
        no_stroke()
        vizs = vizinhos(coluna, fila)
        for v, (vi, vj) in zip(vizs, GRADE_VIZS):
            if estado and not v:
                fill(100, 100, 200)
            elif not estado and v:
                fill(100, 200, 100)
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
    
def key_pressed():
    if key == 's':
        save_frame('###.png' )
    elif key == 'r':
        set_grid()
        

