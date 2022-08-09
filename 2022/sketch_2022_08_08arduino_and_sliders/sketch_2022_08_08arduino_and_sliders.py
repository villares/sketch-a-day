"""
based on sktech "s085" 2018_03_26
"""

import py5
from peasy import PeasyCam
from inputs import InputInterface
from diamond import diamond

MARGIN = 20

COLORS = [
    py5.color(0),
    py5.color(100, 0, 0),
    py5.color(0, 100, 0),
    py5.color(0, 0, 150)
]

SHAPES = [
    py5.ellipse,
    py5.rect,
    diamond,
]

def setup():
    global interface
    py5.size(800, 800, py5.P3D)
    py5.rect_mode(py5.CENTER)
    
    interface = InputInterface()          # Arduino with pots or sliders
    
    this = py5.get_current_sketch()
    cam = PeasyCam(this, 1000)
    cam.setMinimumDistance(1000)          # these two lines will kill the zoom 
    cam.setMaximumDistance(1000)          #    good to liberate the mouse wheel
    panDH = cam.getPanDragHandler();      # get the PanDragHandler
    cam.setCenterDragHandler(panDH);      # set it to the Center/Wheel drag
    orbitDH = cam.getRotateDragHandler(); # get the RotateDragHandler
    cam.setRightDragHandler(orbitDH);                       
    cam.setLeftDragHandler(None);         # sets no left-drag Handler

def draw():
    py5.translate(0, 0, -200)
    py5.background(220)
    py5.no_fill()

    a = int(1 + interface.analog_read(1) / 32)  # number of elements
    b = int(1 + interface.analog_read(2) / 16)  # size of elements
    c = int(1 + interface.analog_read(3) / 32)  # space between elements
    d = int(1 + interface.analog_read(4) / 32)  # number of grids

    py5.random_seed(int(d * 100))  # a different random seed

    for i in range(d):
        hw = a * c / 2
        x = int(1 + py5.random(-a, a)) / 2 * c
        y = int(1 + py5.random(-a, a)) / 2 * c
        z = py5.random_choice((-400, 400)) + d
        sc = py5.random_choice(COLORS)
        py5.stroke(sc)
        sw = int(py5.random(1, 3))
        py5.stroke_weight(sw)
        rx = py5.random_choice((py5.HALF_PI, 0))
        shape_function = py5.random_choice(SHAPES)
        if rx == 0:
            grid(x, y, z, a, b, c, rx, shape_function)
        else:
            grid(x, z, y, a, b, c, rx, shape_function)

    interface.update()


def grid(x, y, z, num, size_, space, rot_x, func):
    with py5.push():
        w = num * space
        py5.translate(x - w / 2, y - w / 2, z)
        py5.rotate_x(rot_x)
        for i in range(0, w, space):
            for j in range(0, w, space):
                func(i, j, size_, size_)


def key_pressed():
    if py5.key == 'p':
        py5.save_frame("grids-s85-####.png")
    if py5.key == 'h':
        interface.help()
    interface.key_pressed()


def key_released():
    interface.key_released()


def mouse_wheel(e):
    interface.mouse_wheel(e)


py5.run_sketch()
