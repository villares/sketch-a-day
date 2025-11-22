import py5_tools

axioma = 'F'
regras = {
    #'X': 'F+[[X]-X]-F[-FX]+X',
    'F': ' FF+[+F-F-F0]-[-F+F+F0]',
    }
angulo = 22.5
passo = 20
num_iter = 3
gravando = False
animar = 0

def setup():
    size(600, 600)
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
    global gravando, angulo, animar
    if animar:
        angulo = animar
        animar = animar + 1
    if gravando:
        begin_record(PDF, f'Moita-{angulo}-{passo}.pdf')        
    background(240, 250, 250)
    translate(300, 600)
    for simbolo in resultado:
        if simbolo == 'F':
            stroke(0)
            line(0, 0, 0, -passo)
            translate(0, -passo)
        elif simbolo == '-':
            rotate(radians(angulo))
        elif simbolo == '+':
            rotate(radians(-angulo))
        elif simbolo == '[':
            push_matrix()
        elif simbolo == ']':
            pop_matrix()
        elif simbolo == '0':
            no_stroke()
            fill(random(255), random(255), random(255))
            circle(0, 0, passo * 0.5)
   
    if gravando:
        end_record()
        gravando = False
        print('fim da gravação do PDF.')
   
def key_pressed():  # esperada pelo framework/biblioteca
    # executada quando alguém aperta uma tecla
    global angulo, passo, gravando, num_iter, animar
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
    elif key == 'g':
        gravando = True
        return
    elif key == 'm':
        global animar
        animar = 1
        py5_tools.animated_gif(
            'out.gif',
            frame_numbers=range(frame_count + 1,
                                frame_count+362, 5),
            duration=0.15,
            )
    
    print(f'ângulo: {angulo} passo: {passo}')
        
   

