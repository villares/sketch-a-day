angulo = radians(22)

def setup():
    size(500, 500)

def draw():
    random_seed(1)
    background(240, 240, 200)
    translate(250, 300)  # desloca a origem, o 0,0 das coordenadas
    galho(60)

def galho(tamanho):
    stroke_weight(tamanho / 8)
    line(0, 0, 0, -tamanho)
    encurtamento = 0.9 - random(0.3)
    if tamanho > 5:
        a = angulo + (random(2) - 1) / 6
        b = angulo + (random(2) - 1) / 6
        push_matrix()  # uma maneira de salvar o estado atual das coordenadas, usado em conjunto com `pop_matrix()`
        translate(0, -tamanho)
        rotate(a)
        galho(tamanho * encurtamento)
        rotate(-a * 2)
        galho(tamanho * encurtamento)
        pop_matrix()  # retoma o estado do sistema de coordenadas salvo por `push_matrix()`