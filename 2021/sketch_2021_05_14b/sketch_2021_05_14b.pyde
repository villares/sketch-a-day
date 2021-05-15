elements = []

def setup():
    size(500, 500)
    for _ 
    e = Element(100, 100, 400, 400)
    e.display()


class Element:
    
    def __init__(self, x1, y1, x2, y2):
        self.p1 = PVector(x1, y1)
        self.p2 = PVector(x2, y2)
        self.points = [PVector.lerp(self.p1, self.p2,
                                    (i + 1)/11.0)
                           for i in range(10)]
        
        
    def display(self):
        for p in self.points + [self.p1, self.p2]:
            circle(p.x, p.y, 3)
        
            
