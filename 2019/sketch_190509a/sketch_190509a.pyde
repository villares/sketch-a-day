"""
Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day

- Unfolding solid....
"""

add_library('GifAnimation')
from gif_exporter import gif_export
from unfold_face import *

CUT_STROKE = color(255, 0, 0)
FOLD_STROKE = color(0, 0, 255)

p_height, base_radius, top_radius = 100, 50, 50
sides = 5

def setup():
    size(600, 600, P3D)
    hint(ENABLE_DEPTH_TEST)
    hint(ENABLE_DEPTH_SORT)

def draw():
    background(240)
    pushMatrix()
    translate(width / 2, height / 4 + 50)
    rotateX(radians(45))
    rotateZ(radians(frameCount / 3.))
    fill(255, 200)
    stroke(0)
    strokeWeight(2)
    # draw 3D piramid and get points
    points, face = prism_3D(sides, p_height, base_radius, top_radius)
    popMatrix()
    # draw unfolded 2D
    translate(width / 2, height * 3 / 4 - 50)
    prism_2D(points, face)
    # triangulated_face(*face)

def prism_3D(np, h, base_r, top_r):
    # calculando os points
    base_points = []
    for i in range(np):
        ang = radians(i * 360. / np)
        x = sin(ang) * base_r
        y = cos(ang) * base_r
        base_points.append((x, y))
    # edges da base
    o_base_points = base_points[1:] + [base_points[0]]
    base_edges = zip(base_points, o_base_points)
    top_points = []
    for i in range(np):
        ang = radians(i * 360. / np)
        x = sin(ang) * top_r
        y = cos(ang) * top_r
        top_points.append((x, y))
    # edges da base
    o_top_points = top_points[1:] + [top_points[0]]
    top_edges = zip(top_points, o_top_points)
    # edges
    for base_edge, top_edge in zip(base_edges, top_edges):
        (p1x, p1y), (p2x, p2y) = base_edge
        (p1tx, p1ty), (p2tx, p2ty) = top_edge
        beginShape()
        vertex(p1x, p1y, 0)
        vertex(p1tx, p1ty, h)
        vertex(p2tx, p2ty, h)
        vertex(p2x, p2y, 0)
        endShape(CLOSE)
        #line(p1x, p1y, 0, p2tx, p2ty, h)
    # one face
    (p1x, p1y), (p2x, p2y) = base_edges[0]
    (p1tx, p1ty), (p2tx, p2ty) = top_edges[0]
    face = [(p2x, p2y, 0),
            (p1x, p1y, 0),
            (p1tx, p1ty, h),
            (p2tx, p2ty, h),
            ]
    # always draws base
    beginShape()
    for bpt in base_points:
        vertex(bpt[0], bpt[1], 0)
    endShape(CLOSE)
    beginShape()
    for tpt in top_points:
        vertex(tpt[0], tpt[1], h)
    endShape(CLOSE)
    # return points for 2D!
    return (base_points, top_points), face

def prism_2D(top_bot, face):
    with pushMatrix():
        translate(150, -300)
        poly_draw(top_bot[1])
    with pushMatrix():
        translate(-150, -300)
        poly_draw(top_bot[0])
    x0, y0, z0 = face[1]
    x2, y2, z2 = face[2]
    d = dist(x0, y0, z0, x2, y2, z2)
    side = ((150, d - 150), (150, -150))
    for i in range(sides):
        side = unfold_tri_face(side, face[::-1])
    stroke(CUT_STROKE)
    glue_tab((150, -150), (150, d - 150), 10)

    # for points in all_points:
    #     ang = radians(360. / len(points))
    #     with pushMatrix():
    #         translate(-width / 4, 0)
    #         rotate(ang / 2)
    #         noFill()
    # base fold lines
    #         stroke(FOLD_STROKE)
    #         beginShape()
    #         for pt in points:
    #             vertex(*pt)
    #         endShape(CLOSE)
    # lateral edges
    #         o_points = points[1:] + [points[0]]
    #         edges = zip(points, o_points)
    # for i, edge in enumerate(edges):  # edges[1:] to skip one
    #             p1, p2 = edge
    #             stroke(CUT_STROKE)
    # abas de cola
    # glue_tab(p2, p1, 10, )
    # FOLD_STROKE
    # stroke(FOLD_STROKE)
    #             line(p2[0], p2[1], p1[0], p1[1])
    #     translate(width / 2, 0)

def glue_tab(p1, p2, tab_w, cut_ang=QUARTER_PI / 3):
    """
    draws a trapezoidal or triangular glue tab along edge defined by p1 and p2,
    with width tab_w and cut angle a
    """
    al = atan2(p1[0] - p2[0], p1[1] - p2[1])
    a1 = al + cut_ang + PI
    a2 = al - cut_ang
    # calculate cut_len to get the base_rght tab width
    cut_len = tab_w / sin(cut_ang)
    f1 = (p1[0] + cut_len * sin(a1),
          p1[1] + cut_len * cos(a1))
    f2 = (p2[0] + cut_len * sin(a2),
          p2[1] + cut_len * cos(a2))
    edge_len = dist(p1[0], p1[1], p2[0], p2[1])

    if edge_len > 2 * cut_len * cos(cut_ang):    # 'normal' trapezoidal tab
        beginShape()
        vertex(*p1)    # vertex(p1[0], p1[1])
        vertex(*f1)
        vertex(*f2)
        vertex(*p2)
        endShape()
    else:    # short triangular tab
        fm = ((f1[0] + f2[0]) / 2, (f1[1] + f2[1]) / 2)
        beginShape()
        vertex(*p1)
        vertex(*fm)    # middle way of f1 and f2
        vertex(*p2)
        endShape()

def keyPressed():
    global base_radius, top_radius, p_height, sides
    if keyCode == UP:
        p_height += 5
    if keyCode == DOWN:
        p_height -= 5
    if keyCode == LEFT:
        base_radius += 5
    if keyCode == RIGHT:
        base_radius -= 5
    if key == "w":
        sides += 1
    if key == "s" and sides > 3:
        sides -= 1
    if key == "a" and top_radius > 0:
        top_radius -= 5
    if key == "d":
        top_radius += 5
    if key == "g":
    #    saveFrame(SKETCH_NAME + ".gif")
        gif_export(GifMaker, filename=SKETCH_NAME)

def settings():
    from os import path
    global SKETCH_NAME
    SKETCH_NAME = path.basename(sketchPath())
    OUTPUT = ".gif"
    println(
        """
![{0}]({2}/{0}/{0}{1})

[{0}](https://github.com/villares/sketch-a-day/tree/master/{2}/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, OUTPUT, year())
    )
