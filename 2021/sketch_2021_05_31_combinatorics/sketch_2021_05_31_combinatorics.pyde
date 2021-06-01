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
    global grade, combos
    size(500, 500)
    grade = list(product(range(100, 500, 100), repeat=2))    
    frameRate(2)
    all_polys = permutations(grade, 4)
    
    t = millis()
    tested, polys = set(), []
    for poly in all_polys:
        edges = edges_as_sets(poly)
        if edges not in tested and edges:
            tested.add(edges)
            polys.append(poly)
    combos = [p for p in polys
              if is_poly_para(p)
              and not is_poly_self_intersecting(p)
              and is_poly_good(p)
              ]
    
    print(millis() - t)
    # shuffle(combos)
    print(len(combos))
    
        
def draw():
    colorMode(RGB)
    background(200, 200, 180)
    colorMode(HSB)
    fill(0)
    for x, y in grade:
        circle(x, y, 5)
    fill(255, 100)
    
    polys = (combos[(frameCount + i) % len(combos)] for i in range(4))
    for p in polys:
        fill(poly_color(p), 100)
        beginShape()
        for x, y in p:
            vertex(x, y)
        endShape(CLOSE)
        fill(poly_color(p))
        for x, y in p:
            circle(x, y, 10)
    if frameCount % len(combos) == 0:
        gif_export(GifMaker, finish='True')
        exit()
    else:
        gif_export(GifMaker, 'output', delay=400, quality=0)

def poly_color(p):
    return color(poly_area(p) % 256, 200, 200)
                
def is_poly_good(poly_points):
    a, b, c, d = poly_points
    return (triangle_area(a, b, c) and
            triangle_area(b, c, d) and
            triangle_area(c, d, a))

def sq_dist(a, b):
    xa, ya = a
    xb, yb = b
    return (xa - xb) * (xa - xb) + (ya - yb) * (ya - yb)

def is_poly_para(poly_points):
    a, b, c, d = poly_points
    return (sq_dist(a, b) == sq_dist(c, d)
          and sq_dist(a, d) == sq_dist(b, c)) 
    
    
     
