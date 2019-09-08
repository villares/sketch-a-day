# estudo para risografia no Sesc 24 de maio
from random import choice

def setup():
    global pts
    size(500, 500)
    num, margin = 5, 25
    w = (width - margin * 2) / num
    pts = []
    for i in range(num):
        x = margin + w / 2 + i * w
        for j in range(num):
            y = margin + w / 2 + j * w 
            pts.append((x, y))
    strokeWeight(5)
    noLoop()

def draw():
    background(255)
    for i in range(10):
        (x0, y0), (x1, y1) = choice(pts), choice(pts)
        noStroke()
        fill(200, 0, 0) # red
        circle(x0, y0, 50)  
        stroke(0, 0, 200) # bluse  
        line(x0, y0, x1, y1)
        circle(x0, y0, 5)            
        circle(x1, y1, 5)            

def keyPressed():
    saveFrame("###.png")
    redraw()
