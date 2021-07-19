import doctest
from collections import deque

shapes = deque(([],), maxlen=10)

def setup():
    size(500, 500)
    
def draw():
    background(200)
    noFill()
    for ps in shapes:
        beginShape()
        for i, (x, y) in enumerate(ps):
            vertex(x, y)
            if shapes[0]:
                 ps[i] = moved(ps[i], shapes[0][0])

        endShape(CLOSE)
    fill(0)
    for ps in shapes:
        for x, y in ps: 
            circle(x, y, 3)
                        
    new_shapes = [] 
    ps = shapes[-1]
    for i, (x, y) in enumerate(ps):
        px, py = ps[i - 1]
        nx, ny = ps[(i + 1) % len(ps)]
        mdpn =  (dist(px, py, x, y)  +  dist(nx, ny, x, y)) / 2
        dpn =  dist(px, py, nx, ny)  
        d = 0.5 if (mdpn < 30) and (dpn < 30) else -0.5
        a1 = atan2(py - y, px - x) + PI
        a2 = atan2(ny - y, nx - x) + PI
        m = (a1 + a2) / 2 
        md = int(degrees(m if m < TWO_PI else m - TWO_PI) / 30)
        # print(d)
        v = PVector.fromAngle(radians(md * 30 + 90)) * d * 20
        # line(x, y, x + v.x, y + v.y)
        new_shapes.append((x + v.x, y + v.y))
        # text("{} {}".format(degrees(a1), degrees(a2)), x, y)        
        # text(format(degrees(a1)), x, y) 
          
    if keyPressed and frameCount % 10 == 0:  
        shapes.append(new_shapes)
        
def moved(p, fp):
    V = 0.5
    B = 1
    if fp[0] < width / 2 - B:
        new_x = p[0] + V
    elif fp[0] > width / 2 + B:
        new_x = p[0] - V
    else:
        new_x = p[0]
    if fp[1] < height / 2 - B:
        new_y = p[1] + V
    elif fp[1] > height / 2 + B:
        new_y = p[1] - V
    else:
        new_y = p[1]
    return (new_x, new_y)
            
def mouseDragged():
    ps = shapes[-1]
    if ps and dist(ps[-1][0], ps[-1][1], mouseX, mouseY) > 25:
        ps.append((mouseX, mouseY))
    elif not ps:
        ps.append((mouseX, mouseY))


def keyPressed():
    global shapes
    if key == ' ':
        shapes = deque(([],), maxlen=10)
    
    
