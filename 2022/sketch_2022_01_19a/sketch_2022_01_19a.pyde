step = 10
elements = []

def setup():
    size(800, 400)
    background(0)
    noStroke()
    frameRate(10)
    f = createFont('Tomorrow ExtraBold', 100)
    global img
    img = createGraphics(width, height)
    img.beginDraw()
    img.smooth()
    img.textFont(f)
    img.textSize(120)
    img.textLeading(120)
    img.textAlign(CENTER, CENTER)
    img.text('GENUARY\n2022', width / 2, height / 2)
    img.endDraw()
    for x in range(0, width, step):  # range(inicio, limite, step)
        for y in range(0, height, step):
            xc, yc = step / 2 + x, step / 2 + y
            c = img.get(xc, yc)
            e = (x, y), brightness(c) if c != -1 else 255
            print c
            elements.append(e)
                
def draw():
    background(100)
    map(draw_element, elements)
        
def draw_element(e):
    (x, y), c = e
    hs = step / 2
    rr = 0 if random(100) > 1 else random(c)
    cs = (
        (0, 0, color(c, 0, 0)),
        (0, 1, color(0, c, 0)),
        (1, 1, color(0, 0, c)),
        (1, 0, rr)
    ) if c != 0 else ()
    for xo, yo, c in cs:
        fill(c)
        rect(x + xo * hs, y + yo * hs, hs, hs)
