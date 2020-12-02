from __future__ import division
from itertools import product

from villares.line_geometry import draw_poly, poly_edges, Line, min_max
from villares.line_geometry import rect_points, rotate_point, inter_lines
from villares.file_helpers import sketch_name
from villares.grids import grid

def setup():
    size(500, 500)
    global ang_pairs
    angs = (0, 45, 90, 135) #122.5, 135, 147.5)
    ang_pairs = list(set(frozenset((a, b, c)) for a, b, c in  product(angs, repeat=3)))
    textSize(8)
        

def draw():
    background(150, 150, 50)
    # print(frameRate)
    stroke(0)
    fill(255)
    s = 100
    i = 1
    for x, y in grid(5, 6, s, s):
        r = tuple(rect_points(5 + x, 5 + y, s - 10, s - 10) + [(x + s / 2, y + s /2)])
        fill(130, 150, 150)
        draw_poly(r) # rect(6 + x, 6 + y, s - 12, s - 12)
        ang_pair = tuple(ang_pairs[i % len(ang_pairs)]) 
        # if i >=  2* len(ang_pairs): ang_pair = ang_pair[::-1] if len(ang_pair) > 1 else []
        # else: strokeWeight(1)
        for a, ang in enumerate(ang_pair):
            h = hatch_poly(r, radians(ang),
                       spacing=6.0,
                       ps=True,
                       function=fixed_dash_line if i >= len(ang_pairs) and not a % 2 else None,
                       dash_spacing=6.0,
                       base=True,
                       )
            if h: shape(h)
        fill(0)
        text(str(tuple(ang_pair)), x + 10, y + 5)
        i += 1


def memoize(f):
    memo = {}
    def memoized_func(*args, **kwargs):
        if args not in memo:
            r = f(*args, **kwargs)
            memo[args] = r
            return r
        return memo[args]
    return memoized_func

@memoize
def hatch_rect(*args, **kwargs):
    if len(args) == 2:
        r, angle = args
    else:
        x, y, w, h, angle = args
        r = rect_points(x, y, w, h, kwargs.get('mode', CORNER))
    spacing = kwargs.get('spacing', 10)
    function = kwargs.get('function', None)
    kwargs['ps'] = ps =  createShape(GROUP) if kwargs.get('ps', False) else False  
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
                    hli.plot(**kwargs)                
    return ps

@memoize
def hatch_poly(points, angle, **kwargs):
    spacing = kwargs.get('spacing', 5)
    function = kwargs.get('function', None)
    base = kwargs.pop('base', False)
    kwargs['ps'] = ps =  createShape(GROUP) if kwargs.get('ps', False) else False  

    bound = min_max(points)
    diag = Line(bound)
    d = diag.dist()
    cx, cy, _ = diag.midpoint()
    num = int(d / spacing)
    rr = [rotate_point(x, y, angle, cx, cy)
          for x, y in rect_points(cx, cy, d, d, mode=CENTER)]
    # stroke(255, 0, 0)   # debug mode
    ab = Line(rr[0], rr[1])  # ;ab.plot()  # debug mode
    cd = Line(rr[3], rr[2])  # ;cd.plot()  # debug mode
    for i in range(num + 1):
        abp = ab.line_point(i / float(num) + EPSILON)
        cdp = cd.line_point(i / float(num) + EPSILON)
        if base == True:
            kwargs['base_line'] = Line(abp, cdp)
        for hli in inter_lines(Line(abp, cdp), points):
            hli.plot(**kwargs)
    return ps

 
 
def fixed_dash_line(xa, ya, xb, yb, **kwargs):
    proportion = kwargs.pop('dash_proportion', kwargs.pop('proportion', 0.5))
    spacing = kwargs.pop('dash_spacing', kwargs.pop('spacing', 20))
    inside = Line(xa, ya, xb, yb)
    base_line = kwargs.pop('base_line', inside)
    ps = kwargs.get('ps', None)
    
    b = base_line.as_PVector()
    base_length = b.mag()
    divisions = int(base_length / spacing)
    v = (b * spacing).div(base_length)
    xs, ys = base_line[0][0], base_line[0][1]
    for i in range(0, int(divisions) + 1):
        xe, ye = xs + v.x * proportion, ys + v.y * proportion
        start_in, end_in = inside.contains_point(
            xs, ys), inside.contains_point(xe, ye)
        if start_in and end_in:
            # Line(xs, ys, xe, ye).plot(**kwargs)
            if  ps:
                ps.addChild(createShape(LINE, xs, ys, xe, ye))
            else:
                line(xs, ys, xe, ye)
        elif end_in:
            ending = Line(xe, ye, inside[1][0], inside[1][1])
            if ending.dist() <= spacing * proportion:
                ending.plot(**kwargs)
        elif start_in:
            starting = Line(xs, ys, inside[0][0], inside[0][1])
            if starting.dist() <= spacing * proportion:
                starting.plot( **kwargs)
        xs += v.x
        ys += v.y
                                              
def keyPressed():
    saveFrame(sketch_name() + '.png')
    
