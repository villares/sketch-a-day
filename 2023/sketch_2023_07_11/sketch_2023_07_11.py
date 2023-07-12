bandeirinhas = []
salvar = False

def setup():
    size(500, 500)  
    fill(0)
    prepara_bandeirinhas()
    
def draw():
    global salvar
    background(255)
    if salvar:
        begin_record(SVG, f'{frame_count}.svg')
    for x, y, t in bandeirinhas:
        bandeirinha(x, y, t)
    if salvar:
        end_record()
        salvar = False
        
def key_pressed():
    global salvar
    if key == 's':
        salvar = True
    elif key == ' ':
        bandeirinhas[:] = []
        prepara_bandeirinhas()
    
def prepara_bandeirinhas(n=150):
    while len(bandeirinhas) < n:
        t = random(10, 50)
        x = random(t, width - t)
        y = random(t, height - t)
        for xo, yo, to in bandeirinhas:
            if dist(x, y, xo, yo) < (t + to) * 0.85:
                break
        else:
            bandeirinhas.append((x, y, t))
    
def bandeirinha(x, y, t):
    with push_matrix():
        translate(x, y)
        begin_shape()   # começar um forma
        vertex(-t / 2, -t / 2) 
        vertex(t / 2, -t / 2)
        vertex(t / 2, t / 2)
        vertex(0, 0)
        vertex(-t / 2, t / 2)
        end_shape(CLOSE) # terminar um forma fechada
