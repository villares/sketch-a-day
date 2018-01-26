"""
s18026c - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day

Drag the mouse over the canvas to draw
the 'brush' varies with mouse speed.
"""

pspeed = 0

def setup():
    size(500, 500)
    colorMode(HSB)
    background(0)

def draw():
    global pspeed
    x, y, px, py = mouseX, mouseY, pmouseX, pmouseY
    speed = (dist(x, y, px, py))**0.5 # squareroot of dist to previous mouse pos
    w = ((10 - speed) + (10 - pspeed))/2 # mean of 10 minus speed & previous
    stroke(map(w, 0, 10, 0, 255), 255, 255) # maps 1 to 10 to 0 to 255 scale
    strokeWeight(abs(w))
    if mousePressed:
        line(x, y, px, py)
    pspeed = speed # updates previous speed

def keyPressed():
    background(0)