def setup():
    size(500, 500)
    rectMode(CENTER)
    translate(width / 2, height / 2)
    # grid(10, 10, 45, elem_1234)
    grid(10, 10, 45, elem_1234, rule_1234)

def grid(cols, rows, spacing, element, rule=lambda *args: None):
    wid, hei = cols * spacing, rows * spacing
    for i in range(cols):
        x = spacing / 2. + i * spacing - wid / 2.
        for j in range(rows):
            y = spacing / 2. + j * spacing - hei / 2.
            element(x, y, rule(i, j, cols, rows, spacing))

def rule_1234(i, j, cols, rows, spacing):
    """ border and chess """
    w, h = cols - 1, rows - 1
    if i == 0 or i == w or j == 0 or j == h:
        c = color(255)
    else:
        c = color(0)
    if (i + j) % 3 == 0:
        rot = 0
    else:
        rot = QUARTER_PI
    siz = spacing / (1.02 + (i + j) % 2)
    return c, rot, siz

def elem_1234(x, y, args):
    if args != None:
        c, rot, siz = args
    else:
        c, rot, siz = 0, 0, 40
    noStroke()
    fill(c)
    pushMatrix()
    translate(x, y)
    rotate(rot)
    rect(0, 0, siz, siz)
    popMatrix()
