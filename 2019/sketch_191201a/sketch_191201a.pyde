
pontos = []
novos_pontos = []
arrastando = -1
offset_curva = 10

def setup():
    size(500, 500)
    novos_pontos[:] = pontos[:] = sorteia_pontos()

def sorteia_pontos():
    pontos = []
    for _ in range(5):
        x, y = random(width * .2, width * .8), random(height * .2, height * .8)
        pontos.append((x, y))
    return pontos

def draw():
    background(240, 250, 250)
    for i, (x0, y0) in enumerate(pontos):
        x1, y1 = pontos[i - 1]
        noFill()
        stroke(0)
        strokeWeight(2)
        curva(x0, y0, x1, y1)
        if dist(mouseX, mouseY, x0, y0) < 10:
            stroke(255, 0, 0)
        strokeWeight(1)
        circle(x0, y0, 10)
        
    for i, (x0, y0) in enumerate(pontos):
        x1, y1 = novos_pontos[i]
        if (x0, y0) != (x1, y1):
            pontos[i] = ((x0 + x1) / 2, (y0 + y1) / 2)

def curva(x1, y1, x2, y2):
    L = dist(x1, y1, x2, y2)
    with pushMatrix():
        translate(x1, y1)
        angle = atan2(x1 - x2, y2 - y1)
        rotate(angle)
        cx = (L / 2) * offset_curva / 10.
        bezier(0, 0, -cx, L * .50, +cx, L * .50, 0, L)

def mousePressed():
    global arrastando
    for i, (x0, y0) in enumerate(pontos):
        if dist(mouseX, mouseY, x0, y0) < 10:
            arrastando = i

def mouseReleased():
    global arrastando
    arrastando = -1

def mouseDragged():
    if arrastando >= 0:
        novos_pontos[arrastando] = (mouseX, mouseY)
        
def mouseWheel(e):
    global offset_curva
    offset_curva += e.getCount() / 5.
    
def keyPressed():
    if key == ' ':
        novos_pontos[:] = sorteia_pontos()
    if key == 's':
        saveFrame("####.png")
