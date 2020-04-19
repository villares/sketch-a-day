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
    global estado_botoes
    try:
        estado_botoes
    except NameError:
        estado_botoes = dict()
    
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
            estado_botoes[(x, y)] = True
            return False
        elif estado_botoes.get((x, y)):
            estado_botoes[(x, y)] = False
            return True    
    estado_botoes[(x, y)] = False
    return False
