from villares.line_geometry import edges_as_sets, draw_poly, triangle_area
from villares.colors import random_hue_saturated

def setup():
    global cells
    size(400, 400)    
    pa = PVector(100, 100)
    pb = PVector(200, 100)
    pc = PVector(200, 200)
    pd = PVector(100, 200)
    pe = PVector(300, 100)
    pf = PVector(300, 200)
    
    c1 = Cell((pa, pc, pb, pd))    
    c2 = Cell((pb, pe, pf, pc))
    c3 = c1 + c2
    cells = (c1, c2, c3)
    strokeWeight(3)
    
def draw():
    background(240)
    for cell in cells:
        translate(6, 3)
        cell.draw()

def mouseDragged():
    for cell in cells:
        cell.move_point(mouseX, mouseY, (mouseX - pmouseX), (mouseY - pmouseY))

class Cell:
    
    def __init__(self, pts):
        self.pts = list(pts)
        self.edges = edges_as_sets(pts, frozen=False)
        self.colour = random_hue_saturated(200)
        
    def draw(self):
        for a, b in self.edges:
            stroke(self.colour)
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
    
    def move_point(self, mx, my, dx, dy):
        for i, (x, y, z) in enumerate(self.pts):
            if dist(x, y, mx, my) < 10:
                self.pts[i].set(x + dx, y + dy)
                
                        
