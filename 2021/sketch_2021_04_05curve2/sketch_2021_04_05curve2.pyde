arrastando = None 
pontos = [
    (100, 50),   # 0: âncora inicial       
    (150, 150),  # 1: primeiro ponto de controle
    (250, 100),  # 2: segundo ponto de controle
    (250, 200),  # 3: ponto final da primeira curva, âncora da segund
    (150, 250),
    (50, 200),
    (50, 100),
    ]  

def setup():
    size(300, 300)

def draw():
    background(100)
    strokeWeight(3)
    stroke(0)
    noFill()
    beginShape()
    vertex(pontos[0][0], pontos[0][1])
    bezierVertex(pontos[1][0], pontos[1][1],
                 pontos[2][0], pontos[2][1],
                 pontos[3][0], pontos[3][1])
    bezierVertex(pontos[4][0], pontos[4][1],
                 pontos[5][0], pontos[5][1],
                 pontos[6][0], pontos[6][1])
    endShape(),
    strokeWeight(1)
    for i, ponto in enumerate(pontos):
        x, y = ponto
        if i == arrastando:
            fill(200, 0, 0)
        else:
            fill(255)   
        ellipse(x, y, 5, 5)
        text("{}: {}, {}".format(i, x, y), x + 5, y - 5)

def mousePressed():  # quando um botão do mouse é apertado
    global arrastando
    for i, ponto in enumerate(pontos):
        x, y = ponto
        dist_mouse_ponto = dist(mouseX, mouseY, x, y)
        if  dist_mouse_ponto < 10:
            arrastando = i
            break  # encerra o laço
    
def mouseReleased():  # quando um botão do mouse é solto
    global arrastando
    arrastando = None
    
def mouseDragged():  # quando o mouse é movido apertado
    if arrastando is not None:
        x, y = pontos[arrastando]
        x += mouseX - pmouseX
        y += mouseY - pmouseY
        pontos[arrastando] = (x, y)
        
def keyPressed():
    saveFrame("curve_smooth.png")
