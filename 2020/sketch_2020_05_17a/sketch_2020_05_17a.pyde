arrastando = -1  # -1 quer dizer nenhum círculo sendo arrastado
formas = []  # lista com coordenadas e tamanhos dos círculos
NUM_FORMAS = 5

def setup():
    size(400, 400)
    colorMode(HSB)
    rectMode(CENTER)
    noFill()
    sorteia_formas(NUM_FORMAS)

def draw():
    background(200),
    # Queremos uma lista invertida da enumeração dos círculo
    i_formas = list(enumerate(formas))[::-1]
    # De forma a desenhar a lista do último para o primeiro
    for i, forma in i_formas:  
        xb, yb, db = forma
        xa, ya, da = formas[i - 1]
        xc, yc, dc = formas[(i + 1) % len(formas)]
        
        a1 = atan2(xa - xb, yb - ya)
        a2 = atan2(xb - xc, yc - yb)
        if a1 < 0: a1 = a1 + TWO_PI        
        if a2 < 0: a2 = a2 + TWO_PI
        f_line(xa, ya, da, xb, yb, db, a1, a2)

def f_line(xa, ya, da, xb, yb, db, a1, a2):
        d = dist(xa, ya, xb, yb)
        n = 5 * int(d / min(da, db))
        for t in range(n):
            tc = t / float(n)
            xc = lerp(xa, xb, tc)
            yc= lerp(ya, yb, tc)
            dc= lerp(da, db, tc)
            a = lerp(a1, a2, tc)
            stroke(0)
            with pushMatrix():
                translate(xc, yc)
                rotate(a)
                rect(0, 0, dc, dc)

def keyPressed():
    if key == ' ':
        sorteia_formas(NUM_FORMAS)

def mousePressed():  # quando um botão do mouse é apertado
    global arrastando
    for i, forma in enumerate(formas):
        x, y, d = forma
        dist_mouse_forma = dist(mouseX, mouseY, x, y)
        raio = d / 2
        if  dist_mouse_forma < raio:
            arrastando = i
            break  # encerra o laço
    
def mouseReleased():  # quando um botão do mouse é solto
    global arrastando
    arrastando = -1
    
def mouseDragged():  # quando o mouse é movido apertado
    if arrastando >= 0:
        x, y, d = formas[arrastando]
        x += mouseX - pmouseX
        y += mouseY - pmouseY
        formas[arrastando] = (x, y, d)
        
def mouseWheel(event):
    movimento_roda = event.getCount()
    for i, forma in enumerate(formas):
        x, y, d = forma
        dist_mouse_forma = dist(mouseX, mouseY, x, y)
        raio = d / 2
        if  dist_mouse_forma < raio:
            d += movimento_roda
            # Limitar o tamanho possível dos círculos
            if 15 < d < 270:
                formas[i] = (x, y, d)
            # sem `break` todos sob o mouse seriam afetados
            break  # interrompe o laço `for` 
        
def sorteia_formas(num):
    formas[:] = []  # esvazia a lista
    for _ in range(num):  # vamos sortear `num` círculos
        d = 40
        x = random(d / 2, width - d / 2)
        y = random(d / 2, height - d / 2)
        formas.append((x, y, d))
