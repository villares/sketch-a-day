arrastando = -1  # -1 quer dizer nenhum círculo sendo arrastado
circulos = []  # lista com coordenadas e tamanhos dos círculos
NUM_CIRCULOS = 5

def setup():
    size(400, 400)
    strokeWeight(3)
    colorMode(HSB)
    noFill()
    sorteia_circulos(NUM_CIRCULOS)

def draw():
    background(200)
    # Queremos uma lista invertida da enumeração dos círculo
    i_circulos = list(enumerate(circulos))[::-1]
    # De forma a desenhar a lista do último para o primeiro
    for i, circulo in i_circulos:  
        xa, ya, da = circulo
        xb, yb, db = circulos[i - 1]
        ca = color(da - 15, 255, 255, 200)
        cb = color(db - 15, 255, 255, 200)
        n = 36
        for t in range(n):
            tc = t / float(n)
            xc = lerp(xa, xb, tc)
            yc= lerp(ya, yb, tc)
            dc= db + da * sin(t * TWO_PI / n)
            cc = lerpColor(ca, cb, tc)        
            stroke(0)
            if i == arrastando and t == 0:
                stroke(255)
            ellipse(xc, yc, dc, dc)

def keyPressed():
    if key == ' ':
        sorteia_circulos(NUM_CIRCULOS)

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
        
def mouseWheel(event):
    movimento_roda = event.getCount()
    for i, circulo in enumerate(circulos):
        x, y, d = circulo
        dist_mouse_circulo = dist(mouseX, mouseY, x, y)
        raio = d / 2
        if  dist_mouse_circulo < raio:
            d += movimento_roda
            # Limitar o tamanho possível dos círculos
            if 15 < d < 270:
                circulos[i] = (x, y, d)
            # sem `break` todos sob o mouse seriam afetados
            break  # interrompe o laço `for` 
        
def sorteia_circulos(num):
    circulos[:] = []  # esvazia a lista
    for _ in range(num):  # vamos sortear `num` círculos
        d = 40
        x = random(d / 2, width - d / 2)
        y = random(d / 2, height - d / 2)
        circulos.append((x, y, d))
