# inspired by https://twitter.com/beesandbombs/status/1247567578802855938?s=20
add_library('GifAnimation')
from gif_animation_helper import gif_export

s_size = 60
sketch_name = 'sketch_2020_04_13b'

def setup():
    size(400, 400)
    colorMode(HSB)
    blendMode(ADD)  # DIFFERENCE
    rectMode(CENTER)
    textSize(120)
    textAlign(CENTER, CENTER)
    init()

def init():
    from itertools import product
    from random import shuffle
    global origin, target, current
    origin = []
    target = []
    # grid = ((-1, -1), (-1, 0), (0, 0), (0, -1))
    grid = list(product(range(-3, 3), repeat=2))
    # shuffle(grid)

    for i, p in enumerate(grid):
        h_size = s_size / 2
        off_x, off_y = h_size + p[0] * s_size, h_size + p[1] * s_size
        side = i % 2
        origin.append((width / 2. - 30 + side * 60,
                       height / 2.,
                       0,
                       s_size * 2))
        target.append((width / 2. + off_x,
                       height / 2. + off_y,
                       random(-HALF_PI, HALF_PI),
                       random(s_size / 2, s_size * 2)))
    current = origin[:]

def draw():
    background(0)
    noFill()
    strokeWeight(5)
    t = .5 - cos(radians(frameCount % 360)) / 2.  # map(mouseX, 0, width, 0, 1)
    for i, origin_i in enumerate(origin):
        fill((i * 16) % 256, 255, 255)
        x, y, r, s = lerp_sequence(origin_i, target[i], t)
        pushMatrix()
        translate(x, y)
        rotate(r)
        textSize(s)
        text('4', 0, 0)
        popMatrix()

    if frameCount < 360:
        if frameCount % 2:
           gif_export(GifMaker, sketch_name)
    else:
        gif_export(GifMaker, sketch_name, finish=True)

    if frameCount % 360 == 0:
        init()

def lerp_sequence(a, b, t):
    c = []
    for c_a, c_b in zip(a, b):
        c.append(lerp(c_a, c_b, t))
    return c

def keyPressed():
    init()
