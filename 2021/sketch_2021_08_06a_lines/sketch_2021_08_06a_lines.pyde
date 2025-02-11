from collections import deque
from villares.line_geometry import point_inside_poly, min_max, lerp_tuple, triangle_area

shapes = deque(([],), maxlen=20)
play = False

def setup():
    size(700, 700)
    
def draw():
    background(200)
    noFill()
    if shapes[0]:
        mi, ma = min_max(shapes[0])
        me = lerp_tuple(mi, ma, 0.5)
        for ps in shapes:
            beginShape()
            for i, (x, y) in enumerate(ps):
                vertex(x, y)    
                ps[i] = moved(ps[i], me)
    
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
        mdpn = min(dist(px, py, x, y), dist(nx, ny, x, y))  
        dpn =  dist(px, py, nx, ny)  
        ta = abs(triangle_area((px, py), (x, y), (nx, ny)))
        # d = 0.5 #if (mdpn < 40) or (dpn < 40) or ta < 500 else -0.5
        d = 0.5 if ta < 100 or mdpn < 50 else -0.5

        a1 = atan2(py - y, px - x) + PI
        a2 = atan2(ny - y, nx - x) + PI
        m = (a1 + a2) / 2 
        md = int(degrees(m if m < TWO_PI else m - TWO_PI) / 30)
        v = PVector.fromAngle(radians(md * 30)) * 25 #min(max(ta, -5), 10)
        if point_inside_poly(x + v.x, y + v.y, ps):
            v = v * -1 * (i % 2)
        v = v * d
        x2, y2 = x + v.x, y + v.y
        s = dist(x, y, x2, y2)
        # line(x, y, x + v.x, y + v.y)
        noFill()
        circle((px + nx) / 2, (py + ny) / 2, dpn)
        
        new_shapes.append((x + v.x, y + v.y))
        # text("{} {}".format(degrees(a1), degrees(a2)), x, y)        
        # text(format(degrees(a1)), x, y) 
          
    if play and frameCount % 10 == 0:  
        shapes.append(new_shapes)
        
def moved(p, fp):
    if not play:
        return p
    V = 1.5
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
    global shapes, play
    if key == ' ':
        shapes = deque(([],), maxlen=100)
    elif key == 'p':
        play = not play
    
