points, black_lines, white_lines = [], [], [] 
margin = 40

def setup():
    size(600, 600)
    create_points()
    
def create_points():
    points[:] = []
    black_lines[:]  = []
    white_lines[:] = []
    for _ in range(4):
        w = random(margin, width - margin) // 40 * 40
        h = random(margin, height - margin) // 40 * 40
        x = random(margin, width - margin - w) // 40 * 40
        y = random(margin, height - margin - h) // 40 * 40
        points.extend(((x, y), (x + w, y), (x + w, y + h), (x, y + h)))
    for p in points:
        for other in reversed(points):
            if p is other: 
                break
            xa, ya = p
            xb, yb = other
            if xa == xb or ya == yb:
                white_lines.append((xa, ya, xb, yb))
            else:
                black_lines.append((xa, ya, xb, yb))
 
def draw():
    background(240)                    
    stroke(255)
    strokeWeight(3)
    for xa, ya, xb, yb in white_lines:
        line(xa, ya, xb, yb)
    stroke(0)
    strokeWeight(1)
    for xa, ya, xb, yb in black_lines:
        line(xa, ya, xb, yb)
            
def keyPressed():
    create_points()
    
