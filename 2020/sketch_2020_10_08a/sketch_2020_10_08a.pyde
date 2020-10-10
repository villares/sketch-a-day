# import villares.ubuntu_jogl_fix  # intel video linux bug
# from villares.gif_export import gif_export
# add_library('gifAnimation')
# add_library('peasycam')

import random 

NAME = "sketch_2020_10_08a"
random.seed(10080)
choice = random.choice

elements = []

def setup():
    size(500, 500, P3D)
    frameRate(24)
    # cam = PeasyCam(this, 500)
    generate()

def generate(n=500):
    pegs = (-20, -10, 0, 0, 10, 20)
    elements[:] = [(choice('LCCRMY'),
                    (choice(pegs), choice(pegs)),
                    choice((1, 3)),)
                   for _ in range(n)]

def draw():
    background(240, 240, 220)
    translate(width / 2, height / 2, -100)

    r = frameCount / 100.
    rotateY(r)
    draw_e(elements)

    # if r < TWO_PI:
    #     if frameCount % 2:
    #         gif_export(GifMaker,
    #                    NAME,
    #                    delay=100,
    #                    quality=0)
    # else:
    #     gif_export(GifMaker, finish=True)
    #     noLoop()


def draw_e(els):
    for i, e in enumerate(els):
        stroke(0)
        t, v, w = e
        strokeWeight(w)
        if t == 'Y':
            if i % 2:
                rotateX(QUARTER_PI)
            else:
                rotateY(QUARTER_PI)
        if t == 'L':
            line_e(v)
        if t == 'C':
            line_e(v, c=w)
        if t == 'M' and i > 1:
            for _ in range(3):
                line_e(v)
                pushMatrix()
                scale(.5)
                draw_e(els[i - 5:i])
                popMatrix()
        if t == 'R' and i > 1:
            for _ in range(3):
                line_e(v)
                line_e((v[1] / 2, -v[0] / 2))
                draw_e([els[i - 1]])


def line_e(v, c=None):
    line(0, 0, v[0], v[1])
    if c is not None:
        d = PVector(v[0], v[1]).mag()
        if c != 1:
            fill(0)
        else:
            fill(255, 0, 0)
        circle(0, 0, d / c ** 2)
    translate(v[0], v[1])

def keyPressed():
    if key == ' ':
        generate()
