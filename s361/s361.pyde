# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s361"  # 20181225
OUTPUT = ".png"
mode = 0

from cell import Cell
from random import choice

CELL_SIZE = 25
Cell.grid = dict()

def setup():
    size(500, 500)
    global grid_size
    grid_size = width / CELL_SIZE
    rectMode(CENTER)

def init_grid(f=None):
    w, h = width // CELL_SIZE, height // CELL_SIZE
    for i in range(w):
        for j in range(h):
            if f == None:
                f = lambda i, j: choice((True, False))
            Cell.grid[(i, j)] = Cell((i, j), CELL_SIZE, f(i, j))

# def p_ou_b(i, j):
#     c = img.get(xo + i, yo + j)
#     if c == color(0):
#         return True
#     else:
#         return False


def draw():
    background(220)
    for c in Cell.grid.values():
        c.plot(mode)

    for c in Cell.grid.values():
        c.update(mouseX, mouseY)


def keyPressed():
        global mode
        if key == "s" or key == "S":
            saveFrame(SKETCH_NAME + "_###.png")
        if key != CODED and key in "01234567789":
            mode = int(key)
        if key == "-":
            mode = -1
        if key == " ":
            init_grid(lambda i, j: False)
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
