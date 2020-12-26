# from villares import ubuntu_jogl_fix  # you probably won't need this

ox, oy = 0, 0

def setup():
    global grid
    size(640, 640)
    rectMode(CENTER)
    fill(0)
    colorMode(HSB)
    noSmooth()
    grid = rec_grid(0, 0, 8, width)

def draw():
    randomSeed(1)
    global f
    f = frameCount / 80.0
    background(0)
    ortho()
    translate(width / 2, height / 2)

    draw_grid(grid)


def keyPressed():
    if key == 's':
        split_cells(grid)
    if key == 'm':
        merge_cells(grid)

def split_cells(grid):
    for i, cell in enumerate(grid):
        if cell[-1] not in (None, -1):
                split_cells(cell)
        elif cell[-1] in (None, -1) and cell[-2] >= 8:
            if random(10) > 9:
                x, y, cw, _ = cell    
                grid[i] = rec_grid(x, y, 2, cw + 2)

def merge_cells(grid):
    for i, cell in enumerate(grid):
        if cell[-1] not in(None, -1):
            if check_valid_cells(cell):
                x, y, cw, flag = cell[0]
                # grid[i] = mangle_cell(cell)
                if random(10) > 8:
                    grid[i] = (x + (cw + 2) / 2,
                               y + (cw + 2) / 2,
                               cw * 2 + 2, flag)
            else:
                merge_cells(cell)

def mangle_cell(cells):
    return [(x, y, cw, -1)
            for x, y, cw, flag in cells]


def check_valid_cells(cells):
    if cells[-1] in (None, -1):
        return False
    else:
        cw = cells[0][-2]
        return all(cell[-1] is None and cell[-2] == cw
                   for cell in cells)

def draw_grid(grid):
    for cell in grid:
        if cell[-1] in (None, -1):
            x, y, cw, flag = cell
            if flag is None:
                stroke(8 + 2 * (cw + 2), 255, 255)
            else:
                stroke(255)
            square(x, y, cw)  # * (1 + cos(f + PI)) / 2)
        else:
            draw_grid(cell)

def otranslate(x, y):
    global ox, oy
    ox += x
    oy += y

def rec_grid(x, y, n, tw):
    otranslate(x, y)
    cw = float(tw) / n
    margin = (cw - tw) / 2.0
    cells = []
    for i in range(n):
        nx = cw * i + margin
        for j in range(n):
            ny = cw * j + margin
            if cw > 8 and random(10) < 5:
                cs = rec_grid(nx, ny, 2, cw)
                cells.append(cs)
            else:
                cells.append((ox + nx,
                              oy + ny,
                              cw - 2, None))
    otranslate(-x, -y)
    return cells


def sbox(x, y, s, s2):
    pushMatrix()
    translate(x, y, -s2)
    rotateX(PI * cos(f + PI))
    rotateY(PI * cos(f + PI))
    box(s, s, s2)
    popMatrix()
