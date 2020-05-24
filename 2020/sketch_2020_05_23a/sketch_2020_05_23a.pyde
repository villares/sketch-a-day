from __future__ import division

def setup():
    size(400, 400) 
    rectMode(CENTER)
    strokeWeight(3)
    noStroke()
    
def draw():
    background(240)
    xa, ya = 100, 100
    xb, yb = 300, 300
    ca = color(200, 0, 0, 100)
    cb = color(0, 0, 200, 100)
    sa = map(mouseY, 0, height, 10, 200)
    sb = 210 - sa
    n = 1+ int(mouseX / 10)
    for t in range(n + 1):
        xc = lerp(xa, xb, t / n)
        yc = lerp(ya, yb, t / n)
        cc = lerpColor(ca, cb, t / n)
        sc = lerp(sa, sb, t / n)
        fill(cc)    
        rect(xc, yc, sc, sc)
        
    
