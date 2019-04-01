# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
from __future__ import division
from random import choice
from arcs import poly_filleted
add_library('GifAnimation')
from gif_exporter import gif_export

"""
Oh, the difference a grid makes!
"""
SKETCH_NAME, OUTPUT = "sketch_190330a", ".gif"
SPACING, MARGIN = 100, 100
X_LIST, Y_LIST = [], []  # listas de posições para elementos
rad_list = [10, 20, 30, 40]

def setup():
    size(500, 500)
    X_LIST[:] = [x for x in range(MARGIN, 1 + width - MARGIN, SPACING)]
    Y_LIST[:] = [y for y in range(MARGIN, 1 + height - MARGIN, SPACING)]
    create_list()

def create_list():
    global p_list
    p_list = [PVector(choice(X_LIST),choice(Y_LIST)) for r in rad_list]

def draw():
    background(200)
    noFill()
    strokeWeight(2)
    stroke(255) 
    poly_filleted(p_list, rad_list)
    strokeWeight(2)
    stroke(0)
    poly_arc_augmented(p_list, rad_list)

def poly_arc_augmented(p_list, r_list):
    a_list = []
    for i1 in range(len(p_list)):
        i2 = (i1 + 1) % len(p_list)
        p1, p2, r1, r2 = p_list[i1], p_list[i2], r_list[i1], r_list[i2]
        a = circ_circ_tangent(p1, p2, r1, r2)
        a_list.append(a)
        ellipse(p1.x, p1.y, 2, 2)

    for i1 in range(len(a_list)):
        i2 = (i1 + 1) % len(a_list)
        p1, p2, r1, r2 = p_list[i1], p_list[i2], r_list[i1], r_list[i2]
        #ellipse(p1.x, p1.y, r1 * 2, r1 * 2)
        a1 = a_list[i1]
        a2 = a_list[i2]
        if a1 and a2:
            start = a1 if a1 < a2 else a1 - TWO_PI
            arc(p2.x, p2.y, r2 * 2, r2 * 2, start, a2)
        else:
            # println((a1, a2))
            ellipse(p1.x, p1.y, r1 * 2, r1 * 2)
            ellipse(p2.x, p2.y, r2 * 2, r2 * 2)


def circ_circ_tangent(p1, p2, r1, r2):
    d = dist(p1.x, p1.y, p2.x, p2.y)
    ri = r1 - r2
    line_angle = atan2(p1.x - p2.x, p2.y - p1.y)
    if d > abs(ri):
        theta = asin(ri / float(d))

        x1 = cos(line_angle - theta) * r1
        y1 = sin(line_angle - theta) * r1
        x2 = cos(line_angle - theta) * r2
        y2 = sin(line_angle - theta) * r2
        # line(p1.x - x1, p1.y - y1, p2.x - x2, p2.y - y2)

        x1 = -cos(line_angle + theta) * r1
        y1 = -sin(line_angle + theta) * r1
        x2 = -cos(line_angle + theta) * r2
        y2 = -sin(line_angle + theta) * r2
        line(p1.x - x1, p1.y - y1, p2.x - x2, p2.y - y2)
        return (line_angle + theta)
    else:
        line(p1.x, p1.y, p2.x, p2.y)
        return None

def mouseClicked():
    create_list()

def keyPressed():
    gif_export(GifMaker, filename=SKETCH_NAME, delay=1200)

# print text to add to the project's README.md
def settings():
    println(
        """
![{0}](2019/{0}/{0}{1})

[{0}](https://github.com/villares/sketch-a-day/tree/master/2019/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, OUTPUT)
    )
