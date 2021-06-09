from itertools import product, combinations, permutations
import pickle
from villares.line_geometry import edges_as_sets, is_poly_convex

def setup():
    global grade, quads
    size(475, 475)
    frameRate(10)
    grade = list(product(range(50, 500, 75), repeat=2))    
    # all_polys = list(permutations(grade, 4))
    # tested, polys = set(), []
    # for poly in all_polys:
    #     if is_poly_convex(poly):
    #         edges = edges_as_sets(poly)
    #         if edges not in tested and edges:
    #             tested.add(edges)
    #             polys.append(poly)
                
    # print(len(polys))
    # with open("poly.data", "w") as f:
    #         pickle.dump(polys, f)
    # print("done!")
    with open("poly.data") as f:
            polys = pickle.load(f)
    t = millis()
    quads = [(a, b, c, d) for a, b, c, d in polys if 
           corner_angle(a, b, d) == HALF_PI or
           corner_angle(b, c, a) == HALF_PI or
           corner_angle(c, b, d) == HALF_PI 
           ]
    
    print(millis() - t)
    quads.sort(key=poly_area)
    print(len(quads))
             
def draw():
    colorMode(RGB)
    fill(200, 32)
    rect(0, 0, width, height)
    # background(200, 200, 180)
    fill(0)
    for x, y in grade:
        circle(x, y, 5)
    q = quads[(frameCount - 1) % len(quads)]
    colorMode(HSB)
    fill(8 * poly_area(q) % 256, 255, 255)
    beginShape()
    for x, y in q:
        vertex(x, y)
    endShape(CLOSE)

def poly_area(points):
    points = list(points)
    area = 0.0
    for (ax, ay), (bx, by) in zip(points, points[1:] + [points[0]]):
        area += ax * by
        area -= bx * ay
    return abs(area) / 2.0

def corner_angle(corner, a, b):
    ac = atan2(a[1] - corner[1], a[0] - corner[0])
    bc = atan2(b[1] - corner[1], b[0] - corner[0])
    return abs(ac - bc)           
  
  
