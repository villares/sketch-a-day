"""
based on sktech "s085" 2018_03_26
"""

from inputs import InputInterface

COLORS = [
    color(0),
    color(255),
    color(200, 0, 0),
    color(0, 0, 200)
    ]

B_MARGIN = 100
MARGIN = 20

def setup():
    global interface
    size(800, 800 + B_MARGIN)
    color_mode(HSB)
    rect_mode(CENTER)
    #stroke_weight(1.5)
    interface = InputInterface()
    

def draw():
    background(220)
    no_fill()

    a = int(1 + interface.analog_read(1) / 32) # number of elements
    b = int(1 + interface.analog_read(2) / 16) # size of elements
    c = int(1 + interface.analog_read(3) / 32) # space between elements
    d = int(1 + interface.analog_read(4) / 32) # number of grids

    random_seed(int(d * 100))  # a different random seed

    for i in range(d):
        tam = a * c
        x = int(1 + random(MARGIN, width - tam - MARGIN) / (c / 2)) * c // 2
        y = int(1 + random(MARGIN, height - tam - MARGIN - B_MARGIN) / (c / 2)) * c // 2
        stroke(random_choice(COLORS))
        #troke_weight(int(random(1, 3)))
        grid(x, y, a, b, c, random_choice(SHAPES))

    interface.update()

def exes(x, y, c, _):
    with push_matrix():
        translate(x, y)
        line(-c / 2, -c / 2, c / 2, c / 2)
        line(c / 2, -c / 2, -c / 2, c / 2)

def losang(x, y, c, _):
    with push_matrix():
        translate(x, y)
        rotate(radians(45))
        rect(0, 0, c, c)

SHAPES = [
        ellipse,
        rect,
        exes,
        losang,
        ]

def grid(x, y, num, size_, space, func):
    for i in range(x, x + num * space, space):
        for j in range(y, y + num * space, space):
            func(i, j, size_, size_)

def key_pressed():
    if key == 'p':
        save_frame("grids-s85-####.png")
    if key == 'h':
        interface.help()
    interface.key_pressed()

def key_released():
    interface.key_released()

def mouse_wheel(e):
    interface.mouse_wheel(e)


