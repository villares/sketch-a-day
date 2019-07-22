"""Grid study"""

def setup():
    size(500, 500)
    rectMode(CENTER)
    global shapes
    shapes = grid(cols=10,
                  rows=12,
                  space=25,
                  func=(create_element, 10))

def draw():
    translate(width / 2., height / 2.)
    rect(0, 0, 250, 300)
    for s in shapes:
        shape(s)

def grid(cols, rows, space, func):
    result = []
    half_w = cols * space / 2.
    half_h = rows * space / 2.
    for ix in range(cols):
        x = ix * space + space / 2. - half_w
        for iy in range(rows):
            y = iy * space + space / 2. - half_h
            result.append(func[0](x, y, *func[1:]))
    return result

def create_element(x, y, *args):
    return createShape(ELLIPSE, x, y, args[0], args[0])
