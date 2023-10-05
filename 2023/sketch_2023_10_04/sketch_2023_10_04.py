axioma = 'X'
regras = {
    'X': 'F+[[-X]+X]-F[[+X]-X]',
    'F': 'FF',
    }
passo = 5
angulo = 25  # angulo em graus
iteracoes = 6

def setup():
    global frase_resultado
    size(600, 800, P3D)
    frase_inicial=axioma
    for _ in range(iteracoes):
        frase_resultado = ''
        for simbolo in frase_inicial:
            substituir = regras.get(simbolo, simbolo)
            frase_resultado = frase_resultado + substituir
        # print(frase_inicial, frase_resultado)
        frase_inicial=frase_resultado
    print(len(frase_resultado))

def draw():
    background(210, 210, 150)
    stroke_weight(3)
    angulo = 25
    # angulo = mouse_x / 70.0
    translate(width / 2, height * 0.9)
    rotate_y(frame_count / 20.0)
    for i, simbolo in enumerate(frase_resultado):
        if simbolo == 'X':   # se simbolo for igual a 'X'
            pass
        elif simbolo == 'F':   # else if (senão se) o simbolo é F
                stroke(i % 255)
                line(0, 0, 0, -passo)
                translate(0, -passo)
                rotate_y(radians(-angulo))
        elif simbolo == '+':
            rotate(radians(-angulo))  # + random(-5, 5)))
        elif simbolo == '-':
            rotate(radians(+angulo))  # + random(-5, 5)))
        elif simbolo == '[':
            push_matrix()
        elif simbolo == ']':
            pop_matrix()

