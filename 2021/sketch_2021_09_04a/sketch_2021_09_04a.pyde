
from glyphs import Glyph


def setup():
    size(600, 600)
    Glyph.grid_size = 25    

def draw():
    background(200)
    Glyph.draw_grid()
    gs = Glyph.grid_size
    gc = Glyph.current
    if gc:
        fill(0)
        textSize(20)
        text(gc.name, 25, 25)
        gc.plot()
    
    translate(0, gs * 10)        
    for gl in Glyph.glyphs.values():
        gl.plot()
        translate(gl.width, 0)
        
def mousePressed():
    Glyph.mouse_pressed(mouseButton)
    
# def mouseDragged():
#     Glyph.mouse_dragged(mouseButton)
# def mouseReleased():
#     Glyph.mouse_released(mouseButton)

def keyPressed():
    Glyph.key_pressed[key if key != CODED else keyCode] = True

def keyReleased():
    Glyph.key_released()
    Glyph.key_pressed[key if key != CODED else keyCode] = False
