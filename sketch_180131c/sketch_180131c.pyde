"""
s180131c - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day

Drag the mouse over the canvas to draw
the 'brush' varies with mouse speed.
"""

LIST, speed = [], [0, 0]
SAVE_FRAME, FRAME_COUNT = False, 0

def setup():
    size(500, 500)
    colorMode(HSB)
    noFill()

def draw():
    global SAVE_FRAME, FRAME_COUNT
    background(50)
    for w, x, y, px, py in LIST:
        c = map(w, 0, 10, 0, 255)  # maps 1 to 10 to 0 to 255 scale
        stroke((c + frameCount) % 255, 255, 255)  # circle colors
        # strokeWeight(abs(w)/2)
        ellipse(x, y, w, w)
    if len(LIST) > 2:
        w, x, y, px, py = LIST[0]
        a, b = PVector(x,y),PVector(LIST[1][1],LIST[1][2]) 
        c = a - b
        del LIST[0]
        LIST.append((w,
                    LIST[-1][1]+c.x,
                    LIST[-1][2]+c.y,
                    LIST[-1][3]+c.x,
                    LIST[-1][4]+c.y))

    x, y, px, py = mouseX, mouseY, pmouseX, pmouseY
    # squareroot of dist to previous mousse pos
    speed[0] = (dist(x, y, px, py)) ** 0.5
    # mean of 10 minus speed & previous
    w = ((10 - speed[0]) + (10 - speed[1])) / 2
    speed[1] = speed[0]  # updates previous speed

    if mousePressed:
        LIST.append((w, x, y, px, py))
        
    if SAVE_FRAME and FRAME_COUNT < 256:
        saveFrame("####.tga")
        FRAME_COUNT += 1
    elif SAVE_FRAME:
        SAVE_FRAME = False
        print "Recording finished."

def keyPressed():
    global SAVE_FRAME, FRAME_COUNT
    if key == ' ':
        LIST[:] = []
    if key == 's' and not SAVE_FRAME:
        SAVE_FRAME, FRAME_COUNT = True, 0
        print "Recording started."