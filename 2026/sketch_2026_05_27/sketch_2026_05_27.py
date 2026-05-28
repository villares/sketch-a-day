# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org

import py5

def setup():
    global frase_a, frase_b
    py5.size(800, 800)
    
    regras_a = {
        'X': 'X+[-FX]-[+FX]+FX',
        'F': 'FF',
    }
    axioma_a = 'X'
    frase_a = gerar_frase(regras_a, axioma_a, 6)  # num de interações

    regras_b = {
        'X': 'XF[-FX][+FX]FX',
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
    py5.background(250, 250, 220)
    desenha_frase(200, 500, frase_a, angulo=15, passo=5)
    desenha_frase(300, 700, frase_a, angulo=45, passo=5)
    desenha_frase(600, 700, frase_b, angulo=30, passo=1)

def desenha_frase(x, y, frase, angulo, passo):
    py5.push_matrix()
    py5.translate(x, y)
    for simbolo in frase:
        if simbolo == 'F':
            py5.line(0, 0, 0, -passo)
            py5.translate(0, -passo)
        elif simbolo == '-':
            py5.rotate(py5.radians(angulo))
        elif simbolo == '+':
            py5.rotate(py5.radians(-angulo))
        elif simbolo == '[':
            py5.push_matrix()  # põe na pilha a posição e o ângulo da caneta
        elif simbolo == ']':
            py5.pop_matrix()   # restaura o último estado salvo na pilha
    py5.pop_matrix()

def key_pressed():
    py5.save_frame('###.png')

py5.run_sketch()