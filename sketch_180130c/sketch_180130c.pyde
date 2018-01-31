
"""
s18030c - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day

Drag the mouse over the canvas to draw
the 'brush' varies with mouse speed.
"""
add_library('peasycam')
LIST, speed = [], [0, 0]
SAVE_FRAME, FRAME_COUNT = False, 0

def setup():
    global cam
    cam = PeasyCam(this, 400)
    cam.setLeftDragHandler(None)      # nenhum Handler para o botão da esquerda
    orbitDH = cam.getRotateDragHandler()  # pega o RotateDragHandler
    cam.setRightDragHandler(orbitDH) # joga para o botão da direita
    size(500, 500, P3D)
    colorMode(HSB)
    noFill()

def draw():
    global SAVE_FRAME, FRAME_COUNT
    background(100)
    for i, (w, x, y, px, py) in enumerate(LIST):
        c = map(w, 0, 10, 0, 255)  # maps 1 to 10 to 0 to 255 scale
        stroke((c + frameCount) % 255, 255, 255)  # circle colors
        # strokeWeight(abs(w)/2)
        with pushMatrix():
            translate(0, 0, (i  - len(LIST))*2)
            ellipse(x - width/2, y - height/2, w ** 2, w ** 2)

    x, y, px, py = mouseX, mouseY, pmouseX , pmouseY
    # squareroot of dist to previous mouse pos
    speed[0] = (dist(x, y, px, py)) ** 0.5
    # mean of 10 minus speed & previous
    w = ((10 - speed[0]) + (10 - speed[1])) / 2
    speed[1] = speed[0]  # updates previous speed

    if mousePressed and mouseButton == LEFT:
        cam.reset()
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