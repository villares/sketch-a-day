# -*- coding: UTF-8 -*-
"""
From https://github.com/villares/villares/blob/main/line_geometry.py

2020-09-25
2020-10-15 Fixed "line_instersection" typo, added dist() & removed TOLERANCE
2020-10-17 Added point_in_screen(), renamed poly() -> draw_poly()
2020-10-19 Fixed line_intersection typo, again :/, clean up, new point_inside_poly
2020-11-13 set of edges non-frozen option
2020-11-14 line_intersection now works with 2 tuples of 2 points, 4 points or 8 coords.
2020-11-20 Fixing Line that now accepts 1, 2 and 4 arguments; line_instance.draw() returns self
2020-11-20 New min_max algorithm (also adding bounding_box alias)
2020-11-20 rect_points(), rotate_point(), hatch_rect(), hatch_poly()
2020-11-22 Line .plot() method now accepts a custom drawing function. And so does hatch_poly().
2020-11-26 Line .plot() method to accept kwargs, added .as_PVector() as helper for Line objs.
2020-12-02 min_max() fix for PVector (x, y, z), replaced point_inside_poly & reverted some hatch_poly()
2020-12-03 inter_lines() fix, removed hatch_rect(), updated hatch_poly() <- still to be tested
2021_02_21 Simplify is_poly_self_intersecting()
2021_04_26 poly_area()
2021_05_30 ccw() & simple_intersect() - modified is_poly_self_intersecting()
2021_06_08 Removing PVectors all around, simplified min_max(points), added corner_angle(corner, a, b)
2021_09_21 Fix .dist() method in Line for 3D lines and allowed xa, ya, za, xb, yb, zb
2021_09_21 line_intesect() now may provide intersection outside the line segments & bug fix. Clean up.
2021_10_20 Make min_max() compatible with Python 3
2022_03_02 Make it work with py5
"""

from __future__ import division
from helpers import lerp_tuple

try:
    EPSILON
except NameError:
    from py5 import *
    beginShape = begin_shape
    endShape = end_shape
    bezierVertex = bezier_vertex

class Line():

    def __init__(self, *args):
        if len(args) == 1:
            self.start = tuple(args[0][0])
            self.end = tuple(args[0][1])
        elif len(args) == 2:
            self.start = tuple(args[0])
            self.end = tuple(args[1])
        elif len(args) == 4:
            self.start = tuple(args[:2])
            self.end = tuple(args[2:])
        elif len(args) == 6:
            self.start = tuple(args[:3])
            self.end = tuple(args[3:])
        else:
            raise ValueError(
    "Requires 1 Line-like object, a pair of 2D or 3D tuples/PVectors, or x1, y1 [,z1], x2, y2 [,z2] coords."
            )

    def __getitem__(self, i):
        return (self.start, self.end)[i]

    def __setitem__(self, i, v):
        if i == 0:
            self.start = v
        elif i == 1:
            self.end = v
    
    def dist(self):
        return dist(*(self.start + self.end))  # for 3D lines
        # return dist(self.start[0], self.start[1], self.end[0], self.end[1])

    def plot(self, *args, **kwargs):
        function = kwargs.pop('function', None)
        ps = kwargs.get('ps', None)
        if not function and ps:
            ps.addChild(createShape(LINE,
                                    self[0][0], self[0][1],
                                    self[1][0], self[1][1]))
        elif not function:
            line(*(self.start + self.end))  # might make 3D lines (invisible if not in P3D)
            # line(self[0][0], self[0][1], self[1][0], self[1][1])
        else:
            function(self[0][0], self[0][1], self[1][0], self[1][1],
                     *args, **kwargs)
        return self

    draw = plot

    def lerp(self, other, t):
        a = lerp_tuple(self.start, other.start, t)
        b = lerp_tuple(self.end, other.end, t)
        return Line(a, b)

    def line_point(self, t):
        return lerp_tuple(self.start, self.end, t)

    def midpoint(self):
        return lerp_tuple(self.start, self.end, 0.5)

    def intersect(self, other):
        return line_intersect(self, other)

    def simple_intersect(self, other):
        return simple_intersect(self, other)

    def contains_point(self, x, y, tolerance=0.1):
        return point_over_line(x, y,
                               self[0][0], self[0][1],
                               self[1][0], self[1][1],
                               tolerance)

    point_over = contains_point

    def as_PVector(self):
        return PVector(self[1][0], self[1][1]) - PVector(self[0][0], self[0][1])

    def point_colinear(self, x, y, tolerance=EPSILON):
        return points_are_colinear(x, y,
                                   self[0][0], self[0][1],
                                   self[1][0], self[1][1],
                                   tolerance)

