"""
s18025c - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day

Move the cursor over the image to draw
the 'brush' responds to the speed of the mouse.
"""

pspeed = 0

def setup():
    size(500, 500)
    background(200)

def draw():
    global pspeed
    x, y, px, py = mouseX, mouseY, pmouseX, pmouseY
    speed = (dist(x, y, px, py))**0.5
    w = ((10 - speed) + (10 - pspeed))/2
    strokeWeight(abs(w))
    if mousePressed:
        line(x, y, px, py)
    pspeed = speed

def keyPressed():
    background(200)