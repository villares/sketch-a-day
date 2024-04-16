# Alexandre B A Villares - https://abav.lugaralgum.com/
# To run this you will need py5 imported mode https://abav.lugaralgum.com/como-instalar-py5/index-EN.html

from itertools import product, combinations, permutations

import py5

from shape import Shape

space, border = 50, 12.5
name = "shapes"

def setup():
    global polys
    py5.size(600, 400)  
    grid = product((0, 1, 2), (0, 1, 2))  # 3X3
    pts = list(grid)
    polys = []
    for i in [4]: # 3 to 7, as no non-intersecting polys exist with 8 or 9 pts.
        polys.extend(create_polys(pts, i))
    polys.sort(key=shape_area)
    W = int(py5.width - border * 2) // space
    H = int(py5.height - border * 2) // space
    print(f'Polys: {len(polys)} Cols: {W} Rows: {H} Visible grid: {W*H}')
    f = py5.create_graphics(
        py5.width * 10,  # for big PDF export
        py5.height * 10,   
        py5.PDF, name + '.pdf'
        )
    py5.begin_record(f) # begin PDF export
    f.scale(10)
    py5.stroke_join(py5.ROUND)
    py5.background(240)
    py5.no_stroke()
    i = 0
    for y, x in product(range(H), range(W)):
        if i < len(polys):
            shp = polys[i]
            with py5.push_matrix():
                py5.translate(border  + space / 2 + space * x,
                              border + space / 2 + space * y)
                py5.fill(0, 0, 32)
                shp.draw(space * 0.4)
                py5.fill(255, 0, 0)
#                 print(shp.points[0])
#                 cx, cy = shp.points[0]
#                 py5.circle(cx * space * 0.4, cy * space * 0.4, 4)
#                 print(shp)
            i += 1
    py5.end_record()  # end PDF export
    py5.save_frame(name + '.png')

def create_polys(pts, num_pts=None, allow_intersecting=False):
    """
    Generate all distinct shapes/polygons from a collection of pts.
    """
    num_pts = num_pts or len(pts)
    all_polys = list(permutations(pts, num_pts))
    tested, polys = set(), []
    for poly in all_polys:
        s = Shape(poly)
        if (
            s.is_simple and
            not s.has_colinear and
            #s.is_valid and
            s.edges not in tested
            ):
            tested.add(s.edges)
            tested.add(s.edges)

            polys.append(s)
    
    return polys

                        
def shape_area(p):
    return p.area

py5.run_sketch(block=False)
