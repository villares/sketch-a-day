"""
A reboot of a simple poly / linerar glyphs editor
"""

from glyphs import Glyph
import interface

def setup():
    global half_grid_h
    size(600, 600)
    strokeJoin(ROUND)
    # interface.grid_size = 20    
    half_grid_h = height // interface.grid_size // 2

def draw():
    background(200)
    interface.draw_grid()
    interface.show_mode()
    gs = interface.grid_size
    gc = interface.current_glyph
    if gc:
        fill(0)
        textSize(20)
        text(gc.name, gs, gs)
        textSize(8)
        gc.plot()
        text(str(gc.paths), gs, gs * half_grid_h)
    
    translate(0, gs * half_grid_h)        
    for gl in Glyph.glyphs.values():
        s = 0.25
        gl.plot(s)
        translate((gl.width + 1) * gs * s, 0)
        
def mousePressed(): interface.mouse_pressed(mouseButton)
    
def mouseDragged(): interface.mouse_dragged(mouseButton)

def mouseReleased(): interface.mouse_released(mouseButton)

def keyPressed():
    interface.keys_pressed[key if key != CODED else keyCode] = True

def keyReleased():
    interface.key_released(key, keyCode)
    interface.keys_pressed[key if key != CODED else keyCode] = False
