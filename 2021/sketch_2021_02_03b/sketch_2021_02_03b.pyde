siz = 5

def settings():
    size(200, 200)

def setup():
    global img
    img = loadImage("img.jpg")
    # this.surface.setResizable(True)
    this.surface.setSize(img.width, img.height)
    noStroke()

def draw():
    background(0)
    xstart = 0 # width / 2
    ystart = 0
    xend = img.width
    yend = img.height
    img.loadPixels()
    # Begin our loop for every pixel
    for x in xrange(xstart, xend, siz):
        for y in xrange(ystart, yend, siz):
            loc = x + y * img.width
            c = img.pixels[loc]
            b = brightness(c) / 255.0 * 10
            h = hue(c)
            colorMode(HSB)
            fill(h, 255, 255)
            circle(x, y, siz )            
            fill(255)
            circle(x, y, b)


def keyPressed():
    saveFrame("a.png")
