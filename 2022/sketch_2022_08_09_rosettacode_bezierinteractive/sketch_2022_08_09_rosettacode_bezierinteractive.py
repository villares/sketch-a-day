"""
Bézier Curves Cubic (Interactive)
https://rosettacode.org/wiki/Bitmap/B%C3%A9zier_curves/Cubic#Processing
2020-04 Alexandre Villares (Python mode version)
2022-08 Alexandre Villares (py5 version) 

Task:

Using the data storage type for raster images and a draw_line function,
draw a cubic bezier curve.
"""

# A working sketch with movable anchor and control points.
# It can be run online :
# https://www.openprocessing.org/sketch/846556/

pts = []
dragging = None

def setup():
    size(300, 300)
    smooth()
    # startpoint coordinates
    pts.append(Py5Vector(50, 50))
    pts.append(Py5Vector(50, 150))
    pts.append(Py5Vector(250, 150))
    pts.append(Py5Vector(250, 250))

def draw():
    background(255)
    no_fill()
    stroke(0, 0, 255)
    bezier(*pts[1], *pts[0], *pts[3], *pts[2])
    # the bezier handles
    stroke_weight(1)
    stroke(100)
    line(*pts[0], *pts[1])
    line(*pts[2], *pts[3])
    # the anchor and control points
    stroke(0)
    fill(0)
    for i in range(4):
        if i == 0 or i == 3:
            fill(255, 100, 10)
            rect_mode(CENTER)
            rect(*pts[i], 5, 5)
        else:
            fill(0)
            ellipse(*pts[i], 5, 5)

def mouse_released():
    global dragging
    dragging = None

def mouse_pressed():
    global dragging
    for i, p in enumerate(pts):
        if (p.x - 5 <= mouse_x <= p.x + 10 and
            p.y - 5 <= mouse_y <= p.y + 10):
            dragging = i
            break

def mouse_moved():
    # hand cursor when over dragging over points
    for x, y in pts:
        if (x - 5 <= mouse_x <= x + 10 and
            y - 5 <= mouse_y <= y + 10):
            cursor(HAND)
            break
    else:
        cursor(ARROW)

def mouse_dragged():
    if dragging is not None:
        pts[dragging].xy = mouse_x, mouse_y
        cursor(CROSS)