from __future__ import division
retangulos = []

def setup():
    size(600, 600)
    grade(0, 0, 600, 600, 4, 4) 
    
def draw():
    background(200)
    for r in retangulos:
        x, y, w, h = r
        if mouse_over(x, y, w, h):
            fill(0, 0, 200, 100)
        else:
            fill(128, 100)
        rect(x, y, w, h)
def mouse_over(x, y, w, h):
    return (x < mouseX < x + w and
            y < mouseY < y + h) # True/False

def mousePressed():
    global arrastando
    for i, (x, y, w, h) in enumerate(retangulos): 
        if mouse_over(x, y, w, h):
           arrastando = i  

def mouseReleased():
    global arrastando
    arrastando = None
                                        
def mouseDragged():
    if arrastando != None:
        dx = mouseX - pmouseX
        dy = mouseY - pmouseY
        x, y, w, h = retangulos[arrastando]
        retangulos[arrastando] = (x + dx, y + dy, w, h)

def grade(xo, yo, largura_total, altura_total, colunas, filas):
    largura_celula = largura_total / colunas
    altura_celula = altura_total / filas
    for i in range(colunas):
        x = xo + largura_celula * i
        for j in range(filas):
            y = yo + altura_celula * j
            # fill(i * 64, j * 64, 128)
            if largura_celula > 10 and random(10) > 5:
                grade(x, y, largura_celula, altura_celula, 4, 4)
            else:
                # rect(x, y, largura_celula, altura_celula)
                retangulos.append((x, y, largura_celula, altura_celula))
            
