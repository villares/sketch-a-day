from __future__ import division
from itertools import product

from villares.line_geometry import draw_poly, poly_edges, Line
from villares.line_geometry import rect_points, rotate_point, inter_lines

def setup():
    size(500, 500)
    global ang_pairs
    angs = (0, 45, 90, 135)  # 122.5, 135, 147.5)
    ang_pairs = list(set(frozenset((a, b, c))
                         for a, b, c in product(angs, repeat=3)))
    # ang_pairs.extend((ang,) for ang in angs)
    textSize(8)

def draw():
    background(130, 150, 150)
    print(frameRate)
    stroke(0)
    fill(255)
    s = 100
    i = 1
    for x, y in grid(5, 6, s, s):
        r = tuple(rect_points(5 + x, 5 + y, s - 10, s - 10))
        fill(150, 130, 150)
        rect(6 + x, 6 + y, s - 12, s - 12)
        # strokeWeight(3)
        ang_pair = tuple(ang_pairs[i % len(ang_pairs)])
        # if i >=  2* len(ang_pairs): ang_pair = ang_pair[::-1] if len(ang_pair) > 1 else []
        # else: strokeWeight(1)
        for a, ang in enumerate(ang_pair):
            h = hatch_rect(r, radians(ang),
                           spacing=6.0,
                           ps=True,  # for ps=False, disable @memoize!
                           function=None,
                           )
            if h:
                shape(h)
        fill(0)
        text(str(tuple(ang_pair)), x + 10, y + 5)
        i += 1


def keyPressed():
    saveFrame(sketch_name() + '.png')

def sketch_name():
    from os import path
    sketch = sketchPath()
    return path.basename(sketch)

def memoize(f):
    memo = {}

    def memoized_func(*args, **kwargs):
        if args not in memo:
            r = f(*args, **kwargs)
            memo[args] = r
            return r
        return memo[args]
    return memoized_func

@memoize   # only works with rect_hatch ps=True
def hatch_rect(*args, **kwargs):
    if len(args) == 2:
        r, angle = args
    else:
        x, y, w, h, angle = args
        r = rect_points(x, y, w, h, kwargs.get('mode', CORNER))
    spacing = kwargs.get('spacing', 10)
    function = kwargs.pop('function', None)
    base = kwargs.pop('base', False)
    ps = createShape(GROUP) if kwargs.get('ps', False) else None
    d = dist(r[0][0], r[0][1], r[2][0], r[2][1])
    cx = (r[0][0] + r[1][0]) / 2.0
    cy = (r[1][1] + r[2][1]) / 2.0
    num = int(d / spacing)
    rr = [rotate_point(x, y, angle, cx, cy)
          for x, y in rect_points(cx, cy, d, d, mode=CENTER)]
    # stroke(255, 0, 0)   # debug mode
    ab = Line(rr[0], rr[1])  # ;ab.plot()  # debug mode
    cd = Line(rr[3], rr[2])  # ;cd.plot()  # debug mode
    for i in range(num + 1):
        abp = ab.line_point(i / float(num) + EPSILON)
        cdp = cd.line_point(i / float(num) + EPSILON)
        for hli in inter_lines(Line(abp, cdp), r):
            if not ps:
                hli.plot()
            else:
                li = createShape(LINE,
                                 hli[0][0], hli[0][1], hli[1][0], hli[1][1])
                ps.addChild(li)
                shape(li)
    return ps


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
