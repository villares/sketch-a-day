from collections import deque
from villares.line_geometry import point_inside_poly, min_max, lerp_tuple, triangle_area

shapes = deque(([],), maxlen=20)
play = False

def setup():
    size(700, 700)
    
def draw():
    background(200)
    translate(width / 2, height / 2)
    # this started as a way of just drawing the small circles
    # for the vertices, now it draws the big ones too
    for si, ps in enumerate(shapes):
        for i, (x, y) in enumerate(ps):
            px, py = ps[i - 1]
            nx, ny = ps[(i + 1) % len(ps)]
            fill(0)
            stroke(0)
            circle(x, y, 3)
            dpn =  dist(px, py, nx, ny)  
            fill(0, 0, 200, 5)
            stroke(0, 20)
            circle((px + nx) / 2, (py + ny) / 2, dpn / (1 + si / 10))
    
    # this is to draw and to move the shapes into the screen
    # sometimes I comment out the drawing function vertex() 
    # to see just the circles
    noFill()
    if shapes and shapes[-1]:
        mi, ma = min_max(shapes[0])
        stroke(0)
        for ps in shapes:
            beginShape()
            for i, (x, y) in enumerate(ps):
                vertex(x, y)    
                ps[i] = moved(ps[i], mi, ma)
            endShape(CLOSE)

    # this mess creates new shapes on the deque, moving vertices
    # according to messy rules that I fiddle all the time
    # usually involving 3 consecutive vertices        
    new_shapes = [] 
    ps = shapes[-1] # the last shape
    for i, (x, y) in enumerate(ps):
        px, py = ps[i - 1]  # previous vertex
        nx, ny = ps[(i + 1) % len(ps)]  # next vertex
        mdpn = min(dist(px, py, x, y), dist(nx, ny, x, y))  
        dpn =  dist(px, py, nx, ny)  
        ta = abs(triangle_area((px, py), (x, y), (nx, ny)))
        a1 = atan2(py - y, px - x) + PI  # angle of incomming segment
        a2 = atan2(ny - y, nx - x) + PI  # angle of outgoing segment
        m = (a1 + a2) / 2   # average of angles, ugh!
        md = int(degrees(m if m < TWO_PI else m - TWO_PI)) # degrees now
        v = PVector.fromAngle(radians(md)) * 25
        # invert if offset vector falls inside polygon        
        v = v * -1 if point_inside_poly(x + v.x, y + v.y, ps) else v
        # this is the most messy part, deciding the movent direction
        # d = 0.5 #if (mdpn < 40) or (dpn < 40) or ta < 500 else -0.5
        d = 1 if mdpn < 50 or dpn < 50 else -1 
        v = v * d
        x2, y2 = x + v.x, y + v.y
        s = dist(x, y, x2, y2)
        # line(x, y, x + v.x, y + v.y)
        noFill()
        # circle((px + nx) / 2, (py + ny) / 2, dpn)
        new_shapes.append((x + v.x, y + v.y))
        text("{} {}".format(degrees(a1), degrees(a2)), x, y)        
        # text(format(degrees(a1)), x, y) 
          
    if new_shapes and play and frameCount % 10 == 0:  
        shapes.append(new_shapes)
        
def moved(p, mi, ma):
    mx, my = lerp_tuple(mi, ma, 0.5)
    if not play:
        return p
    V = 1.5
    B = 10
    if mx < -B:
        new_x = p[0] + V
    elif mx > B:
        new_x = p[0] - V
    else:
        new_x = p[0]
    if my < -B:
        new_y = p[1] + V
    elif my > B:
        new_y = p[1] - V
    else:
        new_y = p[1]
    return (new_x, new_y)
            
def mouseDragged():
    if shapes:
        ps = shapes[-1]
        omx, omy = mouseX - width / 2, mouseY - height / 2 # offset mouseX & Y
        if not ps or ps and ps[-1] and mouse_away(ps[-1][0], ps[-1][1], 25):
            ps.append((omx, omy))

def mouse_away(x, y, distance):
    omx, omy = mouseX - width / 2, mouseY - height / 2
    return dist(x, y, omx, omy) > distance

def keyPressed():
    global shapes, play
    if key == ' ':
        shapes = deque(([],), maxlen=20)
    elif key == 'p':
        play = not play
    
