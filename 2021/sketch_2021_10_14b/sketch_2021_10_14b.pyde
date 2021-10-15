from random import shuffle
tris = []
unvisited_tris = []

def setup():
    size(600, 600)
    inicial = ((0, -10), (0, 10), (15, 0))
    tris.append(inicial) 
    unvisited_tris.append(inicial)
    noCursor()
    
def draw():
    background(200)
    translate(width / 2, height / 2)
    stroke(255, 30)
    fill(0, 0, 100, 100)
    for t in tris:
        beginShape()
        for x, y in t:
            vertex(x, y)
        endShape(CLOSE)
    
    
def keyPressed():
    shuffle(unvisited_tris)
    for t in reversed(unvisited_tris):
        grow(t)
        unvisited_tris.remove(t)
    # print len(tris), len(visited_tris)
                
def grow(t):        
    edges = get_edges(t)
    for e in edges:
        a = edge_angle(e)
        m = midpoint(e)
        d = edge_dist(e) * 0.87 
        p = point_offset(m, d, a - HALF_PI)
        if not point_in_tris(p):
            new_t = (e[0],  p, e[1])
            tris.append(new_t)
            unvisited_tris.append(new_t)
                                                                                    
def get_edges(t):
    return [((xa, ya), (xb, yb)) for (xa, ya), (xb, yb)
             in zip(t, t[1:] + (t[0],))]
        
def edge_angle(edge):
    (xa, ya), (xb, yb) = edge
    return atan2(yb - ya, xb - xa) + PI

def point_offset(p, offset, angle):
    return (int(p[0] + offset * cos(angle)),
            int(p[1] + offset * sin(angle)))  

def point_in_tris(p):
    for t in tris:
        if point_inside_poly(p[0], p[1], t):
            return True
    return False
    
def point_inside_poly(x, y, points):
    # ray-casting algorithm based on
    # https://wrf.ecse.rpi.edu/Research/Short_Notes/pnpoly.html
    inside = False
    for i, p in enumerate(points):
        pp = points[i - 1]
        xi, yi = p
        xj, yj = pp
        intersect = ((yi > y) != (yj > y)) and (
            x < (xj - xi) * (y - yi) / (yj - yi) + xi)
        if intersect:
            inside = not inside
    return inside  

def edge_dist(edge):
    (xa, ya), (xb, yb) = edge
    return dist(xa, ya, xb, yb)

def midpoint(edge):
    (xa, ya), (xb, yb) = edge
    return (xa + xb) / 2.0, (ya + yb) / 2.0
