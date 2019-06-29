# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
# More combinatorics of triangles in grids based on sektch_190602a
# Lerp to make intermediary triangles

from itertools import product, combinations

space, border = 16, 20

def setup():
    global two_triangle_combos, W, H
    size(1240, 648)
    blendMode(MULTIPLY)
    strokeJoin(ROUND)
    # points on a 3x3 grid
    grid = product((-1, 0, 1), repeat=2)
    # all 3-point combinations on the grid
    points = combinations(grid, 3)
    # identify triangles (discard colinear point triples)
    triangles = []
    for p in points:
        area = (p[1][0] * (p[2][1] - p[0][1]) +
                p[2][0] * (p[0][1] - p[1][1]) +
                p[0][0] * (p[1][1] - p[2][1]))
        if area != 0:
            triangles.append(p)
    println("Number of possible triangles: {}"
            .format(len(triangles)))
    # calculate 2-triangle combinations
    two_triangle_combos = list(combinations(triangles, 2))
    println("Number of 2-triangle combinations: {}"
            .format(len(two_triangle_combos)))
    # calculate display grid
    W = (width - border * 2) // space
    H = (height - border * 2) // space
    println("Cols: {} Rows: {}"
            .format(W, H))
    noLoop()


def draw():
    background(240)
    i = 0
    for y in range(H):
        for x in range(W):
            if i < len(two_triangle_combos):
                pushMatrix()
                translate(border + space / 2 + space * x,
                          border + space / 2 + space * y)
                draw_combo(two_triangle_combos[i])
                popMatrix()
                i += 1

def draw_combo(combo):
    noFill()
    siz = space * .5 # .35
    triangles = (combo[0],
           lerp_poly(combo[0], combo[1], 0.33),
           lerp_poly(combo[0], combo[1], 0.66),
           combo[1])
    for i, t in enumerate(triangles):
        # colors for each of the triangles
        colors = (color(200, 100, 0),
                  color(133, 100, 66),
                  color(66, 100, 33),
                  color(0, 100, 200))
        stroke(colors[i])
        draw_poly(scale_poly(t, siz))

def draw_poly(p_list, closed=True):
    beginShape()
    for p in p_list:
        if len(p) == 2 or p[2] == 0:
            vertex(p[0], p[1])
        else:
            vertex(*p)
    if closed:
        endShape(CLOSE)
    else:
        endShape()
        
def lerp_poly(p0, p1, t):
    pt = []
    for sp0, sp1 in zip(p0, p1):
        pt.append((lerp(sp0[0], sp1[0], t),
                   lerp(sp0[1], sp1[1], t)))
    return pt
        
def scale_poly(p_list, s):
    return [(p[0] * s, p[1] * s) for p in p_list]

def keyPressed():
    if key == "s":
        saveFrame(SKETCH_NAME + OUTPUT)
        
        
def settings():
    """ print markdown to add at the sketch-a-day page"""
    from os import path
    global SKETCH_NAME, OUTPUT
    SKETCH_NAME = path.basename(sketchPath())
    OUTPUT = ".png"
    println(
        """
![{0}]({2}/{0}/{0}{1})

[{0}](https://github.com/villares/sketch-a-day/tree/master/{2}/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, OUTPUT, year())
    )
