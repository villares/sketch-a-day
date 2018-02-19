add_library('pdf')
import random as rnd

LISTA = []
MARGIN = 100

def setup():
    size(712, 712)
    noFill()
    nova_lista()
    println("'s' to save, and 'n' for a new drawing")

def nova_lista():
    LISTA[:] = []
    for _ in range(30):
        LISTA.append((
            random(MARGIN, width - MARGIN),  # x
            random(MARGIN, height - MARGIN),  # y
            rnd.choice([10, 20, 30]),  # size
            rnd.choice([2, 4, 6]),  # strokeWeight
            rnd.choice([True, False]),  # arrow
            list()  # other nodes
        ))
    for node in LISTA:
        random_node = rnd.choice(LISTA)
        if random_node != node:
            node[-1].append(random_node)


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
    for x, y, s, w, arrow, sub_lista in LISTA:
        strokeWeight(w)
        for n in sub_lista:
            if arrow:
                stroke(0)
                seta(x, y, n[0], n[1], s, w * 5)
            else:
                stroke(255)
                line(x, y, n[0], n[1])
        ellipse(x, y, s, s)
        
def keyPressed():
    if key == 's':
        saveFrame("####.png")
    if key == 'n':
        nova_lista()
