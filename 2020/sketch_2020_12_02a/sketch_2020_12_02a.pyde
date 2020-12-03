from __future__ import division
from itertools import product

from villares.line_geometry import draw_poly, poly_edges, Line, min_max
from villares.line_geometry import rect_points, rotate_point, inter_lines
from villares.helpers import sketch_name, grid

def setup():
    size(500, 500)
    global ang_pairs
    angs = (0.0, 45.0, 90, 135) #122.5, 135, 147.5)
    # ang_pairs = list(set(frozenset((a, b, c)) for a, b, c in  product(angs, repeat=3)))
    ang_pairs = []
    ang_pairs.extend((ang,) for ang in angs)
    textSize(8)        

def draw():
    background(150, 50, 150)
    # print(frameRate)
    stroke(0)
    fill(255)
    s = 250
    i = 1
    for x, y in grid(2, 2, s, s):
        # p = (mouseX + x, mouseY + y)
        p = (75 + x, 75 + y)
        r = rect_points(5 + x, 5 + y, s - 10, s - 10)
        r.append(p)
        fill(130, 150, 150)
        draw_poly(r) # rect(6 + x, 6 + y, s - 12, s - 12)
        # strokeWeight(3)
        ang_pair = tuple(ang_pairs[i % len(ang_pairs)]) 
        # if i >=  2* len(ang_pairs): ang_pair = ang_pair[::-1] if len(ang_pair) > 1 else []
        # else: strokeWeight(1)
        for a, ang in enumerate(ang_pair):
            h = hatch_poly(tuple(r), radians(ang),
                       spacing=6.0,
                       ps=True,
                       function=fixed_dash_line,
                       odd_function=None,
                       dash_spacing=6.0,
                       # element_spacing=10.0,
                       # element_size=4,
                       # element_function=lambda x, y, _: point(x, y),
                       base=True,
                       )
            if h: shape(h)
        fill(0)
        text(str(tuple(ang_pair)), x + 10, y + 5)
        i += 1

def memoize(f):
    memo = {}
    NotSet = object()
    def memoized_func(*args, **kwargs):
        a = (args, tuple(kwargs.values()))
        result = memo.get(a, NotSet)
        if result == NotSet:
            result = f(*args, **kwargs)
            memo[a] = result
        return result
    return memoized_func

@memoize
def hatch_poly(*args, **kwargs):
    if len(args) == 2:
        points, angle = args
    else:
        x, y, w, h, angle = args
        points = rect_points(x, y, w, h, kwargs.pop('mode', CORNER))
    spacing = kwargs.get('spacing', 5)
    function = kwargs.pop('function', None)
    base = kwargs.pop('base', False)
    odd_function = kwargs.pop('odd_function', False)

    kwargs['ps'] = ps =  createShape(GROUP) if kwargs.get('ps', False) else False  
    if len(args) == 2:
        d = dist(points[0][0], points[0][1], points[2][0], points[2][1]) + EPSILON
        cx = (points[0][0] + points[1][0]) / 2.0
        cy = (points[1][1] + points[2][1]) / 2.0
    else:
        bound = min_max(points)
        diag = Line(bound) 
        d = diag.dist() + EPSILON
        cx, cy, _ = diag.midpoint()
    num = int(d / spacing)
    rr = [rotate_point(x, y, angle, cx, cy)
          for x, y in rect_points(cx, cy, d, d, mode=CENTER)]
    # stroke(255, 0, 0)   # debug mode
    ab = Line(rr[0], rr[1])   #;ab.plot()  # debug mode
    cd = Line(rr[3], rr[2])   #;cd.plot()  # debug mode
    for i in range(num + 1):
        if odd_function is not False and i % 2:
            kwargs['funtion'] = odd_function 
        else:
            kwargs['funtion'] = function
        abp = ab.line_point(i / float(num) + EPSILON)
        cdp = cd.line_point(i / float(num) + EPSILON)
        if base == True:
            kwargs['base_line'] = Line(abp, cdp)
        for hli in inter_lines(Line(abp, cdp), points):
            hli.plot(**kwargs)
    return ps

hatch_rect = hatch_poly
 
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


# def element_line(xa, ya, xb, yb, **kwargs):
#     spacing = kwargs.pop('element_spacing', kwargs.pop('spacing', 20))
#     element_size = kwargs.pop('element_size', 5)
#     element_function = kwargs.pop('element_function', square)
#     divisions = int(dist(xa, ya, xb, yb) / spacing) + 1  # + keyPressed
#     for i in range(1, divisions):
#         t = i / float(divisions)
#         x, y, _ = Line(xa, ya, xb, yb).line_point(t)
#         element_function(x, y, element_size)


            
def keyPressed():
    saveFrame(sketch_name() + '.png')
    
