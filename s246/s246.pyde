curvas = []
n = 3

def setup():
    size(1024, 300)
    noStroke()
    blendMode(MULTIPLY)
    
def keyPressed():
    if key == "s":
        saveFrame("###.png")
    else: 
        curvas[:] = []
        for i in range(n):
            curvas.append((random(-height/6,height/6),
                  random(-height/6, height/6),
                  random(.33, 3),
                  random(.33, 3),
                  random(.33, 3),
                 ))

def draw():
    background(200)
    translate(0, height/2)
    for i, (h, a, f1, f2, f3) in enumerate(curvas):
        if i % 3 == 0:
            fill(0, 255, 0)
        elif i % 3 == 1:
            fill(255, 0, 0)
        else:
            fill(0, 0, 255)
        beginShape()
        for x in range(width):
            ang = x/30.
            s = sin(ang * f1) + sin(ang * f2) + sin(ang * f3) 
            vertex(x, h+ s * a)
        for xx in range(width):
            x = width-xx
            ang = x/30.
            s = sin(ang * f1)*1.1 + sin(ang * f2)*1.2 + sin(ang * f3)*1.3
            vertex(x, 10 + h + s * a)
        endShape(CLOSE)
        
