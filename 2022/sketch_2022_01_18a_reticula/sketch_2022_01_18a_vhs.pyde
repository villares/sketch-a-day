step = 2
elements = []

def setup():
    size(780, 500)
    background(0)
    global img
    img = loadImage("gato.jpg")
    for x in range(0, width, step):  # range(inicio, limite, step)
        for y in range(0, height, step):
            xc, yc = step / 2 + x, step / 2 + y
            cor = img.get(xc, yc)
            r = red(cor)
            g = green(cor)
            b = blue(cor)
            e = (x, y), r, g, b
            elements.append(e)
                
def draw():
    map(draw_element, elements)
        
def draw_element(e):
    (x, y), r, g, b = e
    cs = (
        (0, 0, color(r, 0, 0)),
        (0, 1, color(0, g, 0)),
        (1, 1, color(0, 0, b)),
        (1, 0, 0)
    )
    for xo, yo, c in cs:
        if random(x % int(random(40, 50))) < 1: yo = 0
        if random((height - y) % int(random(40, 50))) < 2: xo = 0
        set(x + xo, y + yo, c)
