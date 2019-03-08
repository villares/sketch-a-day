# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s337"  # 20181201
OUTPUT = ".png"

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
    for c in Cell.grid.values():
        c.play()

def keyPressed():
    if key == "s":
        saveFrame("###.png")                                    
                                                                                                            
# print text to add to the project's README.md             
def settings():
    println(
"""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, SKETCH_NAME[1:], OUTPUT)
    )
