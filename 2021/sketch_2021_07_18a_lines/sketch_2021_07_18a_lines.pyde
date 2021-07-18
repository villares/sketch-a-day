import doctest
from collections import deque

shapes = deque(([],), maxlen=20)

def setup():
    size(500, 500)
    
def draw():
    background(200)
    noFill()
    for ps in shapes:
        beginShape()
        for x, y in ps:
            vertex(x, y)
        endShape(CLOSE)
    fill(255)
    for ps in shapes:
        for x, y in ps: 
            circle(x, y, 5)
                        
    new_shapes = [] 
    ps = shapes[-1]
    for i, (x, y) in enumerate(ps):
        px, py = ps[i - 1]
        nx, ny = ps[(i + 1) % len(ps)]
        mdpn =  (dist(px, py, x, y)  +  dist(nx, ny, x, y)) / 2
        dpn =  dist(px, py, nx, ny)  
        d = 0.5  if (mdpn < 30) and (dpn < 30) else -.4
        a1 = atan2(py - y, px - x) + PI
        a2 = atan2(ny - y, nx - x) + PI
        m = (a1 + a2) / 2 
        m = m if m < TWO_PI else m - TWO_PI
        print(d)
        v = PVector.fromAngle(m) * d * 20
        line(x, y, x + v.x, y + v.y)
        new_shapes.append((x + v.x, y + v.y))
        # text("{} {}".format(degrees(a1), degrees(a2)), x, y)        
        # text(format(degrees(a1)), x, y) 
          
    if keyPressed and frameCount % 10 == 0:  
        shapes.append(new_shapes)
        
        
def mouseDragged():
    ps = shapes[-1]

    if ps and dist(ps[-1][0], ps[-1][1], mouseX, mouseY) > 10:
        ps.append((mouseX, mouseY))
    elif not ps:
        ps.append((mouseX, mouseY))


def keyPressed():
    global shapes
    if key == ' ':
        shapes = deque(([],), maxlen=10)
    
    
