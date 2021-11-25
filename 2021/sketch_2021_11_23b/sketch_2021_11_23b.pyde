# Alexandre B A Villares - https://abav.lugaralgum.com/
# To run this you will need Processing 3.5.4 + Python mode, instructions at: 
# https://abav.lugaralgum.com/como-instalar-o-processing-modo-python/index-EN.html

"""
Hexagons on a 3 x 3, grid
"""

add_library('pdf')
from itertools import product, combinations, permutations
from villares.line_geometry import edges_as_sets, simple_intersect
import pickle

space, border = 50, 50
name = "polys"

def setup():
    # 1200 x 650 for 6 pts (241)
    # 1050, 500 for 7 pts (152)
    # 1000 450 FOR 8 (126)
    size(1400, 750)
    grid = product((-1, 0, 1), (-1, 0, 1))  # 3X3
    points = list(grid)
    polys = create_polys(points, 6)
    print(len(polys))
    W = (width - border * 2) // space
    H = (height - border * 2) // space
    println("Cols: {} Rows: {} Visible grid: {}".format(W, H, W * H))
    # High res PDF export
    f = createGraphics(width * 10, height * 10,
                       PDF, name + '.pdf')
    beginRecord(f) # begin PDF export
    f.scale(10)
    strokeJoin(ROUND)
    # start drawing
    background(240)
    i = 0
    for y in range(H):
        for x in range(W):
            if i < len(polys):
                pushMatrix()
                translate(border / 2 + space + space * x,
                          border / 2 + space + space * y)
                fill(0)
                draw_poly(scale_poly(polys[i], space * 0.4))
                popMatrix()
                i += 1
    # end PDF export
    endRecord()
    saveFrame(name + '.png')

def draw_poly(p_list, closed=True):
    """Draw a polygon from a list of 2D tuples"""
    beginShape()
    for p in p_list:
            vertex(p[0], p[1])
    if closed:
        endShape(CLOSE)
    else:
        endShape()


def scale_poly(p_list, s):
    """Return a scaled version of a list of points (as tuples)."""
    return [(p[0] * s, p[1] * s) for p in p_list]


def create_polys(points, num_points=None, allow_intersecting=False):
    """
    Generate all distinct polygons from points.
    Requires itertools.permutations and villare.line_geometry's
    is_poly_self_intersecting() and edges_as_sets()
    """
    num_points = num_points or len(points)
    all_polys = list(permutations(points, num_points))
    tested, polys = set(), []
    for poly in all_polys:
        edges = edges_as_sets(poly)
        if edges not in tested and edges:
            tested.add(edges)
            polys.append(poly)
    return [poly for poly in polys
           if (allow_intersecting or not is_poly_self_intersecting(poly))
            and not collapsed(poly)
            ]
    
def is_poly_self_intersecting(poly_points):
    if len(poly_points) < 4:
        return False
    edges = poly_edges(poly_points)
    for i, a in enumerate(edges):
        for b in edges[i + 2:]:
            if simple_intersect(shrink(a), shrink(b)):
                    return True
    return False

def shrink(seg):
    (xa, ya), (xb, yb) = seg
    new_a = lerp(xa, xb, 0.1), lerp(ya, yb, 0.1)
    new_b = lerp(xa, xb, 0.9), lerp(ya, yb, 0.9)
    return (new_a, new_b)

def collapsed(poly):
    for i, c in enumerate(poly):
        a = poly[i - 2]
        b = poly[i - 1]
        if triangle_area(a, b, c) == 0:
            return True
    return False

def triangle_area(a, b, c):
    return (a[0] * (b[1] - c[1]) +
            b[0] * (c[1] - a[1]) +
            c[0] * (a[1] - b[1]))
    
    
def edges_as_sets(poly_points, frozen=True):
    """
    Return a (frozen)set of poly edges as frozensets of 2 points.
    """
    if frozen:
        return frozenset(frozenset(edge) for edge in poly_edges(poly_points))
    else:
        return set(frozenset(edge) for edge in poly_edges(poly_points))

def poly_edges(poly_points):
    return pairwise(poly_points) + [(poly_points[-1], poly_points[0])]


def pairwise(iterable):
    from itertools import tee
    "s -> (s0, s1), (s1, s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)  # this is Python 2.7, so a list...
