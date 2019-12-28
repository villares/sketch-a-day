def setup():
    global bg
    size(500, 500)
    bg = createGraphics(500, 500)
    bg.beginDraw()
    bg.textSize(140)
    bg.text("Hello", 50, 250)
    bg.endDraw()
    strokeWeight(3)
    step = 8
    for x in range(0, width, step):
       for y in range(0, width, step):
           c = bg.get(x, y)
           stroke(c)
           point(x, y)
