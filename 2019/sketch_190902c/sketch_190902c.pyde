
def setup():
    size(500, 500)
    strokeWeight(3)
    setup_sorteio()
    
def setup_sorteio():
    global iniciais, finais
    iniciais = sorteia_linhas(10)
    finais = sorteia_linhas(10)
    
def sorteia_linhas(num):
    linhas = []
    for _ in range(num):
        margem = 50
        x1 = random(margem, width - margem)
        y1 = random(margem, height - margem)
        x2 = random(margem, width - margem)
        y2 = random(margem, height - margem)
        linha = (x1, y1, x2, y2)
        linhas.append(linha)
    return linhas 

def draw():
    background(255)
    t = map(mouseX, 0, width, 0, 1)
    for li, lf in zip(iniciais, finais):
        l = [lerp (a, b, t) for a, b in zip(li, lf)]
        seta(*l)


def seta(x1, y1, x2, y2):
    L = dist(x1, y1, x2, y2)
    angle = atan2(x1 - x2, y2 - y1)
    pushMatrix()
    translate(x1, y1)
    rotate(angle)
    line(0, 0, 0, L)
    l = L / 10
    line(0, L, 0 - l, L - l)
    line(0, L, 0 + l, L - l)
    popMatrix()
    
def keyPressed():
    if key == " ":
        setup_sorteio()
    if key == "s":
        saveFrame("####.png")
        
