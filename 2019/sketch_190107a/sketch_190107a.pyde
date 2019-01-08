# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "sketch_190107a" 
OUTPUT = ".gif"
mode = 0
save_frame = False

from cell import Cell
from random import choice
add_library('GifAnimation')
from gif_exporter import gif_export

CELL_SIZE = 25
Cell.step_start = -3
Cell.step_end = 4
Cell.step = 3
Cell.rotated_start = True
modulus = 3

def setup():
    size(500, 500)
    global grid_size
    grid_size = width / CELL_SIZE
    rectMode(CENTER)
    strokeCap(SQUARE)

def init_grid(f=None):
    # default grid is with random state for cells
    if f == None:
        f = lambda i, j: choice((True, False))
    # number of collums and rows -2 for default cell sized border    
    w = int(width // CELL_SIZE) #- 2
    h = int(height // CELL_SIZE) #- 2
    for i in range(w):
        for j in range(h):
            # default Cell constructor has border=CELL_SIZE
            Cell.grid[(i, j)] = Cell((i, j), CELL_SIZE, f(i, j), border=0) 

def draw():
    background(200)
    for c in Cell.grid.values():
        c.update(mouseX, mouseY)
    for c in Cell.grid.values():
        c.plot(mode)

    if save_frame:
         global save_frame
         save_frame = False
         gif_export(GifMaker, SKETCH_NAME)

def keyPressed():
    global mode, modulus, save_frame
    if key == "g" or key == "G":
        save_frame = True
    if key == "s" or key == "S":
        saveFrame(SKETCH_NAME + "_#######.png")
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
    if key == "<" and modulus > 2:
        modulus -= 1
    if key == ">":
        modulus += 1
    if key == "z":
        move_grid()
    if key == "R":
        Cell.rotated_start = not Cell.rotated_start
    if keyCode == RIGHT:
        move_grid(x=1, y=0)
    if keyCode == LEFT:
        move_grid(x=-1, y=0)
    if keyCode == UP:
        move_grid(x=0, y=-1)
    if keyCode == DOWN:
        move_grid(x=0, y=1)

def move_grid(x=1, y=1):
    w, h = width // CELL_SIZE, height // CELL_SIZE
    new_grid = dict()
    for i in range(w):
        for j in range(h):
            c = Cell.grid.get((i, j), None)
            if c:
                c.index = ((i + x) % w, (j + y) % h)
                c.calculate_pos()
                new_grid[c.index] = c
            # else:
            #     f = lambda i, j: choice((True, False))
            #     new_grid[(i, j)] = Cell((i, j), CELL_SIZE, f(i, j))
                
    Cell.grid = new_grid


# print text to add to the project's README.md
def settings():
    println(
        """
![{0}](2019/{0}/{0}{1})

[{0}](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME,OUTPUT)
    )
