from itertools import product, combinations

def setup():
    global grade, pares, rects
    size(500, 500)
    frame_rate(10)
    grade = list(product(range(50, 500, 75), repeat=2))    
    rects = [pontos_rect(par)
             for par in combinations(grade, 2)
             if boa_diagonal(par)]
    rects.sort(key=poly_area)
    print(len(rects))
               
def draw():
    background(200, 200, 180)
    fill(0)
    for x, y in grade:
        circle(x, y, 5)
    r = rects[frame_count % len(rects)]
    with begin_shape():
        for x, y in r:
            vertex(x, y)

def boa_diagonal(par):
    (x1, y1), (x2, y2) = par
    # if x1 == x2 or y1 == y2:
    #     return False
    # else:
    #     return True
    return not (x1 == x2 or y1 == y2)
            
def pontos_rect(par):
    pa = par[0]
    pb = (par[1][0], par[0][1])
    pc = par[1]
    pd = (par[0][0], par[1][1])
    return (pa, pb, pc, pd)
    
def poly_area(pts):
    vs = list(pts)
    area = 0.0
    for (ax, ay), (bx, by) in zip(vs, vs[1:] + [vs[0]]):
        area += ax * by
        area -= bx * ay
    return abs(area) / 2.0