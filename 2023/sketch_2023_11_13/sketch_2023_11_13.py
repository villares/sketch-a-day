salvar_pdf = False

def setup():
    size(1200, 400)
    frame_rate(12)
    
    
def draw():
    global salvar_pdf
    if salvar_pdf:
        # jogo da velha inclui numero do frame
        begin_record(PDF, '####.pdf') 
    
    background(100, 100, 250)
    w = 10
    stroke_weight(3)
    for x in range(0, width, w):
       
        ya = 100 + 50 * sin(x / 50 + frame_count / 5)
        yb = 100 + 75 * sin(x / 75 + frame_count / 5)
        yc = 100 + 100 * sin(x / 100 + frame_count / 5)
        yd = 100 + 75 * sin(x / 75 + frame_count / 5)
        stroke(0)
        line(x, yc, x, yd)
        line(x, ya + 200, x, yb + 200)
        stroke(255)
        line(x + w / 2, yc + ya, x + w / 2, yb + yd)
        

    if salvar_pdf:    # se verdadeiro, gravação em curso
        end_record()   # termina a gravação
        salvar_pdf = False  # desliga o 'flag'

def key_pressed():
    global salvar_pdf
    if key == 'p':
        salvar_pdf = True
        print('vou salvar um PDF, olha lá')