"""
s33 180202c - Alexandre B A Villares
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
        #strokeWeight(w)
        ellipse(x, y, w*w, w*w)
        #line(x, y, px, py)
    if len(LIST) > 2 and not mousePressed:
        w0, x0, y0, px0, py0 = LIST[0]
        w1, x1, y1, px1, py1 = LIST[1]
        del LIST[0]
        LIST.append((w0,
                    LIST[-1][1] + x0 - x1, #+v.x,
                    LIST[-1][2] + y0 - y1, #+v.y,
                    LIST[-1][3] + px0 - px1, #+pv.x,
                    LIST[-1][4] + py0 - py1 )) #+pv.y))
    elif mousePressed:
        x, y, px, py = mouseX, mouseY, pmouseX, pmouseY
        # squareroot of dist to previous mousse pos
        speed[0] = (dist(x, y, px, py)) ** 0.5
        # mean of 10 minus speed & previous
        w = ((10 - speed[0]) + (10 - speed[1])) / 2
        speed[1] = speed[0]  # updates previous speed
        LIST.append((w, x, y, px, py))
            
    if SAVE_FRAME and FRAME_COUNT < 500:
        if FRAME_COUNT % 2: saveFrame(str(FRAME_COUNT) + ".tga")
    elif SAVE_FRAME:
        FRAME_COUNT = 0
        SAVE_FRAME = False
        print "Recording finished."
    FRAME_COUNT += 1

def keyPressed():
    global SAVE_FRAME, FRAME_COUNT
    if key == ' ':
        LIST[:] = []
    if key == 's' and not SAVE_FRAME:
        SAVE_FRAME, FRAME_COUNT = True, 0
        print "Recording started."