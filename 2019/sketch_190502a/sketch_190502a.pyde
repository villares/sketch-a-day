"""
Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day

- Unfolding piramids
"""

# add_library('GifAnimation')
# from gif_exporter import gif_export

CUT_STROKE = color(255, 0, 0)
FOLD_STROKE = color(0, 0, 255)

outer_radius, inner_radius = 100, 50
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
    points = piramid_3D(sides, outer_radius, inner_radius)
    popMatrix()
    # draw unfolded 2D
    translate(width / 2, height *  3 / 4 - 50)
    piramid_2D(points)

def piramid_3D(np, ext_r, base_r):
    # calculando os points
    points = []
    n = np * 2
    for i in range(n):
        ang = radians(i * 360. / n)
        if i % 2 == 0:
            r = base_r
        else:
            r = ext_r
        x = sin(ang) * r
        y = cos(ang) * r
        points.append((x, y))
    # edges da base
    base_points = points[::2]
    o_base_points = base_points[1:] + [base_points[0]]
    base_edges = zip(base_points, o_base_points)
    # calculo da altura
    (p0x, p0y), (p1x, p1y) = points[0], points[1]
    side = dist(p0x, p0y, p1x, p1y)
    h_squared = side * side - base_r * base_r
    if h_squared > 0:  # se a altura viavel
        h = sqrt(h_squared)
        for edge in base_edges:
            p1, p2 = edge
            beginShape()
            vertex(*p1)
            vertex(*p2)
            vertex(0, 0, h)
            endShape(CLOSE)
    # always draws base
    beginShape()
    for pt in base_points:
        vertex(*pt)
    endShape(CLOSE)
    # return points for 2D!
    return points

def piramid_2D(points):
    noFill()
    # base fold lines
    stroke(FOLD_STROKE)
    beginShape()
    for pt in points[::2]:
        vertex(*pt)
    endShape(CLOSE)
    # lateral edges
    o_points = points[1:] + [points[0]]
    edges = zip(points, o_points)
    for i, edge in enumerate(edges):
        p1, p2 = edge
        stroke(CUT_STROKE)
        if i % 2 == 0:
        # abas de cola
            glue_tab(p2, p1, 10, )
            # FOLD_STROKE
            stroke(FOLD_STROKE)
            line(p2[0], p2[1], p1[0], p1[1])
        else:
            # outra edge cortada
            line(p1[0], p1[1], p2[0], p2[1])

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
    global inner_radius, outer_radius, sides
    if keyCode == UP:
        outer_radius += 5
    if keyCode == DOWN:
        outer_radius -= 5
    if keyCode == LEFT:
        inner_radius += 5
    if keyCode == base_rGHT:
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
