# Alexandre B A Villares - https://abav.lugaralgum.com/
# To run this you will need py5 imported mode https://abav.lugaralgum.com/como-instalar-py5/index-EN.html

from itertools import product, combinations, permutations

from shapely import Polygon

space, border = 100, 50
name = "shapes"

def setup():
    size(700, 400)  # 24 x 22
    grid = product((-1, 1), (-1, 1))  # 3X3
    pts = list(grid) + [(0, 0)]
    polys = []
    for i in range(3, 8): # 3 to 7, as no non-intersecting polys exist with 8 or 9 pts.
        polys.extend(create_polys(pts, i))
    polys.sort(key=poly_area)
    print(len(polys))
    W = (width - border * 2) // space
    H = (height - border * 2) // space
    println("Cols: {} Rows: {} Visible grid: {}".format(W, H, W * H))
   
    f = create_graphics(width * 10,  # for High res PDF export
                       height * 10,   
                       PDF, name + '.pdf')
    begin_record(f) # begin PDF export
    f.scale(10)
    stroke_join(ROUND)
    background(240)
    i = 0
    for y, x in product(range(H), range(W)):
        if i < len(polys):
            push_matrix()
            translate(border  + space / 2 + space * x,
                    border + space / 2 + space * y)
            fill(0)
            no_stroke()
            draw_scaled_poly(polys[i], space * 0.4)
            pop_matrix()
            i += 1
    end_record()  # end PDF export
    save_frame(name + '.png')

def draw_scaled_poly(p_list, s):
    no_stroke()
    begin_shape()
    for p in p_list:
        vertex(p[0] * s, p[1] * s)
    end_shape(CLOSE)
    stroke(255)
    stroke_weight(5)
    for p in p_list:
        point(p[0] * s, p[1] * s)
    

def create_polys(pts, num_pts=None, allow_intersecting=False):
    """
    Generate all distinct shapes/polygons from a collection of pts.
    
    WIP from a prevevious sketch...
    I have to get the colinear points elimination code back...
    """
    num_pts = num_pts or len(pts)
    all_polys = list(permutations(pts, num_pts))
    tested, polys = set(), []
    for poly in all_polys:
        edges = edges_as_sets(poly)
        if edges not in tested:
            tested.add(edges)
            polys.append(poly)
    return [poly for poly in polys
            if Polygon(poly).is_valid]


# def points_are_colinear(ax, ay, bx, by, cx, cy,
#                         tolerance=EPSILON):
#     """
#     Test for colinearity by calculating the area
#     of a triangle formed by the 3 points.
#     """
#     area = triangle_area((ax, ay), (bx, by), (cx, cy))
#     return abs(area) < tolerance
# 
# 
# def triangle_area(a, b, c):
#     area = (a[0] * (b[1] - c[1]) +
#             b[0] * (c[1] - a[1]) +
#             c[0] * (a[1] - b[1]))
#     return area

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

def pairwise(iterable):
    from itertools import tee
    "s -> (s0, s1), (s1, s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return list(zip(a, b))

def poly_area(points):
    return Polygon(points).area