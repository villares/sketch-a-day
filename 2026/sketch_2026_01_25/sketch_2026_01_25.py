import py5_tools

axioma = 'X'
regras = {
    'X': 'F+[[X0]-FX]-F[[X0]+FX]-X0',
    'F': 'FF',
    }
angulo = 22.5
passo = 8
num_iter = 5

def setup():
    size(800, 800)
    gerar_frase_resultado()
    
def gerar_frase_resultado():
    global resultado
    frase_inicial = axioma
    for i in range(num_iter):
        resultado = ''
        for simbolo in frase_inicial:
            resultado += regras.get(simbolo, simbolo)
        frase_inicial = resultado
    print(len(resultado))
    
def draw():
    background(240, 250, 240)
    translate(400, 800)
    a = angulo
    for simbolo in resultado:
        if simbolo == 'F':
            stroke(0)
            line(0, 0, 0, -passo)
            translate(0, -passo)
        elif simbolo == '>':
            a += 1
        elif simbolo == '<':
            a -= 1
        elif simbolo == '-':
            rotate(radians(a))
        elif simbolo == '+':
            rotate(radians(-a))
        elif simbolo == '[':
            push_matrix()
        elif simbolo == ']':
            pop_matrix()
        elif simbolo == '0':
            no_stroke()
            fill(128, 0, 128)
            circle(0, 0, passo * 0.5)
   
def key_pressed():  # esperada pelo framework/biblioteca
    # executada quando alguém aperta uma tecla
    global angulo, passo, num_iter
    if key == 'a':
        angulo += 1
    elif key == 'z':
        angulo -= 1
    elif key == 'd':
        num_iter += 1
        gerar_frase_resultado()
        return
    elif key == 'c':
        num_iter -= 1
        gerar_frase_resultado()
        return
    elif key == 's':
        passo *=  1.1
    elif key == 'x':
        passo /= 1.1
        
    print(f'ângulo: {angulo} passo: {passo}')
        
   
