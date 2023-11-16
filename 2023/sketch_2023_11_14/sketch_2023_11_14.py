regras = {
    'X': 'F+[![X]-X!]-F[-FX]+X',
    'F': 'FGF',
    }
axioma = 'X'
iteracoes = 6
angulo = 25
tamanho = 2

def setup():
    global nova_frase
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
    for simbolo in nova_frase:
        if simbolo == 'F':
            stroke_weight(1)
            stroke(0)  # traço preto
            line(0, 0, 0,-tamanho)
            translate(0,-tamanho)
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
        elif simbolo == 'X':
            stroke_weight(tamanho)
            stroke(255, 0 , 0)  # RGB
            point(0, 0)

def key_pressed():
    save('out.png')