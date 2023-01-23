

from random import choice

from cell import Cell

mode = 0
CELL_SIZE = 50
modulus = 3


def setup():
    size(1050, 500, P2D)
    smooth(8)
    global grid_size
    grid_size = width / CELL_SIZE
    rect_mode(CENTER)
    stroke_cap(SQUARE)
    Cell.step_start = -5
    Cell.step_end = 6
    Cell.step = 5

def init_grid(f=None):
    # default grid is with random state for cells
    if f is None:
        def f(i, j): return choice((True, False))
    # number of collums and rows -2 for default cell sized border
    w = int(width // CELL_SIZE) - 2
    h = int(height // CELL_SIZE) - 2
    for i in range(w):
        for j in range(h):
            # default Cell constructor has border=CELL_SIZE
            Cell.grid[(i, j)] = Cell((i, j), CELL_SIZE, f(i, j))


def draw():
    background(200)
    for c in Cell.grid.values():
        c.update(mouse_x, mouse_y)
    for c in Cell.grid.values():
        c.plot(mode, lambda _: color(100), offset=1.5)
        c.plot(mode, lambda i: 255 if i == 0 else color(0, 128 + i * 25,
                                                           128 - i * 25))


def key_pressed():
    global mode, modulus
    if key == 's' or key == 'S':
        save_frame('###.png')
    if key != CODED and key in '0123456789':
        mode = int(key)
    if key == '-':
        mode = -1
    if key == ' ':
        def t(i, j): return True
        def f(i, j): return False
        init_grid(choice((t, f)))
    if key == 'r':
        init_grid()
    if key == 'x':
        init_grid(lambda i, j: (i + j) % modulus)
    if key == 'z':
        move_grid()
    if key == 'd':
        save_pickle(Cell.grid, 'sketch.data')
    if key == 'l':
        Cell.grid = load_pickle('sketch.data')

def move_grid(x=1, y=1):
    w, h = width // CELL_SIZE, height // CELL_SIZE
    new_grid = dict()
    for i in range(w):
        for j in range(h):
            c = Cell.grid.get((i, j), None)
            if c:
                c.index = ((i + x) % w, (j + y) % h)
                c.calculate_pos()
                new_grid[c.index] = c
    Cell.grid = new_grid


