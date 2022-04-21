"""
Based on 'follow 3' code from Keith Peters in the Processing examples

A segmented line follows the mouse. the relative angle from
each segment to the next is calculated with atan2() and the
position of the next is calculated with sin() and cos().
"""

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
    #for i, (x, y) in enumerate(joints[:-1]): # doesn't work
    # because I'm mutating joints as I go, and enumerate will
    # not see the changes!
    for i in range(len(joints) - 1):
        stroke(i * 10, 200, 100, 150)
        x, y = joints[i]
        drag_segment(i + 1, x, y)

def drag_segment(i, xin, yin):
    dx = xin - joints[i][0]
    dy = yin - joints[i][1]
    angle = atan2(dy, dx)
    x, y = joints[i] = xin - cos(angle) * seg_length, yin - sin(angle) * seg_length
    line(x, y, xin, yin)
    
def mouse_wheel(e):
    global seg_length
    seg_length += e.getCount()
