from itertools import product, combinations, permutations

from villares.line_geometry import edges_as_sets

def setup():
    global grade, quads
    size(500, 500)
    frameRate(10)
    grade = list(product(range(50, 500, 75), repeat=2))    
    polys = list(combinations(grade, 3))
    print(len(polys))

    # tested, polys = set(), []
    # for poly in all_polys:
    #     edges = edges_as_sets(poly)
    #     if edges not in tested and edges:
    #         tested.add(edges)
    #         polys.append(poly)

    quads = [(a, b, (c[0], b[1]), c) for a, b, c in polys if 
           corner_angle(a, b, c) == HALF_PI #and
           # corner_angle(a, b, d) == HALF_PI and
           # corner_angle(d, c, a) == HALF_PI 
           ]
    quads.sort(key=poly_area)
    print(len(quads))
             
def draw():
    colorMode(RGB)
    background(200, 200, 180)
    fill(0)
    for x, y in grade:
        circle(x, y, 5)
    q = quads[frameCount % len(quads)]
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

def corner_angle(c, a, b):
      ac = (c[0] - a[0]) ** 2 + (c[1] - a[1]) ** 2
      bc = (c[0] - b[0]) ** 2 + (c[1] - b[1]) ** 2
      ab = (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2
      return acos((bc + ac - ab) / sqrt(4 * bc * ac))
