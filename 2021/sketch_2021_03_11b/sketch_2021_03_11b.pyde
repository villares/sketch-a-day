from random import randint, choice

AMARELO = color(200, 200, 100)
LARANJA = color(200, 100, 100)
VINHO = color(200, 100, 100)
VERDE = color(100, 200, 100)
AZUL = color(100, 100, 200)

cores = (AMARELO, LARANJA, VINHO, VERDE, AZUL)

def setup():
    size(800, 800)
    noStroke()
    rectMode(CENTER)
    noLoop()
    
def draw():
    # scale(1/8.0)
    translate(width / 2, height / 2)
    background(240)
    # for op in range(1, 8):
    #     fabrica_olhos(op)
    #     translate(width , 0)
    filas = [] 
    for _ in range(10):
        x, y  = 60 * randint(-3, 3), 60 * randint(-3, 3)
        r = randint(0, 3)
        s = randint(1, 5)
        c = choice(cores)
        filas.append((x, y, r, s, c))
        
    for x, y, r, s, c in filas:        
        fill(129, 100)
        fila(x, y, r, s * 1.05)
    filter(BLUR, 3)
        
    for x, y, r, s, c in filas:        
        fill(c)
        fila(x, y, r, s)
        
def fila(x, y, r, s):    
    push()
    rotate(HALF_PI * r)
    fila_horiz(5,  s * width / 24.0,
                   circle,
                   x, y, 
                   s * width / 28.0
                   )
    pop()
    
    
def fabrica_olhos(op):    
    """
    000 - não vai ter
    001 1- só menor
    010 2- só médio
    011 3- menor + medio
    100 4- só o grande
    101 5
    110 6
    111 7 
    """
    if op >= 4: # impar
        fill(AMARELO)
        olhos(width / 4.0)
    if op in (2, 3, 6, 7):
        fill(VINHO)
        olhos(width / 6.0)
    if op % 2 == 1: # impar
        fill(0)
        olhos(width / 12.0)

def olhos(tamanho):
    offset, altura = width / 4.0, width / 4.0
    circle(offset, -altura, tamanho)
    circle(-offset, -altura, tamanho)
    
def fila_horiz(num, espaco, func, *args):
    w = num * espaco
    pushMatrix()
    translate(-w / 2.0 + espaco / 2.0, 0)
    for _ in range(num):
        func(*args)
        translate(espaco, 0)
    popMatrix()
    
def keyPressed():
    redraw()
