seed = 1
graus = 15

def setup():
    size(1200, 900)
    #frame_rate(1)
    
def draw():
    background(200)
    random_seed(seed)
    grade(0, 0, width, height, 4, 3)
    
def grade(xg, yg, largura, altura, colunas, filas):
    w = largura / colunas
    h = altura / filas
    for c in range(colunas):  # c = 0 ... colunas-1
        x = xg + c * w
        for f in range(filas):
            y = yg + f * h
            if random(100) < 50:
                if w > 10:
                    grade(x, y, w, h, 3, 3)
                else:
                    no_fill()
                    stroke(0)
                    stroke_weight(1)
                    square(x, y, w - 2)
            else:
                arvore(x + w/2, y + h/2 , w / 2)
                
def key_pressed():
    save_frame('###.png')
    global seed
    seed = seed + 1
    print(seed)
    
def arvore(x, y, tamanho):
    push_matrix()
    translate(x, y + tamanho)
    galho(tamanho)
    pop_matrix()

def galho(tamanho):
    angulo = radians(graus)
    angulo = angulo - random(-1, 1) / 10
    reduz = 0.85 # reduz 15%
    stroke_weight(tamanho / 20)
    stroke(0)  # liga traço preto
    line(0, 0, 0, -tamanho)
    if tamanho > 10:
        reduz = reduz - random(1) / 10
        push_matrix()  # backup das coordenadas
        translate(0, -tamanho)
        rotate(angulo)
        galho(tamanho * reduz)
        rotate(-2 * angulo)
        galho(tamanho * reduz)
        pop_matrix()  # volta coordenadas salvas
    else:
        fill(255)
        no_stroke() # desliga o traço
        circle(0, -tamanho, 4)