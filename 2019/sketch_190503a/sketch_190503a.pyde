"""
Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day

- Unfolding prism
"""

# add_library('GifAnimation')
# from gif_exporter import gif_export

CUT_STROKE = color(255, 0, 0)
FOLD_STROKE = color(0, 0, 255)

p_height, inner_radius = 100, 50
sides = 5

def setup():
    size(400, 600, P3D)
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
    points = prism_3D(sides, p_height, inner_radius)
    popMatrix()
    # draw unfolded 2D
    translate(width / 2, height *  3 / 4 - 50)
    prism_2D(points)

def prism_3D(np, h, base_r):
    # calculando os points
    points = []
    for i in range(np):
        ang = radians(i * 360. / np)
        x = sin(ang) * base_r
        y = cos(ang) * base_r
        points.append((x, y))
    # edges da base
    base_points = points[::]
    o_base_points = base_points[1:] + [base_points[0]]
    base_edges = zip(base_points, o_base_points)
    for edge in base_edges:
            (p1x, p1y), (p2x, p2y) = edge
            beginShape()
            vertex(p1x, p1y, 0)
            vertex(p1x, p1y, h)
            vertex(p2x, p2y, h)
            vertex(p2x, p2y, 0)
            endShape(CLOSE)
    # always draws base
    beginShape()
    for pt in base_points:
        vertex(pt[0], pt[1], h)
    endShape(CLOSE)
    beginShape()
    for pt in base_points:
        vertex(pt[0], pt[1], 0)
    endShape(CLOSE)
    # return points for 2D!
    return points

def prism_2D(points):
    ang = radians(360. / len(points))
    rotate(ang/2)
    noFill()
    # base fold lines
    stroke(FOLD_STROKE)
    beginShape()
    for pt in points:
        vertex(*pt)
    endShape(CLOSE)
    # lateral edges
    o_points = points[1:] + [points[0]]
    edges = zip(points, o_points)
    for i, edge in enumerate(edges[1:]):
        p1, p2 = edge
        stroke(CUT_STROKE)
        # abas de cola
        glue_tab(p2, p1, 10, )
        # FOLD_STROKE
        stroke(FOLD_STROKE)
        line(p2[0], p2[1], p1[0], p1[1])
        
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
    global inner_radius, p_height, sides
    if keyCode == UP:
        p_height += 5
    if keyCode == DOWN:
        p_height -= 5
    if keyCode == LEFT:
        inner_radius += 5
    if keyCode == RIGHT:
        inner_radius -= 5
    if key == "+":
        sides += 1
    if key == "-" and sides > 3:
        sides -= 1

    # if key == "g":
    #     gif_export(GifMaker, filename=SKETCH_NAME)

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
