points = []
margin = 40

def setup():
    size(600, 600)
    create_points()
    
def create_points():
    points[:] = []
    for _ in range(4):
        w = random(margin, width - margin) // 40 * 40
        h = random(margin, height - margin) // 40 * 40
        x = random(margin, width - margin - w) // 40 * 40
        y = random(margin, height - margin - h) // 40 * 40
        points.extend(((x, y), (x + w, y), (x + w, y + h), (x, y + h)))

def draw():
    background(240)
    for p in points:
        for other in reversed(points):
            if p is other: 
                break
            xa, ya = p
            xb, yb = other
            if xa == xb or ya == yb:
                strokeWeight(3)
            else:
                strokeWeight(1)
            line(xa, ya, xb, yb)
            
def keyPressed():
    create_points()
    
