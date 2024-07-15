from itertools import product, combinations, permutations

import py5_tools

def setup():
    global grid, pairs, rects
    size(800, 800, P3D)
    frame_rate(10)
    grid = list(product((200, 300, 400, 500, 600), repeat=2))    
    rects_as_sets = set()
    rects = []
    for pts in permutations(grid, 4):
        frozen_pts = frozenset(pts)        
        if check_rect(pts) and frozen_pts not in rects_as_sets:
             rects.append(pts)
             rects_as_sets.add(frozen_pts)
    rects.sort(key=poly_area)
    print(len(rects))
    # Note frame 0 is just after setup() and frame 1 is after the first run of draw()
    #py5_tools.animated_gif('out.gif', duration=0.3, frame_numbers=range(1, len(rects)+1))
    
               
def draw():
    translate(width / 2, height / 2, -height / 2)
    rotate_x(radians(mouse_y))
    translate(-width / 2, -height / 2)
    background(0)
#    stroke(0)
#     for x, y in grid:
#         point(x, y)
    no_stroke()
    for i, r in enumerate(rects):
        fill(r[0][0] % 255, r[0][1] % 255, r[2][0] % 255, 150)
        with begin_shape():
            for x, y in r:
                vertex(x, y, i * 5 - 75 * 5)

def check_rect(pts):
    a, b, c, d = pts
    return (
        is_ortho((a,b), (b,c)) and
        is_ortho((b,c), (c,d)) and
        is_ortho((c,d), (d,a))
        )

def is_ortho(ab, cd):
    ((ax, ay), (bx, by)) = ab
    ((cx, cy), (dx, dy)) = cd
    if bx - ax == 0 and dx - cx == 0:
        return False
    elif bx - ax == 0:
        m2 = (dy - cy) / (dx - cx)
        return m2 == 0 
    elif dx - cx == 0:
        m1 = (by - ay) / (bx - ax);
        return m1 == 0 
    else:
        m1 = (by - ay) / (bx - ax)
        m2 = (dy - cy) / (dx - cx)
        return m1 * m2 == -1
    
def poly_area(pts):
    vs = list(pts)
    area = 0.0
    for (ax, ay), (bx, by) in zip(vs, vs[1:] + [vs[0]]):
        area += ax * by
        area -= bx * ay
    return abs(area) / 2.0