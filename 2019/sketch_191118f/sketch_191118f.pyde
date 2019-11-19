# port of aBe Hamoid's work!
# https://discourse.processing.org/t/program-to-test-hint-with-transparency/4361
# plus a few hints from https://processing.org/reference/hint_.html

b = [False] * 5 # list of booleans to toggle hints

def setup():
    size(800, 600, P3D)
    hint(DISABLE_DEPTH_TEST)
    hint(DISABLE_DEPTH_SORT)
    hint(DISABLE_DEPTH_MASK)
    hint(DISABLE_OPTIMIZED_STROKE)
    hint(DISABLE_STROKE_PERSPECTIVE)
    
def draw():
    background(255)

    fill(0)
    text("DEPTH_TEST " + str(b[0]), 20, 20)
    text("DEPTH_SORT " + str(b[1]), 20, 40)
    text("DEPTH_MASK " + str(b[2]), 20, 60)
    text("OPTIMIZED_STROKE " + str(b[3]), 20, 80)
    text("STROKE_PERSPECTIVE " + str(b[4]), 20, 100)
    text("<- use the mouse to toggle settings", 200, 40)

    fill(255, 40, 20, 100)
    translate(width / 2, height / 2)
    rotateY(frameCount * 0.005)

    for x in range(-200, 201, 200):
        for y in range(-200, 201, 200):
            pushMatrix()
            translate(x, 0, y)
            box(180)
            popMatrix()

def mousePressed():
    id = mouseY / 20
    if id < len(b):
        b[id] = not b[id]

    hint(ENABLE_DEPTH_TEST if b[0] else DISABLE_DEPTH_TEST)
    hint(ENABLE_DEPTH_SORT if b[1] else DISABLE_DEPTH_SORT)
    hint(ENABLE_DEPTH_MASK if b[2] else DISABLE_DEPTH_MASK)
    hint(ENABLE_OPTIMIZED_STROKE if b[3] else DISABLE_OPTIMIZED_STROKE)
    hint(ENABLE_STROKE_PERSPECTIVE if b[4] else DISABLE_STROKE_PERSPECTIVE)
