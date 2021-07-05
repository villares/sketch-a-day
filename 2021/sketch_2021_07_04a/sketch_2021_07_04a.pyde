add_library('peasycam')

def setup():
    size(400, 400, P3D)
    cam = PeasyCam(this, 400)
    strokeWeight(5)

def draw():
    background(200)
    translate(-200, -200)
    s = 50
    points = ((100, 100, 30), (200, 50, 0), (300, 100, 0),
              (300, 250, 0), (150, 300, -30), (100, 250, 0))
    fill(200, 0, 0, 128)
    
    # plot(points)
    triangles = triangulate(points) 
    print(len(triangles))
    for tri in triangles:
        plot(tri)
    
    other_points = []
    for i, p in enumerate(points):
        previous_p = points[i - 1]
        next_p = points[(i + 1) % len(points)]
        pn = p_normal(p, previous_p, next_p)
        scaled_pn = scale_v(pn, s) # scale
        other_points.append(add_v(p, scaled_pn))
    
    for (x1, y1, z1), (x2, y2, z2) in zip(points, other_points):
        line(x1, y1, z1, x2, y2, z2)
            
    fill(0, 0, 200, 128)
    for tri in triangulate(other_points):
        plot(tri)
        
def triangulate(points):
    triangles = [(points[0], points[1], points[-1])] 
    for a in range(1, len(points) // 2 - 1):
        triangles.append((points[a + 1], points[a], points[-a]))
        triangles.append((points[a + 1], points[-a], points[-(a + 1)]))
    return triangles
                                                                                                                                                                                                                            

def p_normal(p, previous_p, next_p):
    a = sub_v(p, next_p)
    b = sub_v(p, previous_p)
    c = cross_v(a, b)
    return norm_v(c)  # normalize
    

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
    
