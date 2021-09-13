
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
        ms = module_size or self.module_size
        for path in self.paths:
            beginShape()
            noFill()
            strokeWeight(sw)
            for x, y, d in path:
                sx, sy = x + ox, y + oy
                vertex(sx * ms, sy * ms)
            endShape()
        

            
