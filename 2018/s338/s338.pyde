# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s338"  # 20181202
OUTPUT = ".png"
mode = 0

from cell import Cell
from random import choice

CELL_SIZE = 25
Cell.grid = dict()

def setup():
    size(500, 500)
    rectMode(CENTER)
    init_grid(width//CELL_SIZE, height//CELL_SIZE)

def init_grid(w, h):
    for i in range(w):
        for j in range(h):
            Cell.grid[(i, j)] = Cell((i,j), CELL_SIZE, choice((True, False)))    
            
def draw():    
    background(220)
    for c in Cell.grid.values():
        c.play(mode)
        
def keyPressed():
    global mode
    if key == "s":
        saveFrame("###.png")
    if key == "2":
        mode = 2
    if key == "1":
        mode = 1
    if key == "0":
        mode = 0
                                            
# print text to add to the project's README.md             
def settings():
    println(
"""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, SKETCH_NAME[1:], OUTPUT)
    )
