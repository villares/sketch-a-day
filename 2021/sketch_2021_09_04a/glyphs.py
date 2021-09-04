from __future__ import division
import interface

class Glyph:
    glyphs = {}
    
    mode = interface.ADD
    current = None
    key_pressed = {}
    
    def __init__(self, name):
        self.name = name
        self.glyphs[name] = self
        self.paths = []
        self.current_path = None
        self.width = 4
        
    def plot(self):
        gs = self.grid_size
        for path in self.paths:
            beginShape()
            noFill()
            strokeWeight(2)
            for x, y, d in path:
                vertex(x * gs, y * gs)
            endShape()
        
    @classmethod
    def mouse_pressed(cls, mb):
        mx, my = cls.grid_mouse()

        if cls.current is None:
            cls.current = Glyph('a')
        current_glyph = cls.current
                
        if cls.mode == interface.ADD:
            cp = current_glyph.current_path
            if cp is None:
                current_glyph.paths.append([(mx, my, {})])
                current_glyph.current_path = -1
            elif mb == LEFT:
                current_glyph.paths[cp].append((mx, my, {}))
            else:
                current_glyph.current_path = None
                

    @classmethod    
    def grid_mouse(cls):
        gs = cls.grid_size
        mx = round(mouseX / gs)
        my = round(mouseY / gs)
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
        
    @classmethod
    def check_keys(cls, *args, **kwargs):
        if kwargs.get('ANY'):
            return any(cls.key_pressed.get(k, False) for k in args)
        else:
            return all(cls.key_pressed.get(k, False) for k in args)
    
    @classmethod
    def key_released(cls):
        if cls.check_keys(BACKSPACE, DELETE, ANY=True):
            cps = cls.current.paths if cls.current else None
            cp =  cls.current.current_path if cps else None 
            if cp is not None and cps[cp]:
                cps[cp].pop()
            
            
