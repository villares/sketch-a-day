"""
s18027c - Alexandre B A Villares
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
    background(0)
    for w, x, y, px, py in LIST:
        c = map(w, 0, 10, 0, 255) # maps 1 to 10 to 0 to 255 scale
        stroke((c + frameCount) % 255, 255, 255) # circle colors
        strokeWeight(abs(w))
        line(x, y, px, py)
            
    x, y, px, py = mouseX, mouseY, pmouseX, pmouseY
    speed[0] = (dist(x, y, px, py))**0.5 # squareroot of dist to previous mouse pos
    w = ((10 - speed[0]) + (10 - speed[1]))/2 # mean of 10 minus speed & previous
    speed[1] = speed[0] # updates previous speed
    if mousePressed:
        LIST.append((w, x, y, px, py))
    # if frameCount < 500 and not frameCount % 5:
    #     saveFrame("###.tga")
    
def keyPressed():
    LIST[:] = []