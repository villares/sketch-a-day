"""
sketch 50 180219 - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day
"""
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
            rnd.choice([10, 20, 30]),  # circle size
            rnd.choice([2, 4, 6]),  # strokeWeight
            rnd.choice([True, False]),  # is arrow
            list()  # sub_list of nodes
        ))
    for node in LISTA:
        random_node = rnd.choice(LISTA)
        if random_node != node:
            node[-1].append(random_node)  # adds random node to the sub_list

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
    # x, y, s: circle size, w: strokeWeightm, arrow T/F, points to...
    for x1, y1, d1, sw, arrow, points_to in LISTA:
        strokeWeight(sw)
        for other in points_to:
            x2, y2 = other[0], other[1]
            if arrow:
                stroke(0)
                # x1, y1, x2, y2, circle offset, arrow head size
                seta(x1, y1, x2, y2, d1, sw * 5)
            else:
                stroke(255)
                line(x1, y1, x2, y2)
        ellipse(x1, y1, d1, d1)

def keyPressed():
    if key == 's':
        saveFrame("####.png")
    if key == 'n':
        nova_lista()
