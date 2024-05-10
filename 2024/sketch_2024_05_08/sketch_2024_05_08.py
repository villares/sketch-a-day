from itertools import product, combinations, permutations

import py5
from shapely import Polygon

grid = product((-1, 0, 1, 2), (-1, 0, 1, 2))  # 3X3
pts = list(grid)
edge = (
    (-1, -1), ( 0, -1), ( 1, -1), (2, -1), ( 2,  0),
    ( 2,  1), (2, 2), ( 1,  2), (0, 2), (-1, 2),
    (-1,  1), (-1,  0),
)
    
space, border = 45, 0

def setup():
    global shapes
    py5.size(1640, 920)
    py5.background(200)
    py5.color_mode(py5.HSB)

    py5.stroke_join(py5.ROUND)
    W = int(py5.width - border * 2) // space
    H = int(py5.height - border * 2) // space
    
    perms = list(combinations(range(12), 2))
    shapes = []
    for a, b in perms:
        shp0 = edge[a:b+1]
        area0 = poly_area(shp0)
        if (area0 != 0 and area0 != 9):
            comp_shp0 = edge[:a + 1] + edge[b:]
            shapes.append((shp0, comp_shp0))
        for c in ((0,0), (0, 1), (1, 1), (1, 0)):
            shp1 = (c,) + edge[a:b+1]
            area1 = poly_area(shp1)
            if area1 != area0:
                comp_shp1 = edge[:a + 1] + (c,) + edge[b:]
                shapes.append((shp1, comp_shp1))
            for d in ((0,0), (0, 1), (1, 1), (1, 0)):
                shp2 = (c, d) + edge[a:b+1]
                sp = Polygon(shp2)
                area2 = poly_area(shp2)
                if (sp.is_simple and
                    area2 != area1 and
                    area2 != area0):
                    comp_shp2 = edge[:a + 1] + (d, c) + edge[b:]
                    shapes.append((shp2, comp_shp2))            


    print(W * H, len(shapes))

    i = 0
    scale_factor = space * 0.25
    for y, x in product(range(H), range(W)):
        if i < len(shapes):
            shps = shapes[i]
            with py5.push_matrix():
                py5.translate(border + space * x + space / 2,
                              border + space * y + space / 2)
                py5.no_fill()
                with py5.push_matrix():
                    py5.scale(scale_factor)
                    py5.stroke_weight(2 / scale_factor)
                    py5.stroke(0)
                    j = 0
                    for shp in shps:
                        py5.fill((i * 256/16 + j * 256/2) % 255) #, 255, 255, 100) 
                        with py5.begin_closed_shape():
                            py5.vertices(shp)
                        j = 1
                    py5.stroke(255)
                    py5.points(pts)

        i += 1



def poly_area(points):
    points = list(points)
    area0 = 0.0
    for (ax, ay), (bx, by) in zip(points, points[1:] + [points[0]]):
        area0 += ax * by
        area0 -= bx * ay
    return area0 / 2.0

def key_pressed():
    py5.save_frame('###.png')



py5.run_sketch(block=False)

