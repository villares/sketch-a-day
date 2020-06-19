# foto: Sandra Rocha, São Paulo, 2020

mostra_img = False
mostra_bol = True

cw = 4
hcw = cw / 2

def setup():
    global img
    size(1000, 250)
    img = loadImage("arquivo.jpg")
    noStroke()

def draw():
    background(0)
    w, h = img.width, img.height
    p = w / h
    if mostra_img:
        image(img, 0, 0, width, width / p)
    for x in range(hcw, width, cw):
        ix = map(x, 0, width, 0, w)
        for y in range(hcw, height, cw):
            iy = map(y, 0, height, 0, h)
            cor = img.get(int(ix), int(iy))
            fill(cor)
            if mostra_bol:
                circle(x, y, cw)


def keyPressed():
    # saveFrame("sketch_2020_06_17a.png")
    global mostra_img, mostra_bol, cw
    if key == "i":
        mostra_img = not mostra_img
    if key == "o":
        mostra_bol = not mostra_bol
    if str(key) in '-_' and cw > 1:
        cw -= 1
    if str(key) in '=+':
        cw += 1
