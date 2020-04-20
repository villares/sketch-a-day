"""
"Based on traditional Japanese stitching,
this is a riff on hitomezashi patterns." Annie Perikins @anniek_p
https://twitter.com/anniek_p/status/1244220881347502080?s=20
"""
from random import choice

tam = 10
mtm = tam / 2  # meio tamanho
grid = dict()
chains = []

def setup():
    global cols, rows
    size(400, 400)
    colorMode(HSB)
    cols, rows = width / mtm - 1, height / tam
    init()


def draw():
    background(200)

    for i in range(cols):
        x = i * mtm + mtm
        for j in range(rows):
            y = j * tam + mtm
            chain = in_chains(i, j)
            if chain >= 0:
                stroke((chain * 16) % 256, 255, 200)
            else:
                stroke(150)
            if grid[(i, j)]:
                if i % 2 == 0:
                    line(x, y - mtm, x, y + mtm)
                else:
                    line(x - mtm, y - mtm, x + mtm, y - mtm)

def pick_one():
    found = False
    tested = []
    while not found and len(tested) < cols * rows:
        found = True
        x, y = int(random(cols)), int(random(rows))
        for chain in chains:
            if (x, y) in chain:
                found = False
        if (x, y) not in tested:
            tested.append((x, y))
    chains.append([(x, y)])

def add_to_chains():
    for chain in chains:
        for t in chain:
            for n in active_ngbs(*t):
                if n not in chain:
                    chain.append(n)

def in_chains(x, y):
    for i, chain in enumerate(chains):
        if (x, y) in chain:
            return i
    return -1

def keyPressed():
    if key == 'a':
        pick_one()
        add_to_chains()
        print(len(chains))
        
    if key == 'p':
        saveFrame("####.png")
    if key == ' ':
        init()
        chains[:] = []

def init():
    for y in range(rows):
        on = choice((True, False))
        for x in range(cols):
            if x % 2 == 1:
                if x % 4:
                    on = not on
                grid[(x, y)] = on
    for x in range(cols):
        on = choice((True, False))
        for y in range(rows):
            if x % 2 == 0:
                on = not on
                grid[(x, y)] = on


def active_ngbs(x, y):
    return [n for n in ngbs(x, y)
            if grid[n]]

def ngbs(x, y):
    nbs = []
    if x % 2 == 0:
        nb_list = ((-1, 0), (-1, 1), (1, 0), (1, 1))
    else:
        nb_list = ((-1, 0), (-1, -1), (1, 0), (1, -1))
    for nx, ny in nb_list:
        nb = x + nx, y + ny
        if grid.get(nb) is not None:
            nbs.append(nb)
    return nbs
