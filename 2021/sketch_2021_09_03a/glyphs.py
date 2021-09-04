from __future__ import division

class Glyph:
    
    glyphs = []
    mode = ADD
    current = None
    
    def __init__(self):
        self.current_path = None
        self.paths = []
        self.glyphs.append(self)
        
    def plot(self):
        for path in self.paths:
            beginShape()
            noFill()
            for x, y, d in path:
                vertex(x, y)
            endShape()
        
    @classmethod
    def mouse_pressed(cls, mb):
        mx, my = cls.grid_mouse()

        if cls.current is None:
            cls.current = Glyph()
        current_glyph = cls.current
                
        if cls.mode == ADD:
            cp = current_glyph.current_path
            if cp is None:
                current_glyph.paths.append([(mx, my, {})])
                current_glyph.current_path = -1
            else:
                current_glyph.paths[cp].append((mx, my, {}))

    @classmethod    
    def grid_mouse(cls):
        gs = cls.grid_size
        mx = round(mouseX / gs) * gs
        my = round(mouseY / gs) * gs
        return mx, my      
                
    @classmethod
    def draw_grid(cls):
        push()
        for x in range(0, width, cls.grid_size):
            for y in range(0, height, cls.grid_size):
                if dist(mouseX, mouseY, x, y) < cls.grid_size / 2:
                    stroke(255, 0, 0)
                else:
                    stroke(255)
                strokeWeight(2)
                point(x, y)
        pop()
