from itertools import product, combinations, permutations
from random import choice, sample, shuffle
from villares.line_geometry import edges_as_sets, poly_area
from villares.gif_export import gif_export
add_library('gifAnimation')

def setup():
    global grade, rects
    size(500, 500)
    grade = list(product(range(50, 500, 100), repeat=2))    
    frameRate(2)
    all_polys = permutations(grade, 4)
    
    t = millis()
    # tested, polys = set(), []
    # for poly in all_polys:
    #     edges = edges_as_sets(poly)
    #     if edges not in tested and edges:
    #         tested.add(edges)
    #         polys.append(poly)
            
    # rects = [p for p in polys if
    #            digonals_equal(p)
    #           ]
    
    print(millis() - t)
    # shuffle(rects)
    # print(len(rects))  # 50 rects
    
        
def draw():
    colorMode(RGB)
    background(200, 200, 180)
    fill(0)
    for x, y in grade:
        circle(x, y, 5)
    fill(255, 100)
    
    a, b, c, d = sample(grade, 4)
    line(a[0], a[1], b[0], b[1])          
    line(c[0], c[1], d[0], d[1])          
    
    ab = degrees(atan2(a[1] - b[1], a[0] - b[0]))
    cd = degrees(atan2(c[1] - d[1], c[0] - d[0]))
    p = abs(ab - cd)
    textAlign(CENTER, CENTER)
    if p == 0 or p == 90 or p == 180:
        fill(255, 0, 0)
    else:
        fill(0)
    textSize(40)
    text(format(p, ".0f"), 250, 200)
    # text(cd, 250, 290)
              
    # if frameCount % len(rects) == 0:
    #     gif_export(GifMaker, finish='True')
    #     exit()
    # else:
    #     gif_export(GifMaker, 'output', delay=400, quality=0)

def poly_color(p):
    return color(poly_area(p) % 256, 200, 200)
                
def sq_dist(a, b):
    xa, ya = a
    xb, yb = b
    return (xa - xb) ** 2 + (ya - yb) ** 2

def digonals_equal(poly_points):
    a, b, c, d = poly_points
    ab = sq_dist(a, b)
    bc = sq_dist(b, c)
    return ab == bc and bc == sq_dist(c, d)

def propor(pp):
    a, b, c, d = poly_points
    # abx = a[0] - b[0]
    # dcx = d[0] - c[0]
    # aby = a[1] - b[1]
    # dcy = d[1] - c[1]
    # bcx = b[0] - c[0]
    # adx = a[0] - d[0]
    # bcy = b[1] - c[1]
    # ady = a[1] - d[1]
        
    # # return abx == dcx and aby == dcy
    # return (pp[0][0] - pp[1][0] == pp[3][0] - pp[2][0] 
    #     and pp[1][1] - pp[2][1] == pp[0][1] - pp[3][1]
    #        and pp[0][1] - pp[1][1] == pp[3][1] - pp[2][1]
    #         )
