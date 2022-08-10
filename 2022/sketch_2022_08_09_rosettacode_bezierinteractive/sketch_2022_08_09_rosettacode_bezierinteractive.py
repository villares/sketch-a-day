"""
Bézier Curves Cubic (Interactive)
https://rosettacode.org/wiki/Bitmap/B%C3%A9zier_curves/Cubic#Processing
2020-04 Alexandre Villares

Task:

Using the data storage type for raster images and a draw_line function,
draw a cubic bezier curve.
"""

# A working sketch with movable anchor and control points.
# It can be run online :
# https://www.openprocessing.org/sketch/846556/

x = [0] * 4
y = [0] * 4
dragging = None

def setup():
    size(300, 300)
    smooth()
    # startpoint coordinates
    x[0] = x[1] = 50
    y[0] = 50
    y[1] = y[2] = 150
    x[2] = x[3] = 250
    y[3] = 250

def draw():
    background(255)
    no_fill()
    stroke(0, 0, 255)
    bezier(x[1], y[1], x[0], y[0], x[3], y[3], x[2], y[2])
    # the bezier handles
    stroke_weight(1)
    stroke(100)
    line(x[0], y[0], x[1], y[1])
    line(x[2], y[2], x[3], y[3])
    # the anchor and control points
    stroke(0)
    fill(0)
    for i in range(4):
        if i == 0 or i == 3:
            fill(255, 100, 10)
            rect_mode(CENTER)
            rect(x[i], y[i], 5, 5)
        else:
            fill(0)
            ellipse(x[i], y[i], 5, 5)

def mouse_released():
    global dragging
    dragging = None

def mouse_pressed():
    global dragging
    for i in range(4):
        if (x[i] - 5 <= mouse_x <= x[i] + 10 and
            y[i] - 5 <= mouse_y <= y[i] + 10):
            dragging = i
            break

def mouse_moved():
    # hand cursor when over dragging over points
    for i in range(4):
        if (x[i] - 5 <= mouse_x <= x[i] + 10 and
            y[i] - 5 <= mouse_y <= y[i] + 10):
            cursor(HAND)
            break
    else:
        cursor(ARROW)

def mouse_dragged():
    if dragging is not None:
        x[dragging] = mouse_x
        y[dragging] = mouse_y
        cursor(CROSS)