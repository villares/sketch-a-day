# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s355"  # 20181219
OUTPUT = ".png"
mode = 0

from cell import Cell
from random import choice

CELL_SIZE = 40
Cell.grid = dict()

s = 5
x, y = 0, 0
vx, vy = random(-2, 2), random(-2, 2)

def setup():
    size(500, 500)
    global img, grid_size
    img = loadImage("a.png")
    grid_size = width / CELL_SIZE

def init_grid(f=None):
    w, h = width // CELL_SIZE, height // CELL_SIZE
    for i in range(w):
        for j in range(h):
            if f == None:
                f = lambda i, j: choice((True, False))
            Cell.grid[(i, j)] = Cell((i, j), CELL_SIZE, f(i, j))

def p_ou_b(i, j):
    c = img.get(xo + i, yo + j)
    if c == color(0):
        return True
    else:
        return False


def draw():
    # scale(3)
    background(220)
    rectMode(CENTER)
    for c in Cell.grid.values():
        c.update(x, y)
    for c in Cell.grid.values():
        c.plot(mode)
    global vx, vy, x, y
    x += vx
    y += vy
    if not 0 < x < width:
        vx = -vx
    if not 0 < y < height:
        vy = -vy
    ellipse

def keyPressed():
    global mode
    global xo, yo, xio, yio
    if key == CODED:

        if keyCode == RIGHT and xo < img.width - 11:
            xo += 16
        if keyCode == LEFT and xo > 10:
            xo -= 16
        if keyCode == DOWN and yo < img.height - 11:
            yo += 16
        if keyCode == UP and yo > 10:
            yo -= 16
    else:
        if key == "s" or key == "S":
            saveFrame(SKETCH_NAME + "_###.png")
        if key in "01234567789":
            mode = int(key)
        if key == "-":
            mode = -1
        if key == " ":
            init_grid(lambda i, j: False)
        if key == "x":
            init_grid(lambda i, j: (i + j) % 2 == 0)
        if key == "r":
            init_grid()


# print text to add to the project's README.md
def settings():
    println(
        """
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, SKETCH_NAME[1:], OUTPUT)
    )
