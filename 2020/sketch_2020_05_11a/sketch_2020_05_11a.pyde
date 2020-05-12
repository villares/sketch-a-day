arrastando = -1  # -1 quer dizer nenhum círculo sendo arrastado
circulos = []  # lista com coordenadas e tamanhos dos círculos

def setup():
    size(400, 400)
    strokeWeight(3)
    fill(0, 200) # preenchimento translúcido
    for _ in range(5):  # vamos sortear 5 círculos
        d = random(30, 100)
        x = random(d, width - d)
        y = random(d, height - d)
        circulos.append((x, y, d))

def draw():
    background(0, 0, 200)
    for i, circulo in enumerate(circulos):
        x, y, d = circulo
        if i == arrastando:
            stroke(200, 0, 0)
        else:
            stroke(255)    
        ellipse(x, y, d, d)

def mousePressed():  # quando um botão do mouse é apertado
    global arrastando
    for i, circulo in enumerate(circulos):
        x, y, d = circulo
        dist_mouse_circulo = dist(mouseX, mouseY, x, y)
        raio = d / 2
        if  dist_mouse_circulo < raio:
            arrastando = i
            break  # encerra o laço
    
def mouseReleased():  # quando um botão do mouse é solto
    global arrastando
    arrastando = -1
    
def mouseDragged():  # quando o mouse é movido apertado
    if arrastando >= 0:
        x, y, d = circulos[arrastando]
        x += mouseX - pmouseX
        y += mouseY - pmouseY
        circulos[arrastando] = (x, y, d)
    
