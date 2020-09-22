

class Ponto():
    
    SIZE = 5
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.f = 255
        
    def __getitem__(self, i):
        return (self.x, self.y)[i]
        
    def draw(self):
        fill(self.f)
        circle(self.x, self.y, Ponto.SIZE)
