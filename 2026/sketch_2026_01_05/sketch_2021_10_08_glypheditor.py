"""
A reboot of a simple poly / linerar glyphs editor
"""

from glyphs import Glyph
import interface

def setup():
    global half_grid_h
    size(600, 600)
    stroke_join(ROUND)
    # interface.grid_size = 20    
    half_grid_h = height // interface.grid_size // 2

def draw():
    background(200)
    gs = interface.grid_size
    gc = interface.current_glyph
    ox, oy = interface.OX, interface.OY 
    interface.draw_grid(gc)
    interface.show_mode()
    if gc:
        fill(0)
        textSize(20)
        text(gc.name, gs, gs)
        textSize(8)
        gc.plot(ox, oy, gs)
        text(str(gc.paths), gs, gs * (half_grid_h - 1))
    
    translate(0, gs * half_grid_h) 
    x, y = gs, 2 * gs      
    for gl in Glyph.glyphs.values():
        push()
        translate(x, y)
        s = 0.25
        gl.plot(module_size=gs * s)
        pop()
        x += (gl.width + 1) * gs * s
        if x > width - 220:
            x = gs
            y += 4 * gs
        
def mouse_pressed():
    interface.mouse_pressed(mouse_button)
    
def mouse_dragged():
    interface.mouse_dragged(mouse_button)

def mouse_released():
    interface.mouse_released(mouse_button)

def key_pressed():
    interface.keys_pressed[key if key != CODED else key_code] = True

def key_released():
    interface.key_released(key, key_code)
    interface.keys_pressed[key if key != CODED else key_code] = False
