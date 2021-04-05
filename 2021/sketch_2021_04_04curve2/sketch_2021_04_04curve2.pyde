arrastando = None 
pontos = [
    (100, 50),          
    (150, 100),
    (250, 100),
    (250, 200),
    (150, 200),
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
    curveVertex(pontos[-1][0], pontos[-1][1])
    for x, y in pontos:
        curveVertex(x, y)
    curveVertex(pontos[0][0], pontos[0][1])
    endShape(CLOSE)
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
