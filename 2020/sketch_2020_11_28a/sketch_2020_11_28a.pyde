from __future__ import division
from itertools import product

from villares.line_geometry import draw_poly, poly_edges, Line
from villares.line_geometry import hatch_poly, hatch_rect, rect_points

def setup():
    size(700, 600)
    # noSmooth()
    # rectMode(CENTER)
    global ang_pairs
    angs = (0, 15, 45, 60, 90, 135) #122.5, 135, 147.5)
    ang_pairs = list(set(frozenset((a, b)) for a, b in  product(angs, repeat=2)))

    textSize(8)
        

def draw():
    background(130, 50, 50)
    # print frameRate
    stroke(0)
    fill(255)
    s = 100
    i = 0
    for x, y in grid(7, 6, s, s):
        r = rect_points(5 + x, 5 + y, s - 10, s - 10)
        rect(6 + x, 6 + y, s - 12, s - 12)
        # strokeWeight(3)
        ang_pair = ang_pairs[i % len(ang_pairs)] 
        # if i >= len(ang_pairs): strokeWeight(2)
        # else: strokeWeight(1)
        for ang in ang_pair:
            hatch_rect(r, radians(ang),
                       spacing=6.0,
                       function=fixed_dash_line if i >= len(ang_pairs) else None,
                       dash_spacing=6.0,
                       # element_spacing=10.0,
                       # element_size=4,
                       # element_function=lambda x, y, _: point(x, y),
                       base=True,
                       )
        text(str(tuple(ang_pair)), x + 10, y + 5)
        i += 1

def fixed_dash_line(xa, ya, xb, yb, **kwargs):
    proportion = kwargs.pop('dash_proportion', kwargs.pop('proportion', 0.5))
    spacing = kwargs.pop('dash_spacing', kwargs.pop('spacing', 20))
    base_line = kwargs.pop('base_line', None)
    inside = Line(xa, ya, xb, yb)
    base_line = base_line or inside
    b = base_line.as_PVector()
    base_length = b.mag()
    divisions = int(base_length / spacing)
    v = (b * spacing * proportion).div(base_length)
    xs, ys = base_line[0][0], base_line[0][1]
    for i in range(0, int(divisions) + 1):
        xe, ye = xs + v.x, ys + v.y
        start_in, end_in = inside.contains_point(
            xs, ys), inside.contains_point(xe, ye)
        if start_in and end_in:
            line(xs, ys, xe, ye)
        elif end_in:
            ending = Line(xe, ye, inside[1][0], inside[1][1])
            if ending.dist() <= spacing * proportion:
                ending.plot()
        elif start_in:
            starting = Line(xs, ys, inside[0][0], inside[0][1])
            if starting.dist() <= spacing * proportion:
                starting.plot()
        xs += v.x
        ys += v.y


# def element_line(xa, ya, xb, yb, **kwargs):
#     spacing = kwargs.pop('element_spacing', kwargs.pop('spacing', 20))
#     element_size = kwargs.pop('element_size', 5)
#     element_function = kwargs.pop('element_function', square)
#     divisions = int(dist(xa, ya, xb, yb) / spacing) + 1  # + keyPressed
#     for i in range(1, divisions):
#         t = i / float(divisions)
#         x, y, _ = Line(xa, ya, xb, yb).line_point(t)
#         element_function(x, y, element_size)

def grid(cols, rows, colSize=1, rowSize=1):
    """
    Returns an iterator that provides coordinate tuples. Example:
    # for x, y in grid(10, 10, 12, 12):
    #     rect(x, y, 10, 10)
    """
    rowRange = range(int(rows))
    colRange = range(int(cols))
    for y in rowRange:
        for x in colRange:
            yield (x * colSize, y * rowSize)

def keyPressed():
    saveFrame(sketch_name() + '.png')
    
def sketch_name():
    from os import path
    sketch = sketchPath()
    return path.basename(sketch)
