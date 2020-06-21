nome = "clique na janela para mudar o texto"

def setup():
    size(400, 400)
    textAlign(CENTER, CENTER)
    
def draw():
    background(0, 0, 200)
    text(nome, width / 2, height / 2)
    
def mousePressed():
    global nome
    resposta = input('escreva um novo texto')
    if resposta:
        nome = resposta
    elif resposta == "":
        println("[resposta vazia]")
    else:
        println(resposta) # se diálogo cancelado imprime `None`

def input(message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)
