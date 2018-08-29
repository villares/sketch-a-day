
h, a, f = [], [], []
n = 18

def setup():
    size(1024, 300)
    blendMode(ADD)
    background(0)
    for i in range(n):
        h.append(random(-height/2,height/2))
        a.append(random(-height/2, height/2))
        f.append(random(.2, 5))
    
def draw():
    background(0)
    translate(0, height/2)
    for x in range(width):
        for i in range(n):
            ang = x / 30.
            if i % 3 == 0:
                stroke(255, 0, 0)
            elif i % 3 == 1:
                stroke(0, 255, 0)
            else:
                stroke(0, 0, 255)
            line(x, h[i], x, h[i] + sin(ang * f[i]) * a[i])

def keyPressed():
    loop()
