add_library('GifAnimation')
from gif_animation_helper import gif_export

grids = []

def setup():
    size(600, 600)
    for function in (grid, shuffled_grid, shoebot_shuffled):
        grids.append(make_a_grid(function, 50))

def draw():
    background(0)
    g = lerp_grid(grids[0], grids[1],
                  0.5 + sin(radians(frameCount)) / 2)
    plot_a_grid(g)

    gif_export(GifMaker, sketch_name())
    if frameCount == 360:
        gif_export(GifMaker, finish=True)

def plot_a_grid(a_grid):
    noStroke()
    for x, y, siz, cor in a_grid:
        fill(cor)
        ellipse(x, y, siz, siz)

def shuffled_grid(cols, rows, colSize=1, rowSize=1):
    from random import shuffle
    sg = list(grid(cols, rows, colSize, rowSize))
    shuffle(sg)
    return sg

def grid(cols, rows, colSize=1, rowSize=1):
    """
    Returns an iterator that contains coordinate tuples.
    As seen in Shoebot & Nodebox (minus 'shuffled mode')
    A common way to use is:
    #    for x, y in grid(10, 10, 12, 12):
    #        rect(x, y, 10, 10)
    """
    rowRange = range(int(rows))
    colRange = range(int(cols))
    for y in rowRange:
        for x in colRange:
            yield (x * colSize, y * rowSize)

def shoebot_shuffled(cols, rows, colSize=1, rowSize=1):
    from random import shuffle
    rowRange = list(range(int(rows)))
    colRange = list(range(int(cols)))
    shuffle(rowRange)
    shuffle(colRange)
    for y in rowRange:
        for x in colRange:
            yield (x * colSize, y * rowSize)

def make_a_grid(grid_function, i_offset=50):
    colorMode(HSB)
    i = i_offset
    a_grid = []
    offset_x, offset_y = 30, 30
    for x, y in grid_function(10, 10, 60, 60):
        c = color(i * 2.5 % 256, 255, 200)
        s = 10 + abs(40 - (.8 * i))
        a_grid.append((x + offset_x, y + offset_y, s, c))
        i = (i + 1) % 101
    return a_grid

def lerp_grid(a_grid, b_grid, t):
    c_grid = []
    for a_el, b_el in zip(a_grid, b_grid):
        c_el = (lerp(a_el[0], b_el[0], t),
                lerp(a_el[1], b_el[1], t),
                lerp(a_el[2], b_el[2], t),
                lerpColor(a_el[3], b_el[3], t),
                )
        c_grid.append(c_el)
    return c_grid

def sketch_name():
    from os import path
    sketch = sketchPath()
    return path.basename(sketch)
