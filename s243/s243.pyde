h, a, f = [], [], []
n = 6

def setup():
    size(1024, 300)
    blendMode(ADD)
    background(0)
    
def keyPressed():
    h[:], a[:], f[:] = [], [], []
    for i in range(n):
        h.append(random(-height/4,height/2))
        a.append(random(-height/2, height/2))
        f.append(random(.2, 5))

def draw():
    background(0)
    translate(0, height/2)
    for x in range(width):
        if len(h) > 0:
           for i in range(2, n):
            ang = x / 30.
            if i % 3 == 0:
                stroke(255, 0, 0)
            elif i % 3 == 1:
                stroke(0, 255, 0)
            else:
                stroke(0, 0, 255)
            s = (sin(ang * f[i]) * a[i] + 
                 sin(ang * f[i-1]) * a[i-1] + 
                 sin(ang * f[i-2]) * a[i-2]
                 )
            line(x, h[i], x, h[i] + s)
