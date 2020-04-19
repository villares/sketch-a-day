estado_inicial = True

def setup():
    size(400, 400)
    
def draw():
    background(200)
    global estado_inicial
    if estado_inicial:
        botao_apertado = botao(100, 100, 200, 50, "clique aqui")
        if botao_apertado:
            print('clique')
            # saveFrame('sketch_2020_04_18a.png')
            estado_inicial = not estado_inicial
    else:
        botao_apertado = botao(100, 250, 200, 50, "de novo!")
        if botao_apertado:
            print('clique')
            estado_inicial = not estado_inicial
    
    
            
                                    
def botao(x, y, w, h, _text):
    global _apertado
    mouse_over = (x < mouseX < x + w and
                  y < mouseY < y + h)
    if mouse_over:
        fill(140)
    else:
        fill(240)
    rect(x, y, w, h, 5)
    fill(0)
    textAlign(CENTER, CENTER) 
    text(_text, x + w / 2, y + h / 2)
    if mouse_over and mousePressed:
        _apertado = True
        return False
    else:
        _apertado = False
        
    if mouse_over and _apertado:
        return True
    return False
