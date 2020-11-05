"""
    Here, F means "draw forward", − means "turn right 25°",
    and + means "turn left 25°". X does not correspond to any drawing
    action and is used to control the evolution of the curve.]
    The square bracket "[" corresponds to saving the current values for 
    position and angle, which are restored when the corresponding "]" 
    is executed.
"""
axioma = "X"
regras = {"X" : "F+[[X]-X]-F[-FX]+X",
          "F" : "FF",
          }
n = 6  # numero de iterações (repetições)
angulo = radians(25)
tam_linha = 3
xo, yo = 450, 550  # posição inicial

# OUTRA REGRA
# axioma = "A"
# regras = {'A': 'B-A-B',
#           'B': 'A+B+A',
#           }
# n = 7  # numero de iterações (repetições)
# angulo = radians(60)
# tam_linha = 5
# xo, yo = 600, 550  # posição inicial


def setup():
    global frase_atual
    size(700, 700)
    colorMode(HSB)
    
    frase_atual = axioma
    for _ in range(n):
        frase_nova = ""
        for letra in frase_atual:
            frase_nova += regras.get(letra, letra)
        frase_atual = frase_nova

def draw():
    background(0)
    translate(xo, yo)
    desenha_frase(frase_atual)

def desenha_frase(frase):
    for i, letra in enumerate(frase):
        if letra in "ABF": #  Tanto A como B e F andam e desenham
            stroke((i / 100.) % 256, 255, 255)
            line(0, 0, 0, -tam_linha)
            translate(0, -tam_linha)
        elif letra == "+":
            rotate(angulo + i / 10000.)
        elif letra == "-":
            rotate(-angulo - i / 10000.)
        if letra == "[":
            pushMatrix()
        if letra == "]":
            popMatrix()
            
def keyPressed():
    global angulo, xo, yo, tam_linha
    if str(key) in '-z':
        angulo -= radians(1)
        print(degrees(angulo))
    if str(key) in "=+a":
        angulo += radians(1)
        print(degrees(angulo))
    if key == 's':
        tam_linha *= 2
    if key == 'x':
        tam_linha /= 2
    if keyCode == LEFT:
        xo -= 25
    if keyCode == RIGHT:
        xo += 25
    if keyCode == UP:
        yo -= 25
    if keyCode == DOWN:
        yo += 25
