from itertools import product, combinations, permutations

from random import choice, sample, shuffle

from villares.line_geometry import (is_poly_self_intersecting,
                                    triangle_area,
                                    is_poly_convex,
                                    edges_as_sets,
                                    poly_area
                                    )
from villares.gif_export import gif_export
add_library('gifAnimation')

def setup():
    global grade, squares
    size(500, 500)
    grade = list(product(range(50, 500, 100), repeat=2))    
    frameRate(2)
    all_polys = permutations(grade, 4)
    
    t = millis()
    tested, polys = set(), []
    for poly in all_polys:
        edges = edges_as_sets(poly)
        if edges not in tested and edges:
            tested.add(edges)
            polys.append(poly)
            
    squares = [p for p in polys if
               sides_equal(p) and
               is_rectangle(p)
                ]
    
    print(millis() - t)
    # shuffle(squares)
    print(len(squares))  # 50 squares
    
        
def draw():
    colorMode(RGB)
    background(200, 200, 180)
    colorMode(HSB)
    fill(0)
    for x, y in grade:
        circle(x, y, 5)
    fill(255, 100)
    
    four_squares = (squares[(frameCount + i) % len(squares)] for i in range(4))
    for p in four_squares:
        fill(poly_color(p), 100)
        beginShape()
        for x, y in p:
            vertex(x, y)
        endShape(CLOSE)
        fill(poly_color(p))
        for x, y in p:
            circle(x, y, 10)
    # if frameCount % len(squares) == 0:
    #     gif_export(GifMaker, finish='True')
    #     exit()
    # else:
    #     gif_export(GifMaker, 'output', delay=400, quality=0)

def poly_color(p):
    return color(poly_area(p) % 256, 200, 200)
                
def sq_dist(a, b):
    xa, ya = a
    xb, yb = b
    return (xa - xb) * (xa - xb) + (ya - yb) * (ya - yb)

def sides_equal(poly_points):
    a, b, c, d = poly_points
    ab = sq_dist(a, b)
    bc = sq_dist(b, c)
    return (ab == bc) 

def is_rectangle(poly_points):
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = poly_points
    return not (((x2 - x1) * (x3 - x2) + (y2-y1) * (y3 - y2)) or
              ((x3 - x2) * (x4 - x3) + (y3 - y2) * (y4 - y3)) or
              ((x4 - x3) * (x1 - x4) + (y4 - y3) * (y1 - y4)) or
              ((x1 - x4) * (x2 - x1) + (y1 - y4) * (y2 - y1)))
