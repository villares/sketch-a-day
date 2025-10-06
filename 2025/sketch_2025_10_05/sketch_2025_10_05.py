# Alexandre B A Villares - https://abav.lugaralgum.com/
# To run this you will need py5 https://abav.lugaralgum.com/como-instalar-py5/index-EN.html


from functools import cache
from itertools import permutations
from itertools import product

from shapely import Polygon
import py5


grid = product((0, 1, 2), (0, 1, 2))  # 3X3
pts = list(grid)
space, border = 50, 25
name = "out"

def setup():
    global shapes
    py5.size(1350, 300)
    W = 25 #int(py5.width - border * 2) // space
    H = 5 #int(py5.height - border * 2) // space

#     shapes = []
#     tm = 0
#     for i in [3, 4, 5, 6, 7]: # 3 to 7, as no non-intersecting shapes exist with 8 or 9 pts.
#         m = py5.millis()
#         shapes.extend(all_from_points(pts, i)) #, remove_flipped=True))
#         dt = py5.millis() - m
#         print(i, dt)
#         tm += dt
#     print(f'total: {tm} millisegundos')
#     #   
#     py5.save_pickle(shapes, 'out.pickle')

    shapes = py5.load_pickle('out.pickle')
    print(f'shapes: {len(shapes)} Cols: {W} Rows: {H} Visible grid: {W*H}')

    def shape_key(s):
        return len(s), s.area
    
    shapes.sort(key=shape_key)


    f = py5.create_graphics(py5.width * 10,  # for big PDF export
                            py5.height * 10, py5.PDF, name + '.pdf')
    # begin PDF export
    py5.begin_record(f) # begin PDF export
    py5.color_mode(py5.HSB)
    f.scale(10)
    py5.stroke_join(py5.ROUND)
    py5.background(240)
    py5.no_stroke()
#     i = 0
#     for x, y in product(range(W), range(H)):
#         if i < len(shapes):
#             shp = shapes[i]

    x = y = 0
    for i, shp in enumerate(shapes):
            with py5.push_matrix():
                py5.translate(border + space * x,
                              border + space * y)
                py5.fill(len(shp) * 35, 255, 150)
                #py5.fill(shp.area * 30 % 255, 255, 150)
                shp.draw(space * 0.4)
                py5.fill('black')
                py5.text(i, 0, 0)
            y += 1
            if y > 4 or i == 75:
                y = 0
                x += 1
#             i += 1   
    # end PDF export
    py5.end_record()  
    py5.save_frame(name + '.png')


class Shape(object):
    
    remove_flipped = False
    
    #@profile
    def __init__(self, iterable):
        points_tuple = tuple((x, y) for x, y in iterable)
        self.points = translated_points(points_tuple)
        self.poly = Polygon(self.points)
        self.is_valid = len(self.points) and self.poly.is_valid
        self.area = self.poly.area
        self.is_simple = self.poly.is_simple
        self.is_clean = self.check_clean()
        self.edges = edges_as_sets(self.points)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.points})'

    def __iter__(self):
        return iter(self.points)

    def __len__(self):
        return len(self.points)

    def __eq__(self, other):
        return hash(self) == hash(other)

    #@profile
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
    
#     def check_clean(self):
#         return self.poly.buffer(0) == self.poly.buffer(0).simplify(0, preserve_topology=True)
    
    def check_clean(self):
        for i, (x2, y2) in enumerate(self.points):
            x1, y1 = self.points[i - 1]
            x0, y0 = self.points[i - 2]
            if points_are_colinear(x0, y0, x1, y1, x2, y2):
                return False
        return True
        
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
    min_x, min_y = tuple(map(min, zip(*points)))    
    return tuple((x - min_x, y - min_y)
                 for x, y in points)

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
    #points_tuple = tuple(map(tuple, points_tuple))
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

#@profile
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
        if (s not in tested and
            s.is_simple and
            s.is_clean 
            ):
            tested.add(s)
            shapes.append(s)
    return shapes

py5.run_sketch(block=False)
