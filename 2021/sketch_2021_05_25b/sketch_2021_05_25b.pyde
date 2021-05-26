from __future__ import division
from datetime import datetime
from villares.gif_export import gif_export
add_library('gifAnimation')

from shapes import Shape

def setup():
    global ds
    size(1024, 1024)
    # noStroke()
    noSmooth()
    frameRate(10)
    Shape((0, 0), (width, 0), (width, height), (0, height))
    ds = str(datetime.now())
    
def draw():
    clear()
    Shape.update_all()
    if frameCount % 2 == 0:
        gif_export(GifMaker, ds, delay=200)

def keyPressed():
    if key == ' ':
        Shape.update_all(divide=True)
        gif_export(GifMaker, ds, delay=200)
    if key == 'e':
        gif_export(GifMaker, finish=True)

def mousePressed():
    Shape.shapes.clear()
    Shape((0, 0), (width, 0), (width, height), (0, height))
