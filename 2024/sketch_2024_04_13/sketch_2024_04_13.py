# Alexandre B A Villares - https://abav.lugaralgum.com/
# To run this you will need Processing 3.5.4 + Python mode, instructions at: 
# https://abav.lugaralgum.com/como-instalar-o-processing-modo-python/index-EN.html

"""
Polygons on a 3 x 2, grid
"""

from itertools import product, combinations, permutations

from shapely import Polygon

from villares.line_geometry import edges_as_sets, poly_area, triangle_area, is_poly_self_intersecting



space, border = 60, 30
name = "shapes"

def setup():
    size(850, 790)  # 24 x 22
    grid = product((-1, -0.32, 0.32, 1), (-1, 1))  # 3X3
    pts = list(grid)
    polys = []
    for i in range(3, 7): # 3 to 7, as no non-intersecting polys exist with 8 or 9 pts.
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
            draw_scaled_poly(polys[i], space * 0.4)
            pop_matrix()
            i += 1
    end_record()  # end PDF export
    save_frame(name + '.png')

def draw_scaled_poly(p_list, s):
    begin_shape()
    for p in p_list:
        vertex(p[0] * s, p[1] * s)
    end_shape(CLOSE)

def create_polys(pts, num_pts=None, allow_intersecting=False):
    """
    Generate all distinct shapes/polygons from a collection of pts.
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
            if Polygon(poly).is_valid
            ]