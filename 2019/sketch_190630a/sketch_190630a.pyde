# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
# More combinatorics of triangles based on sketch_190629a
# Now some 3D

from itertools import product, combinations

def setup():
    global two_triangle_combos, triangles, space, border
    size(200, 200, P3D)
    border = 50
    space = width - 2 * border
    smooth(8)
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

def draw():
    background(240)
    ortho()
    translate(width / 2, height / 2)
    rotateY(radians(frameCount))
    noFill()
    i = (frameCount % len(two_triangle_combos)) // 90
    draw_combo(two_triangle_combos[i])

def draw_combo(combo):
    strokeWeight(border / 10)
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
                  color(66, 100, 133),
                  color(0, 100, 200))
        stroke(colors[i])
        draw_poly(scale_poly(t, siz))
    
def draw_poly(p_list):
    beginShape()
    for p in p_list:
       vertex(p[0], p[1], p[0] * p[1] / space)
    endShape(CLOSE)
        
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
