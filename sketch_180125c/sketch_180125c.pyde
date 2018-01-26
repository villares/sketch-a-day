"""
s18025c - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day

Drag the mouse over the canvas to draw
'brush' strokeWeight() varies with mouse speed.
"""

pspeed = 0

def setup():
    size(500, 500)
    background(200)

def draw():
    global pspeed
    x, y, px, py = mouseX, mouseY, pmouseX, pmouseY
    # speed is the square root of distance to previous mouse position
    speed = (dist(x, y, px, py))**0.5 
    # w is the mean of 10 minus speed & 10 minus previous speed
    w = ((10 - speed) + (10 - pspeed))/2 
    strokeWeight(abs(w))
    if mousePressed:
        line(x, y, px, py)
    pspeed = speed # updates previous speed

def keyPressed():
    background(200)