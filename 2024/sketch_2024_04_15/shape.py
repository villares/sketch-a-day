from collections import namedtuple
from functools import cache

from shapely import Polygon
import py5


Point = namedtuple('Point', 'x y') 

class Shape(object):
    
    remove_flipped = False

    def __init__(self, iterable):
        self.points = tuple([Point(*s) for s in iterable])
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
        p = self.translate()
        h = hash(p.edges)
        for _ in range(4):
            rtp = p.rotate().translate()
            h = min(h, hash(rtp.edges))
        if Shape.remove_flipped:
            fp = self.flip().translate()
            h = min(h, hash(fp.edges))
            for _ in range(3):
                rtfp = fp.rotate().translate()
                h = min(h, hash(rtfp.edges))
        return h
    
    
    def find_colinear(self):
        for i, (x2, y2) in enumerate(self.points):
            x1, y1 = self.points[i - 1]
            x0, y0 = self.points[i - 2]
            if points_are_colinear(x0, y0, x1, y1, x2, y2):
                return True
        return False


    def rotate(self):
        """Return a Shape rotated clockwise"""
        return Shape((-y, x) for x, y in self)

    def flip(self):
        """Return a Shape flipped"""
        return Shape((-x, y) for x, y in self)

    def translate(self):
        """Return a Shape Translated to 0,0"""
        minX = min(s.x for s in self)
        minY = min(s.y for s in self)
        return Shape((x - minX, y - minY) for x, y in self)
# 
#     def raise_order(self, size_limit=3):
#         """Return a list of higher order Polyonominos evolved from self"""
#         shapes = []
#         for s in self:
#             adjacents = (adjacent for adjacent in (
#                 (s.x + 1, s.y),
#                 (s.x - 1, s.y),
#                 (s.x, s.y + 1),
#                 (s.x, s.y - 1),
#             ) if adjacent not in self)
#             for adjacent in adjacents:
#                 new_shape = translate(Shape(list(self) + [adjacent]))
#                 if shape_under_limit(new_shape, size_limit):
#                     shapes.append(new_shape)
#         return shapes

    @staticmethod
    def shape_under_limit(shp, size_limit):
        return (max(s.x for s in shp) <= size_limit and 
                max(s.y for s in shp) <= size_limit)

    def render(self):
        """
        Returns a string map representation of the Shape
        """
        p = self.translate()
        order = len(p)
        return ''.join(
            ["\n %s" % (''.join(
                ["X" if (x, y) in p.points else "-" for x in range(order)]
            )) for y in range(order)]
        )
        
    def draw(self, s):
        """
        draw the the shape with "size" s (scale factor)
        beware the stroke_width will be scaled by s
        """
        with py5.push_matrix(), py5.begin_closed_shape():
            py5.scale(s)
            py5.vertices(self.points)
#         with py5.push():
#             py5.scale(s)
#             py5.stroke(255, 255, 0)
#             py5.stroke_weight(5 / s)
#             py5.points(self.points)

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
