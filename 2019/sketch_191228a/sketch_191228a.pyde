def setup():
    global bg
    size(400, 400)
    background(0)
    colorMode(HSB)
    bg = createGraphics(500, 500)
    bg.beginDraw()
    bg.textSize(140)
    bg.text("Hello", 25, 250)
    bg.endDraw()
    strokeWeight(3)
    step = 8
    i = 0
    for x in range(0, width, step):
        for y in range(0, width, step):
            c = bg.get(x, y)
            if c != 0:
                i = (i + 1) % 256
                stroke(i, 255, 255)
            else:
                stroke(32)
            point(x, y)
