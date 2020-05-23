from __future__ import division

def setup():
    size(400, 400) 
    strokeWeight(3)
    noFill()
    
def draw():
    background(240)
    xa, ya = 100, 100
    xb, yb = 300, 300
    ca = color(200, 0, 0)
    cb = color(0, 0, 200)
    n = 1+ int(mouseX / 10)
    for t in range(n + 1):
        xc = lerp(xa, xb, t / n)
        yc = lerp(ya, yb, t / n)
        cc = lerpColor(ca, cb, t / n)
        stroke(cc)    
        ellipse(xc, yc, 200, 200)
        
    
