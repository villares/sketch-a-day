# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s339"  # 20181203
OUTPUT = ".png"
mode = 0

from cell import Cell
from random import choice

CELL_SIZE = 20
Cell.grid = dict()

def setup():
    size(500, 500)
    rectMode(CENTER)
    init_grid()

def init_grid(func=lambda i,j: choice((True, False))):
    w, h = width//CELL_SIZE, height//CELL_SIZE
    for i in range(w):
        for j in range(h):
            Cell.grid[(i, j)] = Cell((i,j), CELL_SIZE, func(i, j))   
            
def draw():    
    background(220)
    for c in Cell.grid.values():
        c.update()
    for c in Cell.grid.values():
        c.plot(mode)
        
def keyPressed():
    global mode
    if key == "s":
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
