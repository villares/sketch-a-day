"""
Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day

Converting some of Maeda's Design by Number
dbnletters.dbn code -> Processing
"""
from dbn_generate_letters import convert_dbn_source_letters
from dbn_generate_polys import convert_dbn_source_polys

from dbn_letters import *
from dbn_polys import *

debug_poly = True

def setup():
    colorMode(HSB)
    size(800, 400)
    fill(0)
    text("Press 't' tto draw letters, and to generate code press 'g'(lines) or 'G'(polys)", 10, 20)

def keyPressed():
    global debug_poly
    if key == 'g':
        convert_dbn_source_letters("data/dbnletters.dbn")
    if key == 'G':
        convert_dbn_source_polys("data/dbnletters.dbn")
    if key == 't':
        dbn_test()
    if key == 'd':
        debug_poly = not debug_poly
        println("debug mode: " + repr(debug_poly))
        stroke(0)
    if key == "s":
        saveFrame("###.png")

def draw():
    scale(4, 4)

def dbn_test():
    background(200)
    noFill()
    pushMatrix()
    strokeCap(ROUND)
    for y in range(0, 5):
        for x in range(1, 6):
            dbn_letter[x + y * 5](x * 12, -20 - y * 12, debug_poly)
    dbn_letterZ(x * 12 + 12, -32 - y * 12)
    translate(100, 0)   
    strokeCap(PROJECT)
    for y in range(0, 5):
        for x in range(1, 6):
            dbn_p_letter[x + y * 5](x * 12, -20 - y * 12, debug_poly)
    dbn_letterZ(x * 12 + 12, -32 - y * 12)
    popMatrix()
