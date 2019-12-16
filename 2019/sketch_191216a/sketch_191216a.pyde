def setup():
    global seed
    size(800, 300, P3D)
    frameRate(10)
    seed = 26876  # novaSemente()

def draw():
    lights()
    background(0)
    randomSeed(seed)
    translate(width / 2, height / 2)
    rotateY(radians(mouseX))
    # translate(-width / 2, -height / 2)
    r = height / 2
    for i in range(36):
        for z in range(-width, width, 30):
            x = r * sin(radians(i * 10))
            y = r * cos(radians(i * 10))
            tamanho = random(5, 25)
            fill(corSorteada())
            caixa(x, y, z, tamanho)

def keyPressed():
    global seed
    if key == ' ':
        seed = novaSemente()

def novaSemente():
    s = int(random(1000000))
    println("seed: {}".format(s))
    return s

def corSorteada():
    return color(random(256), random(256), random(256))

def caixa(x, y, z,
          w, h=None, d=None):
    h = w if h is None else h
    d = w if d is None else d
    pushMatrix()
    translate(x, y, z)
    box(w, h, d)
    popMatrix()
