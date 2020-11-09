
from formas import Quadrado # do arquivo formas.py traga a classe Quadrado

def setup():
    global quadrados
    size(500, 500)    
    quadrados = []    # lista vazia esperando quadrados
    for i in range(100):
        # repetição para invetar obj da classe Quadrado
        # sorteio da posição x: random(width)
        lado = random(10, 50)
        x = random(0, width - lado)
        y = random(0, height - lado) # para não cair para fora da tela 
        novo_quadrado = Quadrado(x, y, lado)  # instanciando um novo Quadrado
        quadrados.append(novo_quadrado)   # acrescentando o novo q na lista
        
def draw():
    background(0)  
    # andando pela lista de quadrados um por um
    for q in quadrados:
        # pedindo pro quadrado se autodesenhar
        q.desenha()         
    # if keyPressed:
    for q in quadrados:
            q.corra()
          
def mouseDragged():   # executado no arraste do mouse
    for q in quadrados:
        if q.mouse_over():    
            dx = mouseX - pmouseX
            dy = mouseY - pmouseY
            q.mova(dx, dy)