def line_intersect(*args, **kwargs):
    """
    Adapted from Bernardo Fontes https://github.com/berinhard/sketches/
    2020-11-14 Does not assume Line objects anymore, and works with 4 points or 8 coords.
    2021_09_26 Adding intersection outside the segments. Also fixing bug when calling with 8 coords as arguments.
    2021_09_26 Removed line_a & line_b variables, rewrote ZeroDivision exception catching as a conditional check.
    """
    as_PVector = kwargs.get('as_PVector', False)
    in_segment = kwargs.get('in_segment', True)
    
    if len(args) == 2:  # expecting 2 Line objects or 2 tuples of 2 point tuples.
        (x1, y1), (x2, y2) = args[0]
        (x3, y3), (x4, y4) = args[1]
    elif len(args) == 4:
        (x1, y1), (x2, y2) = args[:2]
        (x3, y3), (x4, y4) = args[2:]
    elif len(args) == 8:
        x1, y1, x2, y2, x3, y3, x4, y4 = args
    else:
        raise ValueError("line_intersect requires 2 lines, 4 points or 8 coords.")
            
    divisor = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
    if divisor:
        uA = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / divisor
        uB = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / divisor
    else:
        return None
    if not in_segment or 0 <= uA <= 1 and 0 <= uB <= 1:
        x = x1 + uA * (x2 - x1)
        y = y1 + uA * (y2 - y1)
        return PVector(x, y) if as_PVector else (x, y)
    else:
        return None
    
def point_over_line(px, py, lax, lay, lbx, lby,
                    tolerance=0.1):
    """
    Check if point is over line using the sum of
    the distances from the point to the line ends
    (the result has to be near equal for True).
    """
    ab = dist(lax, lay, lbx, lby)
    pa = dist(lax, lay, px, py)
    pb = dist(px, py, lbx, lby)
    return (pa + pb) <= ab + tolerance

def points_are_colinear(ax, ay, bx, by, cx, cy,
                        tolerance=EPSILON):
    """
    Test for colinearity by calculating the area
    of a triangle formed by the 3 points.
    """
    area = triangle_area((ax, ay), (bx, by), (cx, cy))
    return abs(area) < tolerance


# class Poly():

#     def __init__(iterable):
#         self.__points = [p for p in iterable]

#     def __iter__(self):
#         return iter(self.__points)

#     def plot(self):
#         poly(self.__points)

#     draw = poly


def draw_poly(points, holes=None, closed=True):
    """
    Aceita como pontos sequencias de tuplas, lista ou vetores com (x, y) ou (x, y, z).
    Note que `holes` espera uma sequencias de sequencias ou uma única sequencia de
    pontos. Por default faz um polígono fechado.
    """

    def depth(seq):
        """
        usada para checar se temos um furo ou vários
        devolve 2 para um só furo, 3 para vários furos
        """
        if (isinstance(seq, list) or
                isinstance(seq, tuple) or
                isinstance(seq, PVector)):
            return 1 + max(depth(item) for item in seq)
        else:
            return 0

    beginShape()  # inicia o PShape
    if len(tuple(points[0])) == 2:
        for p in points:
            vertex(p[0], p[1])
    else:
        for p in points:
            vertex(*p)  # desempacota pontos em 3d

    holes = holes or []  # equivale a: holes if holes else []
    if holes and depth(holes) == 2:  # sequência única de pontos
        holes = (holes,)     # envolve em um tupla
    for hole in holes:  # para cada furo
        beginContour()  # inicia o furo
        for p in hole:
            if len(p) == 2 or p[2] == 0:
                vertex(p[0], p[1])
            else:
                vertex(*p)
        endContour()  # final e um furo
    # encerra o PShape
    if closed:
        endShape(CLOSE)
    else:
        endShape()

poly = draw_poly

def edges_as_sets(poly_points, frozen=True):
    """
    Return a (frozen)set of poly edges as frozensets of 2 points.
    """
    if frozen:
        return frozenset(frozenset(edge) for edge in poly_edges(poly_points))
    else:
        return set(frozenset(edge) for edge in poly_edges(poly_points))

def poly_edges(poly_points):
    """
    Return a list of edges (tuples containing pairs of points)
    for a list of points that represent a closed polygon
    """
    return pairwise(poly_points) + [(poly_points[-1], poly_points[0])]

edges = poly_edges

def pairwise(iterable):
    from itertools import tee
    "s -> (s0, s1), (s1, s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def min_max(points):
    """
    Return two tuples or PVectors with the most extreme coordinates,
    resulting in "bounding box" corners.
    """
    coords = tuple(zip(*points))
    if isinstance(points[0], PVector):
        return PVector(*map(min, coords)), PVector(*map(max, coords))
    else:
        return tuple(map(min, coords)), tuple(map(max, coords))

bounding_box = min_max

def triangle_area(a, b, c):
    area = (a[0] * (b[1] - c[1]) +
            b[0] * (c[1] - a[1]) +
            c[0] * (a[1] - b[1]))
    return area

def poly_area(points):
    points = list(points)
    area = 0.0
    for (ax, ay), (bx, by) in zip(points, points[1:] + [points[0]]):
        area += ax * by
        area -= bx * ay
    return abs(area) / 2.0
    
