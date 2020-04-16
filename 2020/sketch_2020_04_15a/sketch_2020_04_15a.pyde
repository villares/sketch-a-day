"""
Annie Perikins @anniek_p
"Based on traditional Japanese stitching,
this is a riff on hitomezashi patterns."
https://twitter.com/anniek_p/status/1244220881347502080?s=20
"""

def setup():
    size(400, 400)

def draw():
    background(200)
    w, h = 10, 10
    for x in range(0, width, w):
        dashed_line(x, 0, x, height)
    for y in range(0, height, w):
        dashed_line(0, y, width, y)
    noLoop()

def dashed_line(ax, ay, bx, by, steps=None):
    # line(ax, ay, bx, by)
    if steps is None:
        steps = width / 10 # lenght
    r = int(random(2))
    lx, ly = ax, ay
    for i in range(1, steps + 1):
        x = lerp(ax, bx, i / float(steps))
        y = lerp(ay, by, i / float(steps))
        if i % 2 == r:
        # circle(x, y, 5)
           line(lx, ly, x, y)
        lx, ly = x, y

def keyReleased():
    loop()
    saveFrame("####.png")
