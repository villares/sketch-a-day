estado_inicial = True

def setup():
    size(400, 400)
    
def draw():
    global estado_inicial

    if estado_inicial:
        background(200)
    else:
        background(10)
        
    resultado1 = botao(100, 125, 200, 50, "clique aqui")
    resultado2 = botao(100, 225, 200, 50, "de novo!")
    if resultado1 or resultado2:
            print('clique')
            estado_inicial = not estado_inicial
                               
def botao(x, y, w, h, _text):    
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
    if mouse_over:
        if mousePressed:
            botao.__dict__[(x, y)] = True  # o botão foi apertado
            return False
        elif botao.__dict__.get((x, y)):   # o botão foi solto após estar apertado
            botao.__dict__.pop((x, y))
            return True
    botao.__dict__.pop((x, y))
    return False
