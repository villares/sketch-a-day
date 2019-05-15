# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
# based on "sketch_190125a"

from random import choice
from cell import Cell

CELL_SIZE = 50

def setup():
    size(600, 600, P3D)
    global grid_size
    grid_size = width / CELL_SIZE
    init_grid()

def init_grid(f=None):
    # default grid is with random state for cells
    if f == None:
        f = lambda i, j: choice((True, False))
    # number of collums and rows
    w = int(width // CELL_SIZE)
    h = int(height // CELL_SIZE)
    z = 4
    # print(w, h)
    for i in range(w):
        for j in range(h):
            for k in range(z):
                Cell.grid[(i, j, k)] = Cell((i, j, k), CELL_SIZE, f(i, j))

def draw():
    background(200)
    stroke(128, 0, 0)
    for c in Cell.grid.values():
        c.plot(0)
    stroke(0, 0, 128)
    for c in Cell.grid.values():
        c.plot(1)

def keyPressed():
    if key == "r":
        init_grid()
    elif key == "p":
        saveFrame("####.png")

# print text to add to the project's README.md
def settings():
    from os import path
    global SKETCH_NAME
    SKETCH_NAME = path.basename(sketchPath())
    OUTPUT = ".png"
    println(
        """
![{0}](2019/{0}/{0}{1})

[{0}](https://github.com/villares/sketch-a-day/tree/master/2019/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, OUTPUT)
    )
