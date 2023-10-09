axioma = 'X'
regras = {
    'X': '[-X][+X][+FX]-FXB',
    'F': 'FF',
    }
passo = 9
angulo = 25  # angulo em graus
iteracoes = 6

def setup():
    global frase_resultado
    size(800, 800)
    frase_inicial=axioma
    for _ in range(iteracoes):
        frase_resultado = ''
        for simbolo in frase_inicial:
            substituir = regras.get(simbolo, simbolo)
            frase_resultado = frase_resultado + substituir
        # print(frase_inicial, frase_resultado)
        frase_inicial=frase_resultado
    print(len(frase_resultado))

#def draw():
    background(210, 210, 150)
    stroke_weight(3)
    translate(width / 2, height * 0.9)
    for i, simbolo in enumerate(frase_resultado):
        if simbolo == 'X':   # se simbolo for igual a 'X'
            pass
        elif simbolo == 'F':   # else if (senão se) o simbolo é F
                stroke(i % 255)
                line(0, 0, 0, -passo)
                translate(0, -passo)
        elif simbolo == 'B':
            no_stroke()
            fill(0, 0, 100)
            circle(0, 0, passo)
        elif simbolo == '+':
            rotate(radians(-angulo))  # + random(-5, 5)))
        elif simbolo == '-':
            rotate(radians(+angulo))  # + random(-5, 5)))
        elif simbolo == '[':
            push_matrix()
        elif simbolo == ']':
            pop_matrix()

    save(f'{__file__[:-3]}.png')
