# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s346"  # 20181210
OUTPUT = ".png"
mode = 0

from cell import Cell
from random import choice
from java.awt import Toolkit

CELL_SIZE = 24
Cell.grid = dict()

xo, yo = 100, 100
xio, yio = 0, 0
s = 10

def setup():
    size(600, 600, P3D)
    smooth(2)
    global img, grid_size
    img = loadImage("unifont-11.0.02.png")
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
     if c == color(0): return True
     else: return False
     

def draw():
    background(220)
    strokeWeight(1)
    # KeyEvent.VK_CAPS_LOCK is 20
    capsLocked = Toolkit.getDefaultToolkit().getLockingKeyState(20)
    if capsLocked:
        rectMode(CORNER)
        image(img, xio, yio)
        noFill()
        rect(xio + xo, yio + yo, grid_size, grid_size)
        init_grid(p_ou_b)
    else:
        rectMode(CENTER)
        for c in Cell.grid.values():
            c.update()
        for c in Cell.grid.values():
            c.plot(mode)

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
        if key == "t":
            init_grid(lambda i, j: choice((True, False))
                      if j < grid_size / 3 or j > grid_size * 0.66 else False )
    if xo > width - grid_size:
        xio = width - grid_size - xo
    if yo > height - grid_size:
        yio = height - grid_size - yo


# print text to add to the project's README.md
def settings():
    println(
        """
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, SKETCH_NAME[1:], OUTPUT)
    )
