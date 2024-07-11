from itertools import product, combinations

import py5_tools

def setup():
    global grid, pairs, rects
    size(500, 500, P2D)
    frame_rate(10)
    grid = list(product(range(50, 500, 100), repeat=2))    
    rects_as_sets = set()
    rects = []
    for pair in combinations(grid, 2):
        pts = pontos_rect(pair)
        frozen_pts = frozenset(pts)        
        if boa_diagonal(pair) and frozen_pts not in rects_as_sets:
             rects.append(pts)
             rects_as_sets.add(frozen_pts)
    rects.sort(key=poly_area)
    print(len(rects))
    # Note frame 0 is just after setup() and frame 1 is after the first run of draw()
    py5_tools.animated_gif('out.gif', duration=0.3, frame_numbers=range(1, len(rects)+1))
    no_stroke()
               
def draw():
    background(200, 200, 180)
    fill(0)
    for x, y in grid:
        circle(x, y, 10)
    # shows the first rect (index 0) on the first draw() frame (frame_count 1)
    r = rects[(frame_count - 1) % len(rects)]
    with begin_shape():
        for x, y in r:
            fill(x % 255, y % 255, (x * y) % 255)
            vertex(x, y)
    apply_filter(POSTERIZE, 16)

def boa_diagonal(pair):
    (x1, y1), (x2, y2) = pair
    return not (x1 == x2 or y1 == y2)
            
def pontos_rect(pair):
    pa = pair[0]
    pb = (pair[1][0], pair[0][1])
    pc = pair[1]
    pd = (pair[0][0], pair[1][1])
    return (pa, pb, pc, pd)
    
def poly_area(pts):
    vs = list(pts)
    area = 0.0
    for (ax, ay), (bx, by) in zip(vs, vs[1:] + [vs[0]]):
        area += ax * by
        area -= bx * ay
    return abs(area) / 2.0