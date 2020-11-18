from itertools import product
from poly_cell import Cell


def setup():
    global cells, grid, p1
    size(600, 600)
    cell_size = 30
    grid = [[PVector(x, y) for x in range(cell_size, 600, cell_size)]
            for y in range(cell_size, 600, cell_size)]
    rows = len(grid) - 2
    Cell.cells = [Cell(four_from_grid(i, j)) for i, j in product(range(rows), repeat=2)]
    a = Cell.cells.pop()
    b = Cell.cells.pop()
    Cell.cells.append(a + b)

def draw():
    background(240)
    Cell.draw_cells()

    for row in grid:
        for p in row:
            point(p.x, p.y)

def mouseDragged():
    Cell.drag_cells()

def four_from_grid(oi, oj):
    return [grid[i + oi][j + + oj] for i, j in product(range(2), repeat=2)]
