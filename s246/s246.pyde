curvas = []
n = 6

def setup():
    size(1024, 300)
    blendMode(ADD)
    background(0)
    
def keyPressed():
    curvas[:] = []
    for i in range(n):
        curvas.append((random(-height/4,height/4),
                  random(-height/4, height/4),
                  random(.2, 5),
                  random(.2, 5),
                  random(.2, 5),
                 ))

def draw():
    background(0)
    translate(0, height/2)
    for i, h, a, f1, f2, f3 in enumerate(curvas[::2]):
        if int(a) % 3 == 0:
            stroke(255, 0, 0)
        elif int(a) % 3 == 1:
            stroke(0, 255, 0)
        else:
            stroke(0, 0, 255)
        beginShape()
        for x in range(width):
            ang = x / 30.

                stroke(0, 0, 255)
            s = sin(ang * f1) + sin(ang * f2) + sin(ang * f3) 
            vertex(x, h+ s * a)
        endShape(CLOSE)
