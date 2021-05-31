from itertools import product, combinations, permutations
from villares.line_geometry import (is_poly_self_intersecting,
                                    poly_area,
                                    triangle_area,
                                    is_poly_convex,
                                    edges_as_sets,
                                    )
from random import choice, sample, shuffle

def setup():
    global grade, combos
    size(500, 500)
    grade = list(product(range(100, 500, 100), repeat=2))    
    frameRate(2)
    all_polys = permutations(grade, 4)
    tested, polys = set(), []
    for poly in all_polys:
        edges = edges_as_sets(poly)
        if edges not in tested and edges:
            tested.add(edges)
            polys.append(poly)
    combos = [p for p in polys
              if not is_poly_self_intersecting(p)
              and is_poly_very_good(p)
              ]
    shuffle(combos)
    print(len(combos))
    
        
def draw():
    colorMode(RGB)
    background(200, 200, 180)
    colorMode(HSB)
    fill(0)
    for x, y in grade:
        circle(x, y, 5)
    fill(255, 100)
    f = frameCount % len(combos)
    polys = combos[f:f+3]
    for p in polys:
        fill(poly_area(p) % 256, 200, 200, 100)
        beginShape()
        for x, y in p:
            vertex(x, y)
        endShape(CLOSE)
        fill(poly_area(p) % 256, 200, 200)
        for x, y in p:
            circle(x, y, 10)
    
def is_poly_good(poly_points):
    for i, a in enumerate(poly_points):
        b = poly_points[(i + 1) % len(poly_points)]
        c = poly_points[(i + 2) % len(poly_points)]
        if not triangle_area(a, b, c):
            return False
    return True

    
def is_poly_very_good(poly_points):
    combos = combinations(poly_points, 3)
    if any(not triangle_area(a, b, c) for a, b, c in combos):
        return False
    return True
