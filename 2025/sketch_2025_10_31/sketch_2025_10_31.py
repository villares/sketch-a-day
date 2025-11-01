# This uses py5 in "imported mode" learn more at py5coding.org

from py5_tools import animated_gif
import shapely

axioma = 'Y'
regras = {
    'X': 'X[-FFFF][+FFFF]FX',
    'Y': 'YFFX[+Y][-Y]',
    }
passo = 3
angulo = 45 # graus

def setup():
    size(500, 500)
    stroke_weight(1)
    generate(6)
    #animated_gif('out.gif', frame_numbers=(1, 2, 3, 4, 5), duration=0.1)
    
def generate(n):
    global frase_resultado
    frase_inicial = axioma
    for i in range(n):
        frase_resultado = ''
        for simbolo in frase_inicial:
            frase_resultado = frase_resultado + regras.get(simbolo, simbolo)
        frase_inicial = frase_resultado
    print(len(frase_resultado))

def draw():
    background(240, 240, 200)
    translate(250, 450)
    shapes = []
    for simbolo in frase_resultado:
        ang = angulo #+ random(-1, 1)
        if simbolo == 'F':
            p = passo # + random(-0.5, 0.5)
            x0 = screen_x(0, 0)
            y0 = screen_y(0, 0)
            x1 = screen_x(0, -p)
            y1 = screen_y(0, -p)
            #line(0, 0, 0, -p)
            shapes.append(shapely.LineString(((x0, y0), (x1, y1))))
            translate(0, -p)
        elif simbolo == '-':
            rotate(radians(ang))
        elif simbolo == '+':
            rotate(radians(-ang))
        elif simbolo == '[':
            push_matrix()
        elif simbolo == ']':
            pop_matrix()
    translate(-250, -450/2)
    ls = shapely.MultiLineString(shapes)
    shape(ls.buffer(10))
    shape(ls)
    
def key_pressed():
    global angulo
    if key == 'a':
        angulo = angulo - 1
    if key == 'z':
        angulo = angulo + 1
        
