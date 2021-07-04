add_library('peasycam')

def setup():
    size(400, 400, P3D)
    cam = PeasyCam(this, 400)
    strokeWeight(5)

def draw():
    background(0, 0, 200)
    translate(-200, -200)
    s = 50
    points = ((100, 100, 0), (300, 100, 0), (300, 250, 0), (150, 300, 0), (100, 250, 0))
    fill(255, 100)
    plot(points)
    
    o = points[0]
    a = sub_v(o, points[1])
    b = sub_v(o, points[-1])
    c = cross_v(a, b)
    c = norm_v(c)  # normalize
    c = scale_v(c, s) # scale
    
    other_points = add_m(points, c)
    for (x1, y1, z1), (x2, y2, z2) in zip(points, other_points):
        line(x1, y1, z1, x2, y2, z2)
    noFill()
    plot(other_points)
                                                                                                                                             

def cross_v(a, b):
    return (a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0])
    
def mag_v(v):
    return sqrt(sum(component ** 2 for component in v))

def norm_v(v):
    m = mag_v(v)
    return tuple(component / m for component in v)
    
def scale_v(v, s):
    return tuple(component * s for component in v)   
                                                
def sub_v(a, b):
    return tuple(ca - cb for ca, cb in zip(a, b))
    
def add_v(a, b):
    return tuple(ca + cb for ca, cb in zip(a, b))
    
def add_m(points, v):
    return tuple(add_v(p, v) for p in points)
    
def plot(points):
    beginShape()
    for p in points:
        vertex(*p)
    endShape(CLOSE)
