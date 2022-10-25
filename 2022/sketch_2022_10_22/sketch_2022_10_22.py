s = 0

def setup():
    size(600, 600)

def draw(): # laço/loop principal (ele fica repetindo)
    background(230, 230, 250)
    random_seed(s)
    translate(300, 390) # muda a origem
    galho(120)
    
def galho(tamanho):
    angulo = radians(2 * tamanho) # 30 graus em radianos
    line(0, 0, 0, -tamanho) #x1, y1, x2, y2
    encurtar = 0.8 # reduz 20% quando multiplica
    if tamanho > 5:
        push_matrix()
        translate(0, -tamanho)
        rotate(angulo) # + random(-0.2, 0.2))
        galho(tamanho * encurtar - random(1, 3))
        rotate(angulo * -2) 
        galho(tamanho * encurtar - random(1, 3))
        pop_matrix()
    
def key_pressed():
    global s
    if key == ' ':
        s += 1
  
