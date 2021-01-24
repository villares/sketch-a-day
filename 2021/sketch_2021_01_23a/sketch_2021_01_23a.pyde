from cell import Cell

CELL_SIZE = 25
Cell.grid = dict()
grid_lines = True

def setup():
    size(500, 500)
    rectMode(CENTER)
    init_grid(width//CELL_SIZE, height//CELL_SIZE)

def init_grid(w, h):
    for i in range(w):
        for j in range(h):
            Cell.grid[(i, j)] = Cell((i,j), CELL_SIZE)    
            
def draw():
    if grid_lines:
        stroke(0)
    else:
        noStroke()
    for c in Cell.grid.values():
        c.play()
        
        
        
        
        
        
        
        
