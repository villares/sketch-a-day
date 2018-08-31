curvas = []
n = 6

def setup():
    size(1024, 300)
    blendMode(ADD)
    background(0)
    
def keyPressed():
    curvas[:] = []
    for i in range(n):
        h.append((random(-height/4,height/2)),
        random(-height/2, height/2)),
         random(.2, 5)
                 )

def draw():
    background(0)
    translate(0, height/2)
    for x in range(width):
          for h, f, a in curvas:
            ang = x / 30.
            if h % 3 == 0:
                stroke(255, 0, 0)
            elif h % 3 == 1:
                stroke(0, 255, 0)
            else:
                stroke(0, 0, 255)
            s = sin(ang * f) * a
            line(x, 0, x, h + s)
