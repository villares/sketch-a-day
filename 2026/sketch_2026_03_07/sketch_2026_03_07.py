from itertools import product, combinations, permutations
from villares.geometry_helpers import (is_poly_self_intersecting,
                                    poly_area,
                                    triangle_area,
                                    is_poly_convex,
                                    edges_as_sets,
                                    )
#from random import choice, sample, shuffle
from py5_tools import animated_gif

def setup():
    global grade, combos
    size(500, 500)
    grade = list(product(range(100, 500, 100), repeat=2))    
    frame_rate(2)
    all_polys = permutations(grade, 4)
    tested, polys = set(), []
    for poly in all_polys:
        edges = edges_as_sets(poly)
        if edges not in tested and edges:
            tested.add(edges)
            polys.append(poly)
    combos = [p for p in polys
              if not is_poly_self_intersecting(p)
              and is_poly_good(p)
              ]
    #shuffle(combos)
    print(len(combos))
    animated_gif('out.gif', frame_numbers=range(1, 101), duration=0.5)
        
def draw():
    color_mode(RGB)
    background(200, 200, 180)
    color_mode(HSB)
    fill(0)
    for x, y in grade:
        circle(x, y, 5)
    fill(255, 100)
    f = frame_count % len(combos)
    polys = combos[f:f+5]
    for p in polys:
        fill(poly_area(p) % 256, 200, 200, 100)
        with begin_closed_shape():
            vertices(p)
#         fill(0)
#         for x, y in p:
#             circle(x, y, 10)
    
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

