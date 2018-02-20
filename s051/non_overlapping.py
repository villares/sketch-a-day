"""
sketch 51 180220 - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day
"""
import random as rnd

LISTA = []
MARGIN = 100
CEL_SIZE = 100
HALF_CEL = CEL_SIZE / 2
pontos = []

def setup():
    size(712, 712)
    h, w = height - 2 * MARGIN, width - 2 * MARGIN
    noFill()
    n_rows, n_cols = int(h / CEL_SIZE), int(w / CEL_SIZE)
    for r in range(n_rows):
        for c in range(n_cols):
            x, y = HALF_CEL + c * CEL_SIZE,\
                HALF_CEL + r * CEL_SIZE
            pontos.append((x + MARGIN, y + MARGIN))  # acrescenta um Ponto

    nova_lista()
    println("'s' to save, and 'n' for a new drawing")


def nova_lista():
    LISTA[:] = []
    for _ in range(30):
        x, y = rnd.choice(pontos)
        LISTA.append((
            x,  # x
            y,  # y
            rnd.choice([10, 20, 30]),  # size
            rnd.choice([2, 4, 6]),  # strokeWeight
            rnd.choice([True, False]),  # arrow
            list()  # other nodes
        ))
    for node in LISTA:
        rnd_node = rnd.choice(LISTA)
        x1, y1, x2, y2 = node[0], node[1], rnd_node[0], rnd_node[1]
        if (x1, y1) != (x2, y2):
            node[-1].append(rnd_node)


def seta(x1, y1, x2, y2, shorter=12, head=12):
    """ draws an arrow """
    L = dist(x1, y1, x2, y2)
    with pushMatrix():
        translate(x2, y2)
        angle = atan2(x1 - x2, y2 - y1)
        rotate(angle)
        offset = -shorter * .6
        line(0, offset, 0, -L - offset)
        line(0, offset, -head / 3, -head + offset)
        line(0, offset, head / 3, -head + offset)

def draw():
    background(200)



def keyPressed():
    if key == 's':
        saveFrame("####.png")
    if key == 'n':
        nova_lista()