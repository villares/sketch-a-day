axioma = 'X'
regras = {
    'X': 'F+[[X]-X]-F[-FX]+X',
    'F': 'S',  
    'S': 'SF'    
    }
passo = 15
angulo = 25 # angulo em graus
iteracoes = 5

def setup():
    global frase_resultado
    size(600, 600, P3D)
    strokeWeight(2)
    frase_inicial = axioma
    for _ in range(iteracoes):
        frase_resultado = ''
        for simbolo in frase_inicial:
            substituir = regras.get(simbolo, simbolo)
            frase_resultado = frase_resultado + substituir
        #print(frase_inicial, frase_resultado)
        frase_inicial = frase_resultado    
    print(len(frase_resultado))
    
def draw():
    background(200, 200, 150)
    angulo = 25
    translate(width / 2, height * 0.95)
    rotateY(frameCount / 100.0)
    for simbolo in frase_resultado:
        if simbolo == 'X':   # se simbolo for igual a 'X'
            pass
        elif simbolo in 'FS':   # else if (senão se) o simbolo é F
                line(0, 0, 0, -passo)
                translate(0, -passo)
                rotateY(radians(-angulo))
        elif simbolo == '+':
            rotate(radians(-angulo)) # + random(-5, 5)))
        elif simbolo == '-':
            rotate(radians(+angulo)) # + random(-5, 5)))
        elif simbolo == '[':
            pushMatrix()
        elif simbolo == ']':
            popMatrix()

                
    
    
    
    