def rect_points(ox, oy, w, h, mode=CORNER, angle=None):
    if mode == CENTER:
        x, y = ox - w / 2.0, oy - h / 2.0
    else:
        x, y = ox, oy
    points = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
    if angle is None:
        return points
    else:
        return [rotate_point((x, y), angle, (ox, oy))
                for x, y in points]

def rotate_point(*args):
    """
    point (tuple/PVector), angle
    x, y, angle (around 0, 0)
    point (tuple/PVector), angle, center (tuple/PVector)
    x, y, angle, x_center, y_center
    """
    if len(args) == 2:
        (xp, yp), angle = args
        x0, y0 = 0, 0
    if len(args) == 3:
        try:
            (xp, yp), angle, (x0, y0) = args
        except TypeError:
            xp, yp, angle = args
            x0, y0 = 0, 0
    if len(args) == 5:
        xp, yp, angle, x0, y0 = args
    x, y = xp - x0, yp - y0  # translate to origin
    xr = x * cos(angle) - y * sin(angle)
    yr = y * cos(angle) + x * sin(angle)
    # if isinstance(args[0], PVector):                
    #     return PVector(xr + x0, yr + y0)
    # else:
    #     return (xr + x0, yr + y0)
    return (xr + x0, yr + y0)

def point_in_screen(*args):
    if len(args) == 1:
        x, y = args[0][0], args[0][1]
    else:
        x, y = args[0], args[1]
    return 0 <= screenX(x, y) <= width and 0 <= screenY(x, y) <= height
    

def par_hatch(points, divisions, *sides):
    # points = [(p[0], p[1]) for p in points]
    lines = []
    if not sides:
        sides = [0]
    for s in sides:
        a, b = points[-1 + s], points[+0 + s]
        d, c = points[-2 + s], points[-3 + s]
        for i in range(1, divisions):
            s0 = lerp_tuple(a, b, i / float(divisions))
            s1 = lerp_tuple(d, c, i / float(divisions))
            lines.append(Line(s0, s1))
    return lines

def is_poly_self_intersecting(poly_points):
    edges = poly_edges(poly_points)
    for a, b in edges[::-1]:
        for c, d in edges[2::]:
            # test only non consecutive edges
            if (a != c) and (b != c) and (a != d):
                if simple_intersect(a, b, c, d):
                    return True
    return False

def point_inside_poly(x, y, points):
    # ray-casting algorithm based on
    # https://wrf.ecse.rpi.edu/Research/Short_Notes/pnpoly.html
    inside = False
    for i, p in enumerate(points):
        pp = points[i - 1]
        xi, yi = p
        xj, yj = pp
        intersect = ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi)
        if intersect:
            inside = not inside
    return inside

def inter_lines(given_line, poly_points):
    """ 
    Line objects that indicate the complete overlap of a given line
    and a polygon (provided as a collection og points)
    """
    inter_pts = []
    for a, b in poly_edges(poly_points):
        inter_pt = line_intersect(Line(a, b), given_line)
        if inter_pt:
            inter_pts.append(inter_pt)
    if not inter_pts:
        return []
    inter_lines = []
    if len(inter_pts) > 1:
        fptx, fpty = inter_pts[0][0], inter_pts[0][1]
        first_pt_dist = lambda pt: ((pt[0] - fptx) ** 2 +
                                    (pt[1] - fpty) ** 2)
        inter_pts.sort(key=first_pt_dist)
        pairs = zip(inter_pts[::2], inter_pts[1::2])
        for a, b in pairs:
            if b:
                inter_lines.append(Line(a, b))
    return inter_lines

def ccw(*args):
    """Returns True if the points are arranged counter-clockwise in the plane"""
    if len(args) == 1:
        a, b, c = args[0]
    else:
        a, b, c = args
    return (b[0] - a[0]) * (c[1] - a[1]) > (b[1] - a[1]) * (c[0] - a[0])

def simple_intersect(*args):
    """Returns True if line segments intersect."""
    if len(args) == 2:    
        (a1, b1), (a2, b2) = args[0], args[1]
    else:
        a1, b1, a2, b2 = args
    return ccw(a1, b1, a2) != ccw(a1, b1, b2) and ccw(a2, b2, a1) != ccw(a2, b2, b1)

def is_poly_convex(poly_points):
    for i, a in enumerate(poly_points):
        b = poly_points[i - 1]
        c = poly_points[i - 2]
        if not ccw(a, b, c):
            return False
    return True

def corner_angle(corner, a, b):
    ac = atan2(a[1] - corner[1], a[0] - corner[0])
    bc = atan2(b[1] - corner[1], b[0] - corner[0])
    return abs(ac - bc)           
  
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
        abp = ab.line_point(i / float(num))  # + EPSILON)
        cdp = cd.line_point(i / float(num))  # + EPSILON)
        if base == True:
            kwargs['base_line'] = Line(abp, cdp)
        inter_line_list = inter_lines(Line(abp, cdp), pts)
        for hli in inter_line_list:
            hli.plot(**kwargs)
    return ps

hatch_rect = hatch_poly
