from poly_cell import Cell

def setup():
    global cells
    size(400, 400)
    pa = PVector(100, 100)
    pb = PVector(200, 100)
    pc = PVector(200, 200)
    pd = PVector(100, 200)
    pe = PVector(300, 100)
    pf = PVector(300, 200)

    c1 = Cell((pa, pc, pb, pd))
    c2 = Cell((pb, pe, pf, pc))
    c3 = c1 + c2
    Cell.cells = (c1, c2, c3)

def draw():
    background(240)
    Cell.draw_cells()
    # noLoop()
    
def mouseDragged():
    Cell.drag_cells()
    
        
