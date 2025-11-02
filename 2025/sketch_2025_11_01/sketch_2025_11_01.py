# This uses py5 in "imported mode" learn more at py5coding.org

from py5_tools import animated_gif

axioma = 'Y'
regras = {
    'X': 'X[-FF][+FF]FF0',
    'Y': 'YFFX[+YX][-YX]',
    }


passo = 2.5

def setup():
    global resultado
    size(600, 600)
    frase_inicial = axioma
    for i in range(7):
        resultado = ''
        for simbolo in frase_inicial:
            resultado = resultado + regras.get(simbolo, simbolo)
        frase_inicial = resultado
    print(len(resultado))
    animated_gif('out.gif', frame_numbers=range(1, 361, 10), duration=0.3)

    
def draw():
    background(200, 200, 240)
    translate(300, 550)
    angulo = 45 + 45 * cos(radians(frame_count))
    for simbolo in resultado:
        if simbolo == 'F':
            line(0, 0, 0, -passo)
            translate(0, -passo)
        if simbolo == '-':
            rotate(radians(angulo))
        if simbolo == '+':
            rotate(radians(-angulo))
        if simbolo == '[':
            push_matrix()
        if simbolo == ']':
            pop_matrix()
        if simbolo == '0':
            no_stroke()
            fill('red')
            circle(0, 0, passo * 2)
            stroke(0)
