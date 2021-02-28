# siz = 8  # tamanho da grade
# font_size = 12  # tamanho dsa letras

siz = 8 * 1.33  # tamanho da grade
font_size = 16  # tamanho dsa letras



def settings():
    # size(200, 200)
    size(750, 1000)

def setup():
    global img, fonte, gliphs
    img = loadImage("1.jpg")
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
            fill(h, 255, 255)
            # fill(0)
            g = int(map(bc, 0, 255, 0, len(gliphs)-1))
            text(gliphs[g], x + siz / 2, y + siz / 2)

def keyPressed():
    global img
    if key == 's':
        saveFrame("a####.png")
    if str(key) in "123":    
        img = loadImage("{}.jpg".format(key))
        # this.surface.setResizable(True)
        this.surface.setSize(img.width, img.height)
        
    
    
