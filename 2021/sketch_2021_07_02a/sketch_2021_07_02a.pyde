add_library('peasycam')

def setup():
    size(400, 400, P3D)
    cam = PeasyCam(this, 400)
    strokeWeight(5)

def draw():
    background(0, 0, 200)
    s = 50
    # a = PVector(s, 0, 0)
    # b = PVector(0, s, 0)
    # c = PVector.cross(a, b)    # cross product    
    # c = c.normalize() * s
    
    a = (s, 0, 0)
    b = (0, s, 0)
    c = (a[1] * b[2] - a[2] * b[1],
         a[2] * b[0] - a[0] * b[2],
         a[0] * b[1] - a[1] * b[0])
    c_mag = sqrt(c[0] ** 2 + c[1] ** 2 + c[2] ** 2) 
    c = c[0] / c_mag, c[1] / c_mag, c[2] / c_mag  # normalize
    c = c[0] * s, c[1] * s, c[2] * s              # scale
                 
                                                   
    line(0, 0, 0, a[0], a[1], a[2]) # a
    line(0, 0, 0, b[0], b[1], b[2]) # b
    line(0, 0, 0, c[0], c[1], c[2]) # c

    
            
