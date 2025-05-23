# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s364"  # 20181228
OUTPUT = ".png"
mode = 0

from cell import Cell
from random import choice

CELL_SIZE = 25
Cell.grid = dict()
modulus = 3

def setup():
    size(500, 500)
    global grid_size
    grid_size = width / CELL_SIZE
    rectMode(CENTER)
    strokeCap(SQUARE)

def init_grid(f=None):
    w, h = width // CELL_SIZE, height // CELL_SIZE
    for i in range(w):
        for j in range(h):
            if f == None:
                f = lambda i, j: choice((True, False))
            Cell.grid[(i, j)] = Cell((i, j), CELL_SIZE, f(i, j))

def draw():
    background(200)
    for c in Cell.grid.values():
        c.update(mouseX, mouseY)
    for c in Cell.grid.values():
        c.plot(mode)


def keyPressed():
    global mode, modulus
    if key == "s" or key == "S":
        saveFrame(SKETCH_NAME + "_###.png")
    if key != CODED and key in "01234567789":
        mode = int(key)
    if key == "-":
        mode = -1
    if key == " ":
        t = lambda i, j: True
        f = lambda i, j: False
        init_grid(choice((t, f)))
    if key == "r":
        init_grid()
    if key == "x":
        init_grid(lambda i, j: (i + j) % modulus)
    if keyCode == LEFT and modulus > 2:
        modulus -= 1
    if keyCode == RIGHT:
        modulus += 1
 

# print text to add to the project's README.md
def settings():
    println(
        """
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, SKETCH_NAME[1:], OUTPUT)
    )
