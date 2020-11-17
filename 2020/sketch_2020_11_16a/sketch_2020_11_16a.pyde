from itertools import product
from poly_cell import Cell


def setup():
    global cells, grid, p1
    size(400, 400)
    grid = [[PVector(x, y) for y in range(100, 400, 100)]
            for x in range(100, 400, 100)]
    p1 = four_from_grid(0, 0)
    p2 = four_from_grid(1, 0)
    oi, oj = 1, 1
    p3 = [grid[i + oi][j + + oj] for i, j in product(range(2), repeat=2)]
    c1 = Cell(p1)
    c2 = Cell(p2)
    c3 = Cell(p3)
    c4 = c1 + c2 + c3
    Cell.cells = (c1, c2, c3, c4)

def draw():
    background(240)
    Cell.draw_cells()

    for row in grid:
        for p in row:
            circle(p.x, p.y, 5)

def mouseDragged():
    Cell.drag_cells()

def four_from_grid(oi, oj):
    return [grid[i + oi][j + + oj] for i, j in product(range(2), repeat=2)]
