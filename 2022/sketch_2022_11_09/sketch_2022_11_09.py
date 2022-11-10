"""
Combinations of triangles on octagon, so that the line_segs don't share
starting or ending points: 378

"""
from itertools import combinations

W = 70 # Width base-value for configs
GRID_COLOR = 0
SCALE = 1

def setup():
    size(1040 * SCALE, 900 * SCALE, P2D)
    scale(SCALE)
    stroke_cap(ROUND)
    color_mode(HSB)
    no_fill()
    d45, r = radians(45), 1.5
    positions = [(r * cos(i * d45), r * sin(i * d45)) for i in range(8)]
    colors = {p: color(i * 24, 200, 200) for i, p in enumerate(positions)}
    tri_points = list(combinations(positions, 3))       
    
    print(f'Configurations: {len(tri_points)}')
    i = 1
    x = y = W * 2
    w = W / 3
    for tri in tri_points:
        stroke(GRID_COLOR)
        stroke_weight(w / 5)
        push_matrix()
        translate(x, y)
        points([(xo * w, yo * w) for xo, yo in positions])
        no_stroke()
        (xa, ya), (xb, yb), (xc, yc) = tri
        begin_shape(TRIANGLE)
        fill(colors[(xa, ya)])
        vertex(xa * w, ya * w)
        fill(colors[(xb, yb)])
        vertex(xb * w, yb * w)
        fill(colors[(xc, yc)])
        vertex(xc * w, yc * w)
        end_shape()
        pop_matrix()
        x += W * 1.5
        if x > width / SCALE - W * 1.5:
            #print(i)  # debug
            x = W * 2
            y +=  W * 1.5
        i += 1
    save_frame('sketch_2022_11_09.png')
