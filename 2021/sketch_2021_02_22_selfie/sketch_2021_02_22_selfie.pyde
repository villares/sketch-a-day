# siz = 8  # tamanho da grade
# font_size = 12  # tamanho dsa letras

siz = 8 * 1.33  # tamanho da grade
font_size = 16  # tamanho dsa letras
vEspaco = 10
precisao = 3


def settings():
    # size(200, 200)
    size(650, 650, P2D)

def setup():
    global img, fonte, gliphs
    img = loadImage("unnamed.jpg")
    # this.surface.setResizable(True)
    # this.surface.setSize(img.width, img.height)
    noStroke()
    fonte = createFont("Tomorrow Bold",60)
    textFont(fonte)
    textAlign(CENTER, CENTER)
    gliphs = (
    """`.',-:;^"~*_<>+!ir=ltfj|\/cI1?(v)Lzsx}{T]o[eunaJ"""
    """7YFkhqpdby4#CZg2PVK3XEAUS5H0mDORw8GN%96$Q&BMW@"""
    )[::-1]  

def draw():
    # background(0, 0, 200)
    background(240)
    xend = img.width
    yend = img.height
    img.loadPixels()
    # Begin our loop for every pixel
    for x in xrange(0, xend, siz):
        for y in xrange(0, yend, siz):
            loc = x + y * img.width
            c = img.pixels[loc]
            bc = brightness(c)
            b = bc / 255.0 * siz
            h = hue(c)
            textSize(font_size)
            # if bc  > 150: #map(mouseX, 0, width, 16, 240):
            #     fill(255)
            #     g = int(map(bc, 0, 255, 0, len(gliphs)-1))
            #     text(gliphs[g], x + siz / 2, y + siz / 2)
            # else:
            colorMode(HSB)
            fill(h, 100, 128, 100)
            fill(h, 100, 128)
            g = int(map(bc, 0, 255, 0, len(gliphs)-1))
            text(gliphs[g], x + siz / 2, y + siz / 2)

    # image(img, 0, 0)
    stroke(255)
    strokeWeight(2)
    img.loadPixels()
    noFill()

    tempo = 0 #frameCount / 10.0

    #ondas
    stroke(129)
    for y in range(-vEspaco, img.height + vEspaco, vEspaco * 2):
        comprimento = 0
        beginShape()
        for x in range(0, img.width, 2):
            y_sin = sin(comprimento + tempo) * vEspaco + y
            vertex(x, y_sin)
            comprimento += 1
        endShape()

    #img em frequencias
    for y in range(0, img.height, vEspaco):
        x = 0
        _y = y
        fase = noise(y) * TWO_PI
        beginShape()
        while x < img.width:
            col = img.get(floor(x), y)
            r = red(col)
            g = green(col)
            b = blue(col)
            intensidade = 1 - ((r + g + b) / 765)
            _y = y + sin(fase - intensidade - tempo) * vEspaco / 2 + vEspaco / 2
            stroke(col)
            vertex(x, _y)
            x += precisao / (intensidade + 0.01) / 5
            fase += 0.5

        vertex(img.width, _y)
        endShape()


def keyPressed():
    global img
    if key == 's':
        saveFrame("a####.png")

    
