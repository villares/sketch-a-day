from itertools import product
from poly_cell import Cell


def setup():
    global cells, grid, p1
    size(400, 400)
    grid = [[PVector(x, y) for y in range(100, 400, 100)]
            for x in range(100, 400, 100)]
    oi, oj = 0, 0
    p1 = [grid[i + oi][j + + oj] for i, j in product(range(2), repeat=2)]
    oi, oj = 1, 0
    p2 = [grid[i + oi][j + + oj] for i, j in product(range(2), repeat=2)]
    c1 = Cell(p1)
    c2 = Cell(p2)
    c3 = c1 + c2
    Cell.cells = (c1, c2, c3)

def draw():
    background(240)
    Cell.draw_cells()

    # for row in grid:
    #     for p in row:
    for p in p1:
        circle(p.x, p.y, 5)

def mouseDragged():
    Cell.drag_cells()

def offset(positions, ox, oy):
    return [(x + ox, y + oy) for x, y in positions]
