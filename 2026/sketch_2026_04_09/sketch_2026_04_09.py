# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org
import py5
from py5_tools import animated_gif

axioma = 'F'
regras = {"F":  "FF[+F-F0][-F+F0]"}

passo = 10
angulo = 30  # graus
iteracoes = 4


def setup():
    py5.size(600, 600, py5.P3D)
    py5.color_mode(py5.CMAP, 'viridis', 255)
    calcular_frase()
    animated_gif('out.gif', duration=9/60, frame_numbers=range(1, 361, 9))
    
def calcular_frase():
    global frase_resultado
    frase_inicial = axioma
    for i in range(iteracoes):
        frase_resultado = ''
        for simbolo in frase_inicial:
            frase_resultado += regras.get(simbolo, simbolo)
        frase_inicial = frase_resultado
    print(len(frase_resultado))
    print('+', frase_resultado.count('+'))
    print('-', frase_resultado.count('-'))
        
def draw():
    py5.background('white')
    py5.translate(300, 550)
    py5.rotate_y(py5.radians(py5.frame_count))
    contador = 0
    pilha_contador = []
    for simbolo in frase_resultado:
        if simbolo == 'F':
            py5.stroke(contador % 256)  
            py5.line(0, 0, 0, -passo)
            py5.rotate_y(py5.radians(angulo))
            py5.translate(0, -passo)
            contador += 1
        elif simbolo == '-':
            py5.rotate(py5.radians(angulo))
        elif simbolo == '+':
            py5.rotate(py5.radians(-angulo))
        elif simbolo == '[':
            py5.push_matrix()
            pilha_contador.append(contador)
        elif simbolo == ']':
            py5.pop_matrix()
            contador = pilha_contador.pop()
        elif simbolo == '0':
            py5.push_style()
            py5.no_stroke()
            py5.fill('red')
            py5.circle(0, 0, passo / 3)
            py5.pop_style()
            
def key_pressed():
    global angulo, passo
    if py5.key == 'a':
        angulo += 1
    elif py5.key == 'z':
        angulo -= 1
    if py5.key == 's':
        passo *= 1.1
    elif py5.key == 'x':
        passo /= 1.1
    print(angulo, passo)
        


py5.run_sketch(block=False)
