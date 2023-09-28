from villares.helpers import save_png_with_src

seed = 1
graus = 15
numero = 6
angle_off = 0

def setup():
    size(900, 900)
    #frame_rate(1)
    
def draw():
    background(200)
    random_seed(seed)
    arvore(width / 2, height / 2, 80, numero)
                    
def arvore(x, y, tamanho, num):
    step = TWO_PI / num
    push_matrix()
    translate(x, y)
    for i in range(num):
        rotate(step)
        galho(tamanho)
    pop_matrix()

def galho(tamanho):
    angulo = radians(graus)
    angulo = angulo - random(-1, 1)   / 10
    reduz = 0.85 # reduz 15%
    stroke_weight(tamanho / 20)
    stroke(0)  # liga traço preto
    line(0, 0, 0, -tamanho)
    if tamanho > 10:
        reduz = reduz - random(1) / 10
        push_matrix()  # backup das coordenadas
        translate(0, -tamanho)
        rotate(angulo + angle_off / 10)
        galho(tamanho * reduz)
        rotate(-2 * angulo + angle_off / 10)
        galho(tamanho * reduz)
        pop_matrix()  # volta coordenadas salvas
    else:
        fill(255)
        no_stroke() # desliga o traço
        circle(0, -tamanho, 4)
        
def key_pressed():
    global numero, graus, angle_off
    if key == 'a':
        numero += 1
    if key == 'z' and numero > 1:
        numero -= 1
    if key == 's':
        graus += 1
    if key == 'x':
        graus -= 1
    if key == 'd':
        angle_off += 1
    if key == 'c':
        angle_off -= 1
        
    if key == 'p':
        save_png_with_src()
    if key == 'o':
        global seed
        seed = seed + 1
    print(seed)

        
        