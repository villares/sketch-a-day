
from villares.helpers import lerp_tuple


class Glyph:
    
    module_size = 5    
    glyphs = {}
    
    def __init__(self, name):
        self.name = name
        self.glyphs[name] = self
        self.paths = []
        self.width = 5
        
    def plot(self, ox=0, oy=0, module_size=None, **kwargs):
        sw = kwargs.pop('stroke_weight', 2)
        ms = self.module_size = module_size or self.module_size
        strokeWeight(sw)
        # for path in self.paths:
        #     beginShape()
        #     noFill()    
        #     for x, y, d in path:
        #         sx, sy = x + ox, y + oy
        #         vertex(sx * ms, sy * ms)
        #     endShape()
        for path in self.paths:
            noFill()
            push()
            translate(ox * ms, oy * ms)
            for (xa, ya, d), (xb, yb, d) in zip(path, path[1:]):
                self.my_line(xa * ms, ya * ms, xb * ms, yb *ms)
            pop()
    
    def my_line(self, xa, ya, xb, yb):
        ms = self.module_size
        if 4.2 * ms > dist(xa, ya, xb, yb) > 1.5 * ms: 
            xa2, ya2 = lerp_tuple((xa, ya), (xb, yb), 0.33)
            xb2, yb2 = lerp_tuple((xa, ya), (xb, yb), 0.66)
            line(xa, ya, xa2, ya2)
            line(xb2, yb2, xb, yb)       
        else:    
            line(xa, ya, xb, yb) 

            
