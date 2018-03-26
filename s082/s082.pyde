SKETCH_NAME = "s082"
"""
sketch 82 180323 - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day
"""

add_library('gifAnimation')
from gif_exporter import gif_export
from slider import Slider

A = Slider(1, 40, 10)
B = Slider(1, 40, 10)
C = Slider(1, 40, 10)
D = Slider(1, 40, 10)
# I need these globals because I want to call the sliders after drawing
a, b, c, d = 1, 1, 1, 1
SHAPES = [ellipse, rect, lambda x, y, c, _: rect(x, y, c, c, c/2)]

def setup():
    size(600, 600, P2D)
    frameRate(30)
    colorMode(HSB)
    rectMode(CENTER)
    noFill()
    A.position(20, height - 70)
    B.position(20, height - 30)
    C.position(width - 140, height - 70)
    D.position(width - 140, height - 30)
    # noLoop()

def draw():
    global a, b, c, d
    background(200)
    randomSeed(int(d * 100))

    func = ellipse
    for i in range(d):
        tam = a * c
        x = int(random(width - tam))
        y = int(random(height - tam))
        if i % 2:
            stroke(0)
        else:
            stroke(255)
        grid(x, y, a, b, c, rnd_choice(SHAPES))  # , ellipse, (a, a))

    a = int(A.value())  # elem num
    b = int(B.value())  # size
    c = int(C.value())  # space
    d = int(D.value())  # grid num

    # uncomment next lines to export GIF
    if not frameCount % 10:
        gif_export(GifMaker,
                   frames=2000,
                   filename=SKETCH_NAME)

def grid(x, y, num, size_, space, func):  # , func, *args):
    for i in range(x, x + num * space, space):
        for j in range(y, y + num * space, space):
            func(i, j, size_, size_)
            
def rnd_choice(collection):
    i = int(random(len(collection)))
    return collection[i]
