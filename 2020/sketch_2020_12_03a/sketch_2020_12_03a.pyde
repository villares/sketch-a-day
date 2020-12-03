from __future__ import division
from itertools import product

from villares.line_geometry import draw_poly, poly_edges, Line, min_max
from villares.line_geometry import rect_points, rotate_point, inter_lines
from villares.helpers import grid, memoize, sketch_name

def setup():
    size(500, 500)
    # noSmooth()
    # rectMode(CENTER)
    global ang_pairs
    angs = (0, 45, 90, 135)  # 122.5, 135, 147.5)
    ang_pairs = list(set(frozenset((a, b))
                         for a, b in product(angs, repeat=2)))
    textSize(8)

def draw():
    background(50, 50, 150)
    # print frameRate
    stroke(0)
    fill(255)
    s = 100
    i = 0
    for x, y in grid(5, 5, s, s):
        pts = rect_points(5 + x, 5 + y, s - 10, s - 10)
        pts.append((x + s / 2, y + s * 0.75))
        draw_poly(pts)
        # strokeWeight(3)
        ang_pair = ang_pairs[i % len(ang_pairs)]
        # if i >= len(ang_pairs): strokeWeight(2)
        # else: strokeWeight(1)
        for ang in ang_pair:
            ps = hatch_poly(tuple(pts), radians(ang),
                            ps=True,
                            spacing=8.0,
                            function=(fixed_dash_line
                                      if i >= len(ang_pairs)
                                      else None),
                            odd_function=(None
                                          if i >= len(ang_pairs) * 2
                                          else False),
                            dash_spacing=10.0,
                            # element_spacing=10.0,
                            # element_size=4,
                            # element_function=lambda x, y, _: point(x, y),
                            base=False
                            )
            if ps:
                shape(ps)
        text(str(tuple(ang_pair)), x + 10, y + 5)
        i += 1

def fixed_dash_line(xa, ya, xb, yb, **kwargs):
    proportion = kwargs.pop('dash_proportion', kwargs.pop('proportion', 0.5))
    spacing = kwargs.pop('dash_spacing', kwargs.pop('spacing', 20))
    inside = Line(xa, ya, xb, yb)
    base_line = kwargs.pop('base_line', inside)
    ps = kwargs.get('ps', None)

    def ps_or_line(ps, xs, ys, xe, ye):
        # circle(xs, ys, 3)
        # circle(xe, ye, 2)
        if ps:
            ps.addChild(createShape(LINE, xs, ys, xe, ye))
        else:
            line(xs, ys, xe, ye)

    b = base_line.as_PVector()
    base_length = b.mag()
    divisions = int(base_length / spacing)
    v = (b * spacing).div(base_length + EPSILON)
    xs, ys = base_line[0][0], base_line[0][1]
    insx, insy = inside[1][0], inside[1][1]
    inex, iney = inside[0][0], inside[0][1]

    for i in range(0, int(divisions) + 1):
        xe, ye = xs + v.x * proportion, ys + v.y * proportion
        start_in = inside.contains_point(xs, ys)
        end_in = inside.contains_point(xe, ye)
        if start_in and end_in:
            ps_or_line(ps, xs, ys, xe, ye)
        elif end_in and dist(xe, ye, inex, iney) < spacing * proportion:
            ps_or_line(ps, xe, ye, inex, iney)
        elif start_in and dist(xs, ys, insx, insy) < spacing * proportion:
            ps_or_line(ps, xs, ys, insx, insy)
        xs += v.x
        ys += v.y


# def element_line(xa, ya, xb, yb, **kwargs):
#     spacing = kwargs.pop('element_spacing', kwargs.pop('spacing', 20))
#     element_size = kwargs.pop('element_size', 5)
#     element_function = kwargs.pop('element_function', square)
# divisions = int(dist(xa, ya, xb, yb) / spacing) + 1  # + keyPressed
#     for i in range(1, divisions):
#         t = i / float(divisions)
#         x, y, _ = Line(xa, ya, xb, yb).line_point(t)
#         element_function(x, y, element_size)


def keyPressed():
    saveFrame(sketch_name() + '.png')

def hatch_poly(*args, **kwargs):
    if len(args) == 2:
        pts, angle = args
        bound = min_max(pts)
        diag = Line(bound)
        d = diag.dist()
        cx, cy, _ = diag.midpoint()
    else:
        x, y, w, h, angle = args
        pts = rect_points(x, y, w, h, kwargs.pop('mode', CORNER))
        d = dist(pts[0][0], pts[0][1], pts[2][0], pts[2][1])
        cx = (pts[0][0] + pts[1][0]) / 2.0
        cy = (pts[1][1] + pts[2][1]) / 2.0
    spacing = kwargs.get('spacing', 5)
    function = kwargs.pop('function', None)
    base = kwargs.pop('base', True)
    odd_function = kwargs.pop('odd_function', False)
    kwargs['ps'] = ps = (createShape(GROUP) if kwargs.get('ps', False)
                         else False)
    num = int(d / spacing)
    rr = [rotate_point(x, y, angle, cx, cy)
          for x, y in rect_points(cx, cy, d, d, mode=CENTER)]
    # stroke(255, 0, 0)   # debug mode
    ab = Line(rr[0], rr[1])  # ;ab.plot()  # debug mode
    cd = Line(rr[3], rr[2])  # ;cd.plot()  # debug mode
    for i in range(num + 1):
        if odd_function is not False and i % 2:
            kwargs['function'] = odd_function
        else:
            kwargs['function'] = function
        abp = ab.line_point(i / float(num)) 
        cdp = cd.line_point(i / float(num)) 
        if base == True:
            kwargs['base_line'] = Line(abp, cdp)
        inter_line_list = inter_lines(Line(abp, cdp), pts)
        for hli in inter_line_list:
            hli.plot(**kwargs)
            # if len(inter_line_list) > 1:
            #     fill(255, 0, 0)
            # else:
            #     fill(255)
            # circle(hli[0][0], hli[0][1], 3) # debug mode
            # circle(hli[1][0], hli[1][1], 5) # debug mode
    return ps
