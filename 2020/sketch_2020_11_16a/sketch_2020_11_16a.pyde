from itertools import product
from poly_cell import Cell


def setup():
    global cells
    size(400, 400)
    grid = [[PVector(x, y) for x in range(100, 400, 100)]
                           for y in range(100, 400, 100)]
    base_pos = product(range(2), repeat=2)
    p1 = [grid[i][j] for i, j in base_pos]
    Cell.cells.append(Cell(p1))

    pos2 = offset(base_pos, 0, 1)
    p2 = [grid[i][j] for i, j in pos2]
    Cell.cells.append(Cell(p2))
                      
    Cell.cells.append(Cell(p1) + Cell(p2))



def draw():
    background(240)
    Cell.draw_cells()
    # noLoop()

def mouseDragged():
    Cell.drag_cells()

def offset(positions, ox, oy):
    return [(x + ox, y + oy) for x, y in positions]
