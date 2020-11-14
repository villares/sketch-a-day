from villares.line_geometry import edges_as_sets, draw_poly

def setup():
    global c1, c2
    size(400, 400)    
    pa = (100, 100)
    pb = (200, 100)
    pc = (200, 200)
    pd = (100, 200)
    pe = (300, 100)
    pf = (300, 200)
    
    c1 = Cell((pa, pb, pc, pd))    
    c2 = Cell((pb, pe, pf, pc))
    
    strokeWeight(3)
    
def draw():
    fill(0)
    stroke(200, 0, 0)
    c1.draw()

    translate(3, 0)
    stroke(0, 0, 200)
    c2.draw()

    c3 = c1 + c2

    translate(5, 5)
    fill(255, 0, 0)
    stroke(150, 0, 150)
    c3.draw()

class Cell:
    
    def __init__(self, pts):
        self.pts = list(pts)
        self.edges = edges_as_sets(pts, frozen=False)
        
    def draw(self):
        for a, b in self.edges:
            line(a[0], a[1], b[0], b[1])
            
    def __add__(self, other):
        new_edges = self.edges ^ other.edges
        pts = []
        # for a, b in self.edges | other.edges:
        for a, b in new_edges:
            pts.append(a); pts.append(b)
        new_cell = Cell(list(set(pts)))
        new_cell.edges = new_edges
        return new_cell    
                        
        
        
