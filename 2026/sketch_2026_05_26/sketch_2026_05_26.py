# This is a py5 "imported mode" sketch
# learn about py5 modes at https://py5coding.org

def setup():
    global frase_a, frase_b
    size(800, 800)
    
    regras_a = {
        'X': 'X[-FFF][+FFF]FX',
        'Y': 'YFX[+Y][-Y]',
    }
    axioma_a = 'Y'
    frase_a = gerar_frase(regras_a, axioma_a, 6)  # num de interações

    regras_b = {
        'X': 'X[-FFF][+FFF]FX',
        'F': 'FF',
    }
    axioma_b = 'X'
    frase_b = gerar_frase(regras_b, axioma_b, 6)  # num de interações


def gerar_frase(regras, axioma, num_iteracoes):
    frase_inicial = axioma
    for i in range(num_iteracoes):
        frase_resultado = ''
        for simbolo in frase_inicial:
            frase_resultado = frase_resultado + regras.get(simbolo, simbolo)
        frase_inicial = frase_resultado
    return frase_resultado
    
def draw():
    background(250, 250, 220)
    desenha_frase(200, 700, frase_a, angulo=45, passo=4)
    desenha_frase(400, 700, frase_a, angulo=25, passo=2)
    desenha_frase(600, 700, frase_b, angulo=30, passo=2)

def desenha_frase(x, y, frase, angulo, passo):
    push_matrix()
    translate(x, y)
    for simbolo in frase:
        if simbolo == 'F':
            line(0, 0, 0, -passo)
            translate(0, -passo)
        elif simbolo == '-':
            rotate(radians(angulo))
        elif simbolo == '+':
            rotate(radians(-angulo))
        elif simbolo == '[':
            push_matrix()  # põe na pilha a posição e o ângulo da caneta
        elif simbolo == ']':
            pop_matrix()   # restaura o último estado salvo na pilha
    pop_matrix()

def key_pressed():
    save_frame('###.png')

