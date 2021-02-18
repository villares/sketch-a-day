from random import choice

colors = (color(250, 50, 0),
          color(150, 0, 0),
          color(240),
          # color(250, 0, 0),
          # color(0, 150, 0),
          # color(50, 50, 250),
          # color(0, 50, 150),
          # color(150, 50, 250),
          # color(50, 150, 250)
          )

def setup():
    global fs, ft
    size(750, 750)
    noLoop()
    rectMode(CENTER)
    textAlign(CENTER, CENTER)
    # fs = createFont("Source Sans Pro Bold",60)
    fs = createFont("Tomorrow Bold",60)


def draw():
    background(0)
    translate(width / 2, height / 2)
    grade(0, 0, 10, 750.)
    fill(choice((color(150, 0, 0), color(0, 0, 150))))
    rotate(-QUARTER_PI)
    textFont(fs)
    # text("RECOMENDO!", 0, 0)
    

def grade(xo, yo, n, tw, e=None):
    cw = tw / n
    offset = (cw - tw) / 2.
    for i in range(n):
        x = xo + offset + cw * i
        for j in range(n):
            y = yo + offset + cw * j
            o = (i + j) % 4
            if cw > 10 and random(10) < 5:
                grade(x, y, 2, cw)
            else:
               element(x, y, cw, o)
 

def element(x, y, w, option):
    fill(0)
    if option == 0:
        textFont(fs)
        t = choice((':;.,!'))
        fill(choice(colors))
        textSize(w * 2 )
        text(t, x, y)
    else:
        textFont(fs)
        t = choice((u'“”»«'))
        fill(choice(colors))
        textSize(w * 2)
        text(t, x, y)


def keyPressed():
    if key == 's':
        saveFrame("####.png")
    redraw()
