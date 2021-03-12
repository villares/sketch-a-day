
siz = 6  # tamanho da grade
font_size = 18  # tamanho dsa letras
vEspaco = 5
precisao = 0.7


def settings():
    # size(200, 200)
    size(1200, 1200, P2D)

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
    background(0)
    #ondas
    tempo = 0 #frameCount / 10.0
    stroke(129)
    noFill()
    for y in range(-vEspaco, img.height + vEspaco, vEspaco * 2):
        comprimento = 0
        beginShape()
        for x in range(0, img.width, 2):
            y_sin = sin(comprimento + tempo) * vEspaco + y
            vertex(x * 2, y_sin * 2)
            comprimento += 1
        endShape()    
    
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
            fill(h, 200, 200)
            # fill(c)
            g = int(map(bc, 0, 255, 0, len(gliphs)-1))
            text(gliphs[g], 2 * x + siz / 2, 2 * y + siz / 2)

    stroke(255)
    strokeWeight(2)
    noFill()


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
            colorMode(HSB)
            stroke(col)
            # stroke(hue(col), 255, 255)
            vertex(x * 2, _y * 2)
            x += precisao / (intensidade + 0.01) / 5
            fase += 0.5

        vertex(img.width * 2, _y * 2)
        endShape()


def keyPressed():
    global img
    if key == 's':
        saveFrame("a####.png")

    
