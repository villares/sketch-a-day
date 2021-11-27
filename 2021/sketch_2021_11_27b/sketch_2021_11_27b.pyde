# Alexandre B A Villares - https://abav.lugaralgum.com/
# To run this you will need Processing 3.5.4 + Python mode, instructions at: 
# https://abav.lugaralgum.com/como-instalar-o-processing-modo-python/index-EN.html

"""
3-segment combinations on a 3 x 2 grid: 381 + 74
Cols: 13 Rows: 13 (169)
"""

add_library('pdf')
from itertools import product, combinations, permutations

space, border = 40, 50
name = "segs"

def setup():
    size(980, 940)
    grid = product((-1, 0, 1), (-1,  1))  
    points = list(grid)
    segs = create_lines(points)
    print(len(segs))
    W = (width - border * 2) // space
    H = (height - border * 2) // space
    println("Cols: {} Rows: {} Visible grid: {}".format(W, H, W * H))
    
    strokeJoin(ROUND)
    strokeWeight(2)
    # start drawing
    background(240)
    i = 0
    for y in range(H):
        for x in range(W):
            if i < len(segs):
                pushMatrix()
                translate(border / 2 + space + space * x,
                          border / 2 + space + space * y)
                seg, collapsed = segs[i]
                if collapsed:
                    stroke(255, 0, 0)
                else:
                    stroke(0)
                draw_segs(scale_segs(seg, space * 0.30))
                popMatrix()
                i += 1

    saveFrame(name + '.png')

def draw_segs(seg_list):
    for seg in seg_list:
        beginShape()
        for p in seg:
                vertex(p[0], p[1])
        endShape()
    

def scale_segs(p_list, s):
    return [[(p[0] * s, p[1] * s) for p in l_list] for l_list in p_list]

def create_lines(points):
    all_lines = sorted(combinations(points, 2))
    return [
        (combo, collapsed(combo)) for combo in combinations(all_lines, 3)
        # if collapsed(combo)
        # if not collapsed(combo)
        ]
    
def collapsed(segs):
    for i, seg_b in enumerate(segs):
        seg_a = segs[i - 1]
        pts = set(seg_a) | set(seg_b)
        if len(pts) == 3:
            a, b, c = pts
        else:
            continue 
        if triangle_area(a, b, c) == 0:
            return (a, b, c)
        else:
            continue
    
def triangle_area(a, b, c):
    return (a[0] * (b[1] - c[1]) +
            b[0] * (c[1] - a[1]) +
            c[0] * (a[1] - b[1]))
    

    
