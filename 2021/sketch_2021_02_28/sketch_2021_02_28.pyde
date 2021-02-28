# siz = 8  # tamanho da grade
# font_size = 12  # tamanho dsa letras

siz = 8 * 1.33  # tamanho da grade
font_size = 8 * 1.33 # tamanho dsa letras
noise_scale = 0.01


def settings():
    # size(200, 200)
    size(600, 600)

def setup():
    global img, fonte, gliphs
    # img = loadImage("1.png")
    # this.surface.setResizable(True)
    # this.surface.setSize(img.width, img.height)
    noStroke()
    fonte = createFont("Tomorrow Bold",60)
    textFont(fonte)
    textAlign(CENTER, CENTER)
    gliphs = (
    """`.',-:;^"~*_<>+!ir=ltfj|\/cI1?(v)Lzsx}{T]o[eunaJ"""
    """7YFkhqpdby4#CZg2PVK3XEAUS5H0mDORw8GN%96$Q&BMW@"""
    )#[::-1]  

def draw():
    # background(0, 0, 200)
    background(0)
    xend = width # img.width
    yend = height #img.height
    # img.loadPixels()
    # Begin our loop for every pixel
    f = frameCount / 2.0
    for x in xrange(0, xend, siz):
        for y in xrange(0, yend, siz):
            # bc = 128 * noise(x * noise_scale, y * noise_scale, f * noise_scale)
            h = 255 * noise(y * noise_scale, f * noise_scale, x * noise_scale, )
            bc = 128 * noise(y * noise_scale, f * noise_scale, x * noise_scale, )

            textSize(font_size)
            colorMode(HSB)
            fill(h, 255, 255)
            # fill(0)
            g = int(map(bc, 0, 255, 0, len(gliphs)-1))
            text(gliphs[g], x + siz / 2, y + siz / 2)

def keyPressed():
    global img
    if key == 's':
        saveFrame("a####.png")

        
    
    
