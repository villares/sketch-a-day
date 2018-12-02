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
    saveFrame("###.png")
    print "oi"        
        
        
        
        
        
        
