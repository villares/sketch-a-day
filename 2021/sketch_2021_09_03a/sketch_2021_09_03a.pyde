
from glyphs import Glyph


def setup():
    size(500, 500)
    Glyph.grid_size = 25    

def draw():
    background(200)
    Glyph.draw_grid()
    for gl in Glyph.glyphs:
        gl.plot()
        
def mousePressed():
    Glyph.mouse_pressed(mouseButton)
    
    
