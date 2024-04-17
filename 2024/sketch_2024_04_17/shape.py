from functools import cache
from itertools import permutations

from line_profiler import profile
from shapely import Polygon
import py5

class Shape(object):
    
    remove_flipped = False
    
    @profile
    def __init__(self, iterable):
        points_tuple = tuple((x, y) for x, y in iterable)
        self.points = translated_points(points_tuple)
        self.poly = Polygon(self.points)
        self.is_valid = self.points and self.poly.is_valid
        self.area = self.poly.area
        self.is_simple = self.poly.is_simple
        self.has_colinear = self.find_colinear()
        self.edges = edges_as_sets(self.points)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.points})'

    def __iter__(self):
        return iter(self.points)

    def __len__(self):
        return len(self.points)

    def __eq__(self, other):
        return hash(self) == hash(other)

    @profile
    def __hash__(self):
        """
        The smaller hash of the item itself
        (calculated from the frozenset of edges)
        and the hashes of its 3 rotated siblings
        """
        pts = self.points
        hashes = [hash(self.edges)]
        if Shape.remove_flipped:
            fpts = translated_points(flipped_points(pts))
            fedges = edges_as_sets(fpts)
            hashes.append(hash(fedges))
            for _ in range(3):
                pts = translated_points(rotated_points(pts))
                edges = edges_as_sets(pts)
                hashes.append(hash(edges))
                fpts = translated_points(flipped_points(pts))
                fedges = edges_as_sets(fpts)
                hashes.append(hash(fedges))
        else:
            for _ in range(3):
                pts = translated_points(rotated_points(pts))
                edges = edges_as_sets(pts)
                hashes.append(hash(edges))
        return min(hashes)
    
    def find_colinear(self):
        for i, (x2, y2) in enumerate(self.points):
            x1, y1 = self.points[i - 1]
            x0, y0 = self.points[i - 2]
            if points_are_colinear(x0, y0, x1, y1, x2, y2):
                return True
        return False
        
    def draw(self, s):
        """
        draw the the shape with "size" s (scale factor)
        beware the stroke_width will be scaled by s
        """
        with py5.push_matrix(), py5.begin_closed_shape():
            py5.scale(s)
            py5.vertices(self.points)


def flipped_points(points):
    """Return tuples with points flipped"""
    return tuple((-x, y) for x, y in points)

@cache
def rotated_points(points):
    """Return tuples with points rotated"""
    return tuple((-y, x) for x, y in points)

@cache
def translated_points(points):
    """Return tuples translated to 0, 0"""
    minX = min(s[0] for s in points)
    minY = min(s[1] for s in points)
    return tuple((x - minX, y - minY) for x, y
                        in points)

def points_are_colinear(ax, ay, bx, by, cx, cy,
                        tolerance=py5.EPSILON):
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

@cache
def edges_as_sets(points_tuple):
    """
    Return a frozenset of poly edges as frozensets of 2 points.
    """
    return frozenset(frozenset(edge) for edge in poly_edges(points_tuple))

def poly_edges(poly_points):
    """
    Return a tuple of edges (tuples containing pairs of points)
    for a points that represent a closed polygon
    """
    return pairwise(poly_points) + ((poly_points[-1], poly_points[0]),)

def pairwise(iterable):
    from itertools import tee
    "s -> (s0, s1), (s1, s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return tuple(zip(a, b))

@profile
def all_from_points(pts, num_pts=None, remove_flipped=False):
    """
    Generate all distinct shapes, simple (not self-intersecting)
    polygons from a collection of points.
    """
    Shape.remove_flipped = remove_flipped
    num_pts = num_pts or len(pts)
    all_polys = list(permutations(pts, num_pts))
    tested, shapes = set(), []
    for poly in all_polys:
        s = Shape(poly)
        if (s.is_simple and
            not s.has_colinear and
            s not in tested):
            tested.add(s)
            shapes.append(s)
    return shapes