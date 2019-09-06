
def setup():
    size(500, 500)
    strokeWeight(3)
    setup_sorteio()

def setup_sorteio():
    global iniciais, finais, cores
    iniciais = sorteia_linhas(10)
    finais = sorteia_linhas(10)
    cores = sorteia_linhas(10)

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
    t = 1 + sin(frameCount / 100.)
    for li, lf, c in zip(iniciais, finais, cores):
        l = [lerp(a, b, t) for a, b in zip(li, lf)]
        stroke(c[0]/2, c[1]/2, c[2]/2)
        seta(*l)
    move(iniciais)
    move(finais)

def move(l):
    for i, li in enumerate(l):
        x1, y1, x2, y2 = li
        a = atan2(x2 - x1, y1 - y2)
        d = dist(x2, y2, width/2, height/2)
        if d > width: 
            step = -width
        else:
            step = 1
        v = PVector.fromAngle(a - HALF_PI) * step
        l[i] = (x1 + v.x, y1 + v.y,
                x2 + v.x, y2 + v.y)

def seta(x1, y1, x2, y2):
    L = dist(x1, y1, x2, y2)
    angle = atan2(x1 - x2, y2 - y1)
    pushMatrix()
    translate(x1, y1)
    rotate(angle)
    l = L / 10.
    strokeWeight(1 + l / 5.)
    line(0, 0, 0, L)
    line(0, L, 0 - l, L - l)
    line(0, L, 0 + l, L - l)
    popMatrix()

def keyPressed():
    if key == " ":
        setup_sorteio()
    if keyCode == UP:
        move(iniciais)
        move(finais)
    if key == "s":
        saveFrame("####.png")
