# Alexandre B A Villares - https://abav.lugaralgum.com/
# To run this you will need Processing 3.5.4 + Python mode, instructions at: 
# https://abav.lugaralgum.com/como-instalar-o-processing-modo-python/index-EN.html

"""
segs on a 3 x 3, grid
"""

add_library('pdf')
from itertools import product, combinations, permutations

space, border = 20, 20
name = "segs"

def setup():
    size(1830, 930)
    grid = product((-1, 0, 1), (-1, 0, 1))  # 3X3
    points = list(grid)
    segs = create_lines(points)
    print(len(segs))
    W = (width - border * 2) // space
    H = (height - border * 2) // space
    println("Cols: {} Rows: {} Visible grid: {}".format(W, H, W * H))
    # High res PDF export
    f = createGraphics(width * 10, height * 10,
                       PDF, name + '.pdf')
    beginRecord(f) # begin PDF export
    f.scale(10)
    strokeJoin(ROUND)
    strokeWeight(1.5)
    # start drawing
    background(240)
    i = 0
    for y in range(H):
        for x in range(W):
            if i < len(segs):
                pushMatrix()
                translate(border / 2 + space + space * x,
                          border / 2 + space + space * y)
                fill(0)
                draw_segs(scale_segs(segs[i], space * 0.38))
                popMatrix()
                i += 1
    # end PDF export
    endRecord()
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
    all_lines = list(combinations(points, 2))
    return [
        combo for combo in combinations(all_lines, 3)
        if not collapsed(combo)
        ]
    
def collapsed(segs):
    s0, s1, s2 = segs
    for seg_a, seg_b in [(s0, s1), (s0, s2), (s1, s2)]:
        pts = set(seg_a) | set(seg_b)
        if len(pts) == 3:
            a, b, c = pts
        else:
            continue 
        if triangle_area(a, b, c) > 0:
            continue
        else:
            return True
    
def triangle_area(a, b, c):
    return (a[0] * (b[1] - c[1]) +
            b[0] * (c[1] - a[1]) +
            c[0] * (a[1] - b[1]))
    

    
