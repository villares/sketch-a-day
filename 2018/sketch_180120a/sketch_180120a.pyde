"""
s18020 - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day


Converting some of Maeda's Design by Number
dbnletters.dbn code -> Processing
"""
from dbn_generate_poly import *
from dbn_polys import *

debug_poly = False

def setup():
    colorMode(HSB)
    size(400, 400)
    strokeCap(PROJECT)
    noFill()
    # noLoop()
    # dbn_test()

def keyPressed():
    global debug_poly
    if key == 'g':
        convert_dbn_source("data/dbnletters.dbn")
    if key == 't':
        dbn_test()
    if key == 'd':
        debug_poly = not debug_poly
        println("debug mode: " + repr(debug_poly))
        stroke(0)

def draw():
    scale(4, 4)

def dbn_test():
    for y in range(0, 5):
        for x in range(1, 6):
            dbn_letter[x + y * 5](x * 12, -20 - y * 12, debug_poly)
    dbn_letterZ(x * 12 + 12, -32 - y * 12)
