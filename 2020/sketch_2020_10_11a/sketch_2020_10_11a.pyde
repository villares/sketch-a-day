# import villares.ubuntu_jogl_fix  # intel video linux bug
# from villares.gif_export import gif_export
# add_library('gifAnimation')
# add_library('peasycam')

import random 

NAME = "sketch_2020_10_11a"
random.seed(101101)

elements = []

def setup():
    size(400, 400, P3D)
    frameRate(24)
    # cam = PeasyCam(this, 500)
    generate()

def generate(n=500):
    pegs = (-20, -10, 0, 0, 10, 20)
    elements[:] = [(random.choice('LCCRMY'),
                    random.sample(pegs, 2),
                    random.choice((1, 3)),)
                   for _ in range(n)]

def draw():
    lights()
    background(240, 240, 220)
    translate(width / 2, # disable if using PeasyCam
              height / 2,
              -200) 

    r = frameCount / 100.
    rotateY(r)
    draw_e(elements)

    # export_frame(r)

def export_frame(r):
    if r < TWO_PI:
        if frameCount % 2:
            gif_export(GifMaker,
                       NAME,
                       delay=100,
                       quality=0)
    else:
        gif_export(GifMaker, finish=True)
        noLoop()


def draw_e(els):
    for i, e in enumerate(els):
        t, v, w = e
        if t == 'Y':
            if i % 2:
                rotateX(QUARTER_PI)
            else:
                rotateY(HALF_PI)
        if t == 'L':
            line_e(v, w)
        if t == 'C':
            line_e(v, w, func=box_e)
        if t == 'M' and i > 1:
            for _ in range(3):
                line_e(v, w)
                pushMatrix()
                scale(.5)
                draw_e(els[i - 4:i])
                popMatrix()
        if t == 'R' and i > 1:
            for _ in range(3):
                line_e(v, w)
                line_e((v[1] / 2, -v[0] / 2), w)
                draw_e([els[i - 1]])


def line_e(v, w, func=None):
    stroke(0)
    strokeWeight(w)
    line(0, 0, v[0], v[1])
    if func:
        d = PVector(v[0], v[1]).mag()
        if w != 1:
            fill(0)
        else:
            fill(0, 0, 200)
        func(0, 0, d / (1 + w**2))
    translate(v[0], v[1])

def box_e(x, y, s):
    pushMatrix()
    translate(x, y)
    box(s)
    popMatrix()

def keyPressed():
    if key == ' ':
        generate()
