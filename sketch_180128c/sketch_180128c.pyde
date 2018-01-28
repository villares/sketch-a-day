"""
s18028c - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day

Drag the mouse over the canvas to draw
the 'brush' varies with mouse speed.
"""

speed = [0, 0]
LIST = []

def setup():
    size(500, 500)
    colorMode(HSB)

def draw():
    background(100)
    for w, x, y, px, py in LIST:
        c = map(w, 0, 10, 0, 255) # maps 1 to 10 to 0 to 255 scale
        stroke(abs(255 - (c + frameCount) % 511)) # circle colors
        strokeWeight(abs(w))
        line(x, y, px, py)
            
    x, y, px, py = mouseX, mouseY, pmouseX, pmouseY
    speed[0] = (dist(x, y, px, py))**0.5 # squareroot of dist to previous mouse pos
    w = ((10 - speed[0]) + (10 - speed[1]))/2 # mean of 10 minus speed & previous
    if mousePressed:
        LIST.append((w, x, y, px, py))
    speed[1] = speed[0] # updates previous speed

def keyPressed():
    LIST[:] = []