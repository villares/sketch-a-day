
pts = []

def setup():
    size(500, 500)
    for i in range(4):
        pts.append((random(100, width - 100), random(100, height - 100)))
        
def draw():
    plot_poly(pts)
    
        
def plot_poly(points):
    beginShape()
    for p in points:
        vertex(*p)    
    endShape(CLOSE)
