from functools import cache

from shapely import Polygon
import py5



class Shape(object):
    
    remove_flippedped = False

    def __init__(self, iterable):
        points_tuple = tuple((x, y) for x, y in iterable)
        self.points = Shape.translate_points(points_tuple)
        self.poly = Polygon(self.points)
        self.is_valid = self.points and self.poly.is_valid
        self.area = self.poly.area
        self.is_simple = self.poly.is_simple
        self.has_colinear = self.find_colinear()
        self.edges = edges_as_sets(self.points)

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, repr(self.points))

    def __iter__(self):
        return iter(self.points)

    def __len__(self):
        return len(self.points)

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        """
        The smaller hash of the item itself
        (calculated from the frozenset of edges)
        and the hashes of its 3 rotated siblings
        """
        p = self
        h = hash(p.edges)
        for _ in range(3):
            p = p.rotated()
            h = min(h, hash(p.edges))
        if Shape.remove_flippedped:
            f = self.flipped()
            h = min(h, hash(f.edges))
            for _ in range(3):
                f = f.rotated()
                h = min(h, hash(f.edges))
        return h
    
    
    def find_colinear(self):
        for i, (x2, y2) in enumerate(self.points):
            x1, y1 = self.points[i - 1]
            x0, y0 = self.points[i - 2]
            if points_are_colinear(x0, y0, x1, y1, x2, y2):
                return True
        return False


    def rotated(self):
        """Return a Shape rotated clockwise"""
        return Shape((-y, x) for x, y in self)

    def flipped(self):
        """Return a Shape flippedped"""
        return Shape((-x, y) for x, y in self)

    @cache
    @staticmethod
    def translate_points(points):
        """Return tuples translated to 0, 0"""
        minX = min(s[0] for s in points)
        minY = min(s[1] for s in points)
        return tuple((x - minX, y - minY) for x, y
                            in points)
        
    def draw(self, s):
        """
        draw the the shape with "size" s (scale factor)
        beware the stroke_width will be scaled by s
        """
        with py5.push_matrix(), py5.begin_closed_shape():
            py5.scale(s)
            py5.vertices(self.points)


@cache
def points_are_colinear(ax, ay, bx, by, cx, cy,
                        tolerance=py5.EPSILON):
    """
    Test for colinearity by calculating the area
    of a triangle formed by the 3 points.
    """
    area = triangle_area((ax, ay), (bx, by), (cx, cy))
    return abs(area) < tolerance

@cache
def triangle_area(a, b, c):
    area = (a[0] * (b[1] - c[1]) +
            b[0] * (c[1] - a[1]) +
            c[0] * (a[1] - b[1]))
    return area

                        
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
    poly_points = tuple(poly_points)
    return pairwise(poly_points) + [(poly_points[-1], poly_points[0])]

def pairwise(iterable):
    from itertools import tee
    "s -> (s0, s1), (s1, s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return list(zip(a, b))
