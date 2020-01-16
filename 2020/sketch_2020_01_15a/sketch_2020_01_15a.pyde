from random import choice, shuffle
from particula import Particula

NODE_SIZE = 5


def setup():
    size(500, 500)
    global grid, f
    f = createFont("Free Sans Bold", 100)
    strokeWeight(1)

    imagem = draw_text('PCD', 250, 225, text_size=225)
    grid = make_grid(imagem, width, height, 25, margin=10)
    background(100, 100, 200)

def draw():
    for particula in grid.values():
        particula.atualize()
        particula.desenha()


def keyPressed():
    if key == 's':
        saveFrame("s####.png")


def draw_text(txt, x, y, text_size=120):
    img = createGraphics(width, height)
    img.beginDraw()
    img.textFont(f)
    img.textAlign(CENTER, CENTER)
    img.textSize(text_size)
    # img.textFont(f)
    img.text(txt, x, y)
    img.endDraw()
    return img


def make_grid(p_graphics, w, h, s, margin=None):
    off = s / 2
    margin = off if margin is None else margin
    cols, rows = (w - margin * 2) // s, (h - margin * 2) // s
    points = dict()
    for i in range(cols):
        x = off + i * s + margin
        for j in range(rows):
            y = off + j * s + margin
            bc = p_graphics.get(x, y)
            if bc != 0:
                points[(i, j)] = Particula(x, y)

    return points
