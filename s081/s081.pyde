SKETCH_NAME = "s081"
"""
sketch 81 180322 - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day
"""

add_library('gifAnimation')
from gif_exporter import gif_export
from slider import Slider

A = Slider(1, 40, 10)
B = Slider(1, 40, 10)
C = Slider(1, 40, 10)
D = Slider(1, 40, 10)
a, b, c, d = 1, 1, 1, 1

def setup():
    size(600, 600, P2D)
    colorMode(HSB)
    noFill()
    A.position(20, height - 70)
    B.position(20, height - 30)
    C.position(width - 140, height - 70)
    D.position(width - 140, height - 30)
    #noLoop()

def draw():
    global a, b, c, d
    rect(10, 10, 100, 100)
    background(200)
    frameRate(30)

    randomSeed(int(d * 100))

    func = ellipse
    for _ in range(d):
        tam = a * c
        x = int(random( width - tam))
        y = int(random( height - tam))
        stroke(0)
        grid(x, y, a, b, c) #, ellipse, (a, a))
        x = int(random( width - tam))
        y = int(random( height - tam))    
        stroke(255)
        grid(x, y, a, b, c) #, ellipse, (a, a))
    
    a = int(A.value())  # elem num
    b = int(B.value())  # size
    c = int(C.value())  # space
    d = int(D.value())  # grid num

    # uncomment next lines to export GIF
    if not frameCount % 10: gif_export(GifMaker,
                                       frames=2000,
                                       filename=SKETCH_NAME)

def grid(x, y, num, size_, space): #, func, *args):
    for i in range(x, x + num * space, space):
        for j in range(y, y + num * space, space):
            ellipse(i, j, size_, size_)
            
