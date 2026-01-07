# PY5 IMPORTED MODE CODE

from py5 import *

class Glyph:
    
    module_size = 5    
    glyphs = {}
    
    def __init__(self, name):
        self.name = name
        self.glyphs[name] = self
        self.paths = []
        self.width = 5
        
    def plot(self, ox=0, oy=0, module_size=None):
        ms = module_size or self.module_size
        for path in self.paths:
            begin_shape()
            no_fill()
            #stroke_weight(3)
            for x, y, d in path:
                sx, sy = x + ox, y + oy
                vertex(sx * ms, sy * ms)
            end_shape()
        

            
