# WIP - partition a grid?

from itertools import product, combinations, permutations

import py5

grid = product((-1, 0, 1), (-1, 0, 1))  # 3X3
pts = list(grid)
space, border = 60, 0

def setup():
    global shapes
    py5.size(900, 800)
    py5.background(200)
    py5.stroke_join(py5.ROUND)
    W = int(py5.width - border * 2) // space
    H = int(py5.height - border * 2) // space
    borders = [
        set( ((-1, -1), ( 0, -1), ( 1, -1)) ),
        set( ((-1,  1), ( 0,  1), ( 1,  1)) ),
        set( ((-1, -1), (-1,  0), (-1,  1)) ),
        set( (( 1, -1), ( 1,  0), ( 1,  1)) ),        
        ]
    perms = list(permutations(pts, 3))
    shapes = []
    for shp in perms:
        if (
            shp[0] != (0, 0) and
            shp[-1] != (0, 0) and
            shp[::-1] not in shapes and
            set(shp) not in borders
            ):
            shapes.append(shp)    
    
    print(W * H, len(shapes))

    i = 0
    scale_factor = space * 0.25
    for y, x in product(range(H), range(W)):
        if i < len(shapes):
            shp = shapes[i]
            with py5.push_matrix():
                py5.translate(border + space * x + space / 2,
                              border + space * y + space / 2)
                
                py5.no_fill()
                with py5.push_matrix():
                    py5.scale(scale_factor)
                    py5.stroke_weight(3 / scale_factor)
                    py5.stroke(255)
                    py5.points(pts)
                    py5.stroke(0)
                    with py5.begin_shape():
                        py5.vertices(shp)
        i += 1



def poly_area(points):
    points = list(points)
    area = 0.0
    for (ax, ay), (bx, by) in zip(points, points[1:] + [points[0]]):
        area += ax * by
        area -= bx * ay
    return area / 2.0

def key_pressed():
    py5.save_frame('###.png')



py5.run_sketch(block=False)
