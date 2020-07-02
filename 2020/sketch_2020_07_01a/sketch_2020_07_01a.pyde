arrastando = None 
pontos = [(-100,-100, 50),
          (100, -100, -50),
          (100, 100, 50),
          (-100, 100, 50)]  
tam = 10

def setup():
    size(300, 300, P3D)
    noFill()
    strokeWeight(3)
    
def draw():
    translate(width / 2, height / 2)
    rotateY(radians(frameCount))
    background(100)
    for i, ponto in enumerate(pontos):
        x, y, z = ponto
        if i == arrastando:
            stroke(200, 0, 0)
        else:
            stroke(255)    
        ellipse(x, y, tam, tam)

    for p in pontos:
        caixa(p[0], p[1], p[2], tam)

    stroke(0)
  # generalização
    line(pontos[0][0], pontos[0][1], pontos[0][2], 
         pontos[1][0], pontos[1][1], pontos[1][2])    
    beginShape()
    for i in range(len(pontos) + 3):
        curveVertex(pontos[i % len(pontos)][0],
                    pontos[i % len(pontos)][1],
                    pontos[i % len(pontos)][2])
    endShape()

def mousePressed():  # quando um botão do mouse é apertado
    global arrastando
    for i, ponto in enumerate(pontos):
        x, y, z = ponto
        mw, mh = width / 2, height / 2
        dist_mouse_ponto = dist(mouseX - mw, mouseY -mh,
                                 x, y)
        if  dist_mouse_ponto < tam:
            arrastando = i
            break  # encerra o laço
    
def mouseReleased():  # quando um botão do mouse é solto
    global arrastando
    arrastando = None
    
def mouseDragged():  # quando o mouse é movido apertado
    if arrastando is not None:
        x, y, z = pontos[arrastando]
        x += mouseX - pmouseX
        y += mouseY - pmouseY
        pontos[arrastando] = (x, y, z)
        

def caixa(x, y, z, w, h=None, d=None):
    h = h or w
    d = d or h
    pushMatrix()
    translate(x, y, z)
    box(w, h, d)
    popMatrix()
