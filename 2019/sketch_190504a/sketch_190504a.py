# Alexandre B A Villares
# run this, install and run pyp5js
# instructions at https://pypi.org/project/pyp5js/

from pyp5js import *

def setup():
    createCanvas(400, 400)
    colorMode(_P5_INSTANCE.HSB, 255, 255, 255)
    frameRate(30)
    strokeWeight(2)

def draw():
    background(200)
    r = 125  # radius
    x1, y1 = 150, 200
    x2, y2 = 250, 200
    for i in range(128):
        stroke(i * 2, 200, 200)
        a1 = i * TWO_PI / 128 + HALF_PI
        sx1 = x1 + sin(a1) * r * cos(frameCount/50.)
        sy1 = y1 + cos(a1) * r * sin(frameCount/77.)
        a2 = i * TWO_PI / 128 + QUARTER_PI
        sx2 = x2 + cos(a2) * r * sin(frameCount/141.)
        sy2 = y2 + sin(a2) * r * cos(frameCount/30.)
        line(sx1, sy1, sx2, sy2)

# This is required by pyp5js to work
start_p5(setup, draw)
