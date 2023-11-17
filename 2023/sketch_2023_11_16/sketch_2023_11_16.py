regras = {
    'X': 'FG[X[+X]-X]',
    'F': 'FF',
    }
axioma = 'X'
iteracoes = 8
angulo = 25
tamanho = 1.5
scale_factor = 1.05

def setup():
    global nova_frase
    #size(800, 800, P3D)
    size(800, 800)
    frase_inicial = axioma
    for n in range(iteracoes):  # repete 7 vezes
        nova_frase = ''
        for simbolo in frase_inicial:
            nova_frase = nova_frase + regras.get(simbolo, simbolo)
        frase_inicial = nova_frase
        print(len(nova_frase))
    
    
def draw():
    global angulo
    background(200, 240, 240)
    translate(400, 700)
    #rotate_y(radians(mouse_x))
    for simbolo in nova_frase:
        if simbolo == 'F':
            stroke_weight(1)
            stroke(0)  # traço preto
            line(0, 0, 0,-tamanho)
            translate(0,-tamanho)
            #rotate_y(HALF_PI / 18)
        elif simbolo == 'G':
            translate(0,-tamanho)
        elif simbolo == '+':
            rotate(radians(-angulo))
        elif simbolo == '-':
            rotate(radians(angulo))
        elif simbolo == '!':
            angulo = -angulo
        elif simbolo == '[':
            push_matrix()
        elif simbolo == ']':
            pop_matrix()
        elif simbolo == '@':
            scale(scale_factor)
#             stroke_weight(tamanho)
#             stroke(0, 200 , 0)  # RGB
#             point(0, 0)
        elif simbolo == 'X':
            stroke_weight(tamanho)
            stroke(255, 200 , 0)  # RGB
            point(0, 0)

def key_pressed():
    save('out.png')