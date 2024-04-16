# Alexandre B A Villares - https://abav.lugaralgum.com/
# To run this you will need py5 https://abav.lugaralgum.com/como-instalar-py5/index-EN.html

from itertools import product, combinations, permutations

import py5

from shape import Shape

grid = product((0, 1, 2), (0, 1, 2))  # 3X3
pts = list(grid)
space, border = 50, 25
name = "shapes"

def setup():
    global shapes
    py5.size(350, 250)
    W = int(py5.width - border * 2) // space
    H = int(py5.height - border * 2) // space

    shapes = []
    for i in [4]: # 3 to 7, as no non-intersecting shapes exist with 8 or 9 pts.
        shapes.extend(create_shapes(pts, i))
    
    def shape_area(s):
        return s.area
    shapes.sort(key=shape_area)
    
    print(f'shapes: {len(shapes)} Cols: {W} Rows: {H} Visible grid: {W*H}')

    f = py5.create_graphics(py5.width * 10,  # for big PDF export
                            py5.height * 10, py5.PDF, name + '.pdf')
    # begin PDF export
    py5.begin_record(f) 
    f.scale(10)
    py5.stroke_join(py5.ROUND)
    py5.background(240)
    py5.no_stroke()
    i = 0
    for y, x in product(range(H), range(W)):
        if i < len(shapes):
            shp = shapes[i]
            with py5.push_matrix():
                py5.translate(border + space * x,
                              border + space * y)
                py5.fill(0, 0, 100)
                shp.draw(space * 0.4)
                py5.fill(255, 0, 0)
            i += 1
    # end PDF export 
    py5.end_record()  
    py5.save_frame(name + '.png')


def create_shapes(pts, num_pts=None, allow_intersecting=False):
    """
    Generate all distinct shapes, simple* polygons
    from a collection of points.
    
    * not self-intersecting
    """
    num_pts = num_pts or len(pts)
    all_shapes = list(permutations(pts, num_pts))
    tested, shapes = set(), []
    for poly in all_shapes:
        s = Shape(poly)
        if (
            s.is_simple and
            not s.has_colinear and
            #s.is_valid and
            s not in tested
            ):
            tested.add(s)
            shapes.append(s)
    return shapes


py5.run_sketch(block=False)