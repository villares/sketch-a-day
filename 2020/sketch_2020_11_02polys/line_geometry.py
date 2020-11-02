# -*- coding: UTF-8 -*-
"""
From github.com/villares/villares/line_geometry.py

2020-09-25
2020-10-15 Fixed "line_instersection" typo, added dist() & removed TOLERANCE
2020-10-17 Added point_in_screen(), renamed poly() -> draw_poly()
2020-10-19 Fixed line_intersection typo, again :/, cleaned up stuff
"""
from __future__ import division

class Line():

    def __init__(self, a, b):
        self.a = PVector(*a)
        self.b = PVector(*b)

    def __getitem__(self, i):
        return (self.a, self.b)[i]

    def dist(self):
        return PVector.dist(self.a, self.b)

    def plot(self):
        line(self.a.x, self.a.y, self.b.x, self.b.y)

    draw = plot

    def lerp(self, other, t):
        a = PVector.lerp(self.a, other.a, t)
        b = PVector.lerp(self.b, other.b, t)
        return Line(a, b)

    def intersect(self, other):
        return line_intersect(self, other)

    def contains_point(self, x, y, tolerance=0.1):
        return point_over_line(x, y,
                               self[0][0], self[0][1],
                               self[1][0], self[1][1],
                               tolerance)

    point_over = contains_point

    def point_colinear(self, x, y, tolerance=EPSILON):
        return points_are_colinear(x, y,
                                   self[0][0], self[0][1],
                                   self[1][0], self[1][1],
                                   tolerance)

def line_intersect(line_a, line_b):
    """
    code adapted from Bernardo Fontes 
    https://github.com/berinhard/sketches/
    """
    x1, y1 = line_a.a.x, line_a.a.y
    x2, y2 = line_a.b.x, line_a.b.y
    x3, y3 = line_b.a.x, line_b.a.y
    x4, y4 = line_b.b.x, line_b.b.y
    try:
        uA = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / \
            ((y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1))
        uB = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / \
            ((y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1))
    except ZeroDivisionError:
        return
    if not(0 <= uA <= 1 and 0 <= uB <= 1):
        return
    x = line_a.a.x + uA * (line_a.b.x - line_a.a.x)
    y = line_a.a.y + uA * (line_a.b.y - line_a.a.y)
    return PVector(x, y)

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

def triangle_area(a, b, c):
    area = (a[0] * (b[1] - c[1]) +
            b[0] * (c[1] - a[1]) +
            c[0] * (a[1] - b[1]))
    return area

# class Poly():

#     def __init__(iterable):
#         self.__points = [p for p in iterable]

#     def __iter__(self):
#         return iter(self.__points)

#     def plot(self):
#         poly(self)

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
    for p in points:
        if len(p) == 2 or p[2] == 0:
            vertex(p[0], p[1])
        else:
            vertex(*p)  # desempacota pontos em 3d
    # tratamento dos furos, se houver
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

def edges_as_sets(poly_points):
    """
    Return a frozenset of poly edges as frozensets of 2 points.
    """
    return frozenset(frozenset(edge) for edge in edges(poly_points))

def edges(poly_points):
    """
    Return a list of edges (tuples containing pairs of points)
    for a list of points that represent a closed polygon
    """
    return pairwise(poly_points) + [(poly_points[-1], poly_points[0])]

def pairwise(iterable):
    from itertools import tee
    "s -> (s0, s1), (s1, s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def min_max(points):
    """
    Return two PVectors with the most extreme coordinates,
    resulting in "bounding box" corners.
    """
    points = iter(points)
    try:
        p = points.next()
        min_x, min_y = max_x, max_y = p[0], p[1]
    except StopIteration:
        raise ValueError, "min_max requires at least one point"
    for p in points:
        if p[0] < min_x:
            min_x = p[0]
        elif p[0] > max_x:
            max_x = p[0]
        if p[1] < min_y:
            min_y = p[1]
        elif p[1] > max_y:
            max_y = p[1]
    return (PVector(min_x, min_y),
            PVector(max_x, max_y))

def par_hatch(points, divisions, *sides):
    vectors = [PVector(p[0], p[1]) for p in points]
    lines = []
    if not sides:
        sides = [0]
    for s in sides:
        a, b = vectors[-1 + s], vectors[+0 + s]
        d, c = vectors[-2 + s], vectors[-3 + s]
        for i in range(1, divisions):
            s0 = PVector.lerp(a, b, i / float(divisions))
            s1 = PVector.lerp(d, c, i / float(divisions))
            lines.append(Line(s0, s1))
    return lines

def is_poly_self_intersecting(poly_points):
    ed = edges(poly_points)
    intersect = False
    for a, b in ed[::-1]:
        for c, d in ed[2::]:
        # test only non consecutive edges
            if (a != c) and (b != c) and (a != d):
                if line_intersect(Line(a, b), Line(c, d)):
                    intersect = True
                    break
    return intersect

def point_inside_poly(x, y, poly_points):
    min_, max_ = min_max(poly_points)
    if x < min_.x or y < min_.y or x > max_.x or y > max_.y:
        return False

    a = PVector(x, min_.y)
    b = PVector(x, max_.y)
    v_lines = inter_lines(Line(a, b), poly_points)
    if not v_lines:
        return False

    a = PVector(min_.x, y)
    b = PVector(max_.x, y)
    h_lines = inter_lines(Line(a, b), poly_points)
    if not h_lines:
        return False

    for v in v_lines:
        for h in h_lines:
            if line_intersect(v, h):
                return True

    return False


def inter_lines(L, poly_points):
    inter_points = []
    for a, b in edges(poly_points):
        inter = line_intersect(Line(a, b), L)
        if inter:
            inter_points.append(inter)
    if not inter_points:
        return []
    inter_lines = []
    if len(inter_points) > 1:
        inter_points.sort()
        pairs = zip(inter_points[::2], inter_points[1::2])
        for a, b in pairs:
            if b:
                inter_lines.append(Line(PVector(a.x, a.y),
                                        PVector(b.x, b.y)))
    return inter_lines

def point_in_screen(p):
    return 0 <= p[0] <= width and 0 <= p[1] <= height
