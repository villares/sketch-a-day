from __future__ import division
from villares import ubuntu_jogl_fix  # you probably won't need this

from copy import deepcopy

ox, oy = 0, 0

def setup():
    global grid, other_grid
    size(640, 640, P3D)
    rectMode(CENTER)
    fill(0)
    colorMode(HSB)
    noSmooth()
    grid = rec_grid(0, 0, 8, width)
    other_grid = deepcopy(grid)

def draw():
    global f
    f = frameCount / 80.0
    background(0)
    ortho()
    translate(width / 2, height / 2)
    draw_grid(grid)

    if frameCount % 10 == 0:
        n = noise(f)
        if n > 0.5:
            split_cells(grid)
        else:
            merge_cells(grid)


def draw_grid(grid):
    if grid is None: return
    for cell in grid:
        if cell[-1] in (None, -1):
            x, y, cw, flag = cell
            if flag is None:
                stroke(8 + 2 * (cw + 2), 255, 255)
            else:
                stroke(255)
            sbox(x, y, cw)  # * (1 + cos(f + PI)) / 2)
        else:
            draw_grid(cell)

def draw_grid2(grid, other_grid):
    for i, cell in enumerate(grid):
        other_cell = other_grid[i]
        if cell == other_cell:
            if cell[-1] in (None, -1):
                x, y, cw, flag = cell
                if flag is None:
                    stroke(8 + 2 * (cw + 2), 255, 255)
                else:
                    stroke(255)
                sbox(x, y, cw)  # * (1 + cos(f + PI)) / 2)
            else:
                draw_grid2(cell, other_grid[i])
        else:
            t = sin(f) #0map(mouseX, 0, width, 0, 1)
            flat = flatten_grid(cell)
            flat_o = flatten_grid(other_cell)
            flat_l = lerp_grid(flat, flat_o, t)
            draw_grid(flat_l)

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
                grid[i] = rec_grid(x, y, 2, cw + 2, True)

def merge_cells(grid):
    for i, cell in enumerate(grid):
        if cell[-1] not in(None, -1):
            if check_valid_cells(cell):
                x, y, cw, flag = cell[0]
                # grid[i] = mangle_cell(cell)
                if random(10) > 8:
                    grid[i] = (x + (cw + 2) / 2.0,
                               y + (cw + 2) / 2.0,
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


def otranslate(x, y):
    global ox, oy
    ox += x
    oy += y

def rec_grid(x, y, n, tw, shallow=None):
    otranslate(x, y)
    cw = float(tw) / n
    margin = (cw - tw) / 2.0
    cells = []
    for i in range(n):
        nx = cw * i + margin
        for j in range(n):
            ny = cw * j + margin
            if cw > 8 and random(10) < 5 and not shallow:
                cs = rec_grid(nx, ny, 2, cw)
                cells.append(cs)
            else:
                cells.append((ox + nx,
                              oy + ny,
                              cw - 2, None))
    otranslate(-x, -y)
    return cells


def sbox(x, y, s):
    pushMatrix()
    translate(x, y, -abs(s * (x + y)) / 10.0)
    rotateX(PI * sin(f + PI))
    rotateY(PI * cos(f + PI))
    circle(0, 0, s)
    popMatrix()

def flatten_grid(grid):
    cells = []
    for i, cell in enumerate(grid):
        try:
            len(cell)
        except:
            return []

        if cell[-1] in (None, -1):
            cells.append(cell)
        else:
            down = flatten_grid(cell)
            if down:
                cells.extend(down)
    return [cell for cell in cells if len(cell)]

def lerp_grid(a, b, t):
    if len(a) == 0 or len(b) == 0:
        return
    na, nb = a, b
    if len(a) > len(b):
        nb = b + a[: (len(a) - len(b))]
    if len(a) < len(b):
        na = a + b[:1] * (len(b) - len(a))

    return [(lerp(xa, xb, t),
             lerp(ya, yb, t),
             lerp(cwa, cwb, t),
             flag)
            for (xa, ya, cwa, flag),
                (xb, yb, cwb, _) in zip(na, nb)]
