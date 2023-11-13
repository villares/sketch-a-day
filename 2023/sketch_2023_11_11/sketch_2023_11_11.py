salvar_pdf = False

def setup():
    size(1200, 400)
    frame_rate(12)
    
    
def draw():
    global salvar_pdf
    if salvar_pdf:
        # jogo da velha inclui numero do frame
        begin_record(PDF, '####.pdf') 
    
    background(200)
    w = 10
    stroke_weight(3)
    for x in range(0, width, w):
        stroke(0)
        ya = 200 + 50 * sin(x / 50 + frame_count / 10)
        yb = 200 + 25 * sin(x / 25 + frame_count / 10)
        line(x, ya, x, yb)
        stroke(255)
        yc = 200 + 100 * sin(x / 100 + frame_count / 10)
        yd = 200 + 75 * sin(x / 75 + frame_count / 10)
        line(x + w / 2, yc, x + w / 2, yd)

    if salvar_pdf:    # se verdadeiro, gravação em curso
        end_record()   # termina a gravação
        salvar_pdf = False  # desliga o 'flag'
    # não entra mais na gravação
    text('oi oi oi', 100, 100)

def key_pressed():
    global salvar_pdf
    if key == 'p':
        salvar_pdf = True
        print('vou salvar um PDF, olha lá')