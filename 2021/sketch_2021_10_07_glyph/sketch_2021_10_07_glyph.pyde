"""
A reboot of a simple poly / linerar glyphs editor
"""

import pickle
from glyphs import Glyph
import interface

def setup():
    size(600 , 600)
    strokeJoin(ROUND)
    # interface.grid_size = 20    
    with open("glyphs.pickle") as f:
        Glyph.glyphs = pickle.load(f)
        print('glyphs loaded')


def draw():
    background(200)
    glyphs = Glyph.glyphs
    gs = 7
    t = interface.phrase
    ox, oy = interface.OX, interface.OY 
    push()
    x = 200
    y = 10
    for c in t:
        gl = glyphs.get(c)
        if gl:
            gl.plot(ox + x, oy + y, gs,  stroke_weight=4)
            x += gl.width
        else:
            x += 5
        if x * gs > width:
            x = 0
            y += 12   
        
    pop()
    translate(0, height / 2) 
    x, y = 1 * gs, 2 * gs      
    for gl in Glyph.glyphs.values():
        push()
        translate(x, y)
        s = 0.45
        gl.plot(module_size=gs * s, stroke_weight=1)
        pop()
        x += (gl.width + 1) * gs * s
        if x > width - 40:
            x = gs
            y += 4 * gs

def keyPressed():
    interface.keys_pressed[key if key != CODED else keyCode] = True

def keyReleased():
    interface.key_released(key, keyCode)
    interface.keys_pressed[key if key != CODED else keyCode] = False
