"""
Based on follow 3 code from Keith Peters in the Processing examples

A segmented line follows the mouse. the relative angle from
each segment to the next is calculated with atan2() and the
position of the next is calculated with sin() and cos().
"""

x = [300.0] * 20
y = [180.0] * 20
joints = [(250, 250)] * 20
seg_length = 20


def setup():
    size(500, 500)
    stroke_weight(9)
    color_mode(HSB)


def draw():
    background(240)
    fill(0, 150)
    drag_segment(0, mouse_x, mouse_y)
    for i in range(len(x) - 1):
        stroke(i * 10, 200, 100, 150)
        drag_segment(i + 1, x[i], y[i])


def drag_segment(i, xin, yin):
    dx = xin - x[i]
    dy = yin - y[i]
    angle = atan2(dy, dx)
    x[i] = xin - cos(angle) * seg_length
    y[i] = yin - sin(angle) * seg_length
    draw_segment(x[i], y[i], angle)


def draw_segment(x, y, a):
    with push_matrix():
        translate(x, y)
        rotate(a)
        line(0, 0, seg_length, 0)
        
def mouse_wheel(e):
    global seg_length
    seg_length += e.getCount()
