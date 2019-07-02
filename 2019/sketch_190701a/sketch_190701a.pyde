# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
# More combinatorics of polys in grids based on sektch_190630a
# Now quads in 3D

from itertools import product, combinations

def setup():
    global two_poly_combos, polys, space, border
    size(500, 500, P3D)
    border = 100
    space = width - 2 * border
    smooth(8)
    blendMode(MULTIPLY)    
    strokeJoin(ROUND)
    # points on a 3x3 grid
    grid = product((-1, 0, 1), repeat=2)
    # all 3-point combinations on the grid
    points = combinations(grid, 4)
    # identify polys (discard colinear point triples)
    polys = []
    for p in points:
        if area(p) != 0:
            polys.append(p)
    println("Number of possible quads: {}"
            .format(len(polys)))
    # calculate 2-poly combinations
    two_poly_combos = list(combinations(polys, 2))
    println("Number of 2-poly combinations: {}"
            .format(len(two_poly_combos)))

def draw():
    background(240)
    ortho()
    translate(width / 2, height / 2)
    rotateY(radians(frameCount))
    noFill()
    i = (frameCount // 90) % len(two_poly_combos) 
    draw_combo(two_poly_combos[i])

def draw_combo(combo):
    strokeWeight(border / 10)
    noFill()
    siz = space * .5 # .35
    polys = (combo[0],
           lerp_poly(combo[0], combo[1], 0.33),
           lerp_poly(combo[0], combo[1], 0.66),
           combo[1])
    for i, t in enumerate(polys):
        # colors for each of the polys
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


def area(points):
    n = len(points) # of points
    a = 0.0
    for i in range(n):
        j = (i + 1) % n
        a += points[i][0] * points[j][1]
        a -= points[j][0] * points[i][1]
    a /= 2.0
    return a


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
