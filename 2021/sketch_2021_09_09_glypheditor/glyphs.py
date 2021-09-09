import interface

class Glyph:
    glyphs = {}
    
    def __init__(self, name):
        self.name = name
        self.glyphs[name] = self
        self.paths = []
        self.width = 4
        
    def plot(self, s=1):
        gs = interface.grid_size
        for path in self.paths:
            beginShape()
            noFill()
            strokeWeight(2)
            for x, y, d in path:
                vertex(x * gs * s, y * gs * s)
            endShape()
        

            
