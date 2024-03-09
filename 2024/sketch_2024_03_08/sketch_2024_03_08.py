COLS = FILS = 10

board = {}

def setup():
    size(800, 800)
    rect_mode(CENTER)
    e = 0
    for fila in range(FILS):
        for coluna in range(COLS):
            e = random_int(-2, 3)
            board[fila, coluna] = e
            #e = (e + 1) % 4
            
def draw():
    if is_key_pressed and key == ' ':
        stroke(255, 0, 0)
    else:
        no_stroke()
    tam = width / COLS

    for (fila, coluna), estado in board.items():
        y = tam / 2 + tam * fila
        x = tam / 2 + tam * coluna
        if estado >= 0:
            angulo = estado * 90
            azulejo(x, y, tam, radians(angulo))
        else:
            if estado == -1:
                fill(0)
            else:
                fill(255)
            square(x, y, tam)
 
def azulejo(x, y, tam, rot):
    push_matrix() # guarda coordenadas atuais
    translate(x, y) # muda o 0, 0
    rotate(rot)
    fill(255)
    square(0, 0, tam)
    fill(0)
    triangle(tam / 2, -tam / 2,
             tam / 2, tam / 2,
             -tam / 2, tam / 2)
    pop_matrix() # volta coordenadas anteriores
    
def key_pressed():
    if key == 's':
        save_frame(__file__[:-2] + 'png')
