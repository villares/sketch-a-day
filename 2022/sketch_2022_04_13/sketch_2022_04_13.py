from itertools import product
from random import sample
from math import atan2
import py5

def setup():
    py5.size(600, 600)
    py5.no_fill()
    py5.no_loop()

def draw():
    py5.background(200)
    grid = list(product(range(200, py5.width - 150, 100), repeat=2))    
    shapes = [clockwise_sort(sample(grid, 5))]
    for _ in range(10):
        shapes.append(offset(shapes[-1], 20))        
    for i, poly in enumerate(reversed(shapes)):
        py5.fill(i * 25, 100)
        draw_poly(poly)
    py5.fill(0)
    for x, y in grid:
        py5.circle(x, y, 5)

def draw_poly(poly):
    with py5.begin_closed_shape():
        py5.vertices(poly)

def key_pressed():
    py5.redraw()

def offset(poly, off_d):
    result = []
    triples = zip([poly[-1]] + poly[:-1], poly, poly[1:] + [poly[0]])
    for i, ((xa, ya), (xb, yb), (xc, yc)) in enumerate(triples):
        r = -off_d if i == 0 else off_d
        ang0 = py5.atan2(ya - yb, xa - xb)
        ang1 = py5.atan2(yb - yc, xb - xc)
        ang = (ang0 + ang1) / 2 + py5.HALF_PI
        #if ang > py5.PI: ang = ang - py5.PI; print('*')
        off_x = r * py5.cos(ang)
        off_y = r * py5.sin(ang)
        result.append((xb + off_x, yb + off_y))
    return result

def centeroid(pts):
    x, y = zip(*pts)
    return sum(x) / len(x), sum(y) / len(y)

def clockwise_sort(xy_pairs):
    # https://stackoverflow.com/questions/51074984/sorting-according-to-clockwise-point-coordinates
    centroid_x, centroid_y = centeroid(xy_pairs)
    xy_sorted = sorted(xy_pairs,
                       key = lambda p: atan2((p[1] - centroid_y), (p[0] - centroid_x)))
    xy_sorted_xy = [coord for pair in list(zip(*xy_sorted)) for coord in pair]
    half_len = int(len(xy_sorted_xy) / 2)
    return list(zip(xy_sorted_xy[:half_len], xy_sorted_xy[half_len:]))

py5.run_sketch()
