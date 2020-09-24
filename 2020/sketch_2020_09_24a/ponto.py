# -*- coding: UTF-8 -*-


class Ponto():
    
    SIZE = 5
    
    def __init__(self, x, y):
        self.ox = x
        self.oy = y
        self.x = x
        self.y = y
        self.f = 255
        
    def __len__(self):
        return 2
        
    def __iter__(self):
        return iter((self.x, self.y))
    
    def __getitem__(self, i):
        return (self.x, self.y)[i]
        
    def draw(self):
        fill(self.f)
        circle(self.x, self.y, Ponto.SIZE)
