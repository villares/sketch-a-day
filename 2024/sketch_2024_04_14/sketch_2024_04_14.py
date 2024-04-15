# Alexandre B A Villares - https://abav.lugaralgum.com/
# To run this you will need py5 imported mode https://abav.lugaralgum.com/como-instalar-py5/index-EN.html

from itertools import product, combinations, permutations

from shape import Shape

space, border = 50, 50
name = "shapes"

def setup():
    size(700, 200)  
    grid = product((-1, 0, 1), (-1, 0, 1))  # 3X3
    pts = list(grid)
    polys = []
    for i in [4, 5]: # 3 to 7, as no non-intersecting polys exist with 8 or 9 pts.
        polys.extend(create_polys(pts, i))
    polys.sort(key=shape_area)
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
            polys[i].draw(space * 0.4)
            pop_matrix()
            i += 1
    end_record()  # end PDF export
    save_frame(name + '.png')

def create_polys(pts, num_pts=None, allow_intersecting=False):
    """
    Generate all distinct shapes/polygons from a collection of pts.
    
    WIP from a prevevious sketch...
    """
    num_pts = num_pts or len(pts)
    all_polys = list(permutations(pts, num_pts))
    tested, polys = set(), []
    for poly in all_polys:
        s = Shape(poly)
        edges = edges_as_sets(poly)
        if (
            s.is_simple and
            not s.has_colinear
            and s not in tested
            ):
            tested.add(s)
            polys.append(s)
    
    #print(len(polys))
    return polys

                            
                        
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

def shape_area(p):
    return p.area


