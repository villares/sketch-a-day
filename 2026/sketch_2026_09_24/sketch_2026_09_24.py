import py5
from py5_tools import animated_gif

regras = {
    'X': 'X[-FFFL][+FFFL]FFX',
    'Y': 'YFFX[+YFFFB][-YFFFB]',
}
axioma = 'Y'
passo = 5
angulo = 30
iteracoes = 5

def setup():
    global frase
    py5.size(600, 600)  # área de desenho
#     animated_gif('out.gif',
#                  frame_numbers=range(1, 200, 3),
#                  duration=0.1)
        
    frase_inicial = axioma
    for i in range(iteracoes):
        frase = ''
        for simbolo in frase_inicial:
            frase = frase + regras.get(simbolo, simbolo)
        frase_inicial = frase


def draw():
    py5.background(240, 250, 200)
    py5.translate(300, 590)
    #circle(0, 0, 20)
    for i, simbolo in enumerate(frase):
        if i < py5.frame_count * 30:
            flag = True
        else:
            flag = False
        if simbolo == 'F':
            if flag:
                py5.line(0, 0, 0, -passo)
            py5.translate(0, -passo)
        elif simbolo == '+':
            py5.rotate(py5.radians(-angulo))
        elif simbolo == '-':
            py5.rotate(py5.radians(angulo))
        elif simbolo == '[':
            py5.push_matrix()
        elif simbolo == ']':
            py5.pop_matrix()
        elif simbolo == 'L':  # folha/leaf
            if flag:
                py5.no_stroke()
                py5.fill(0, 100, 0)
                py5.circle(0, 0, passo)
                py5.stroke(0)
        elif simbolo == 'B':  # flor/blossom
            if flag:
                py5.no_stroke()
                py5.fill(255, 0, 0)
                py5.circle(0, 0, passo * 1.5)
                py5.stroke(0)
    py5.reset_matrix()
    


py5.run_sketch()
