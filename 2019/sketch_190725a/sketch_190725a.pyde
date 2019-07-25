"""Grid study"""

def setup():
    size(500, 500)
    colorMode(HSB)
    create_grids()

def create_grids():
    global shapes
    shapes = []    
    for i in range(10):
        d = int(random(5, 10))
        sp = int(random(3, 8)) * 5
        x = int(random(-8, 9)) * sp
        y = int(random(-8, 9)) * sp
        si = random(15, 35)
        shapes.extend(grid(pos=(x, y),
                           dims=(d, d),
                           space=sp,
                           elem=(create_element, si))
                      )
def draw():
    background(100)
    translate(width / 2., height / 2.)
    
    for s in shapes:
        shape(s)

def grid(pos, dims, space, elem):
    gx, gy = pos
    col, row = dims
    func, args = elem[0], elem[1:]
    result = []
    half_w = col * space / 2.
    half_h = row * space / 2.
    fill(row * 16, 200, 200, 100)
    for ix in range(col):
        x = gx + ix * space + space / 2. - half_w
        for iy in range(row):
            y = gy + iy * space + space / 2. - half_h
            result.append(func(x, y, *args))
    return result

def create_element(x, y, *args):
    noStroke()
    # fill(255, 100)
    return createShape(ELLIPSE, x, y, args[0], args[0])

def keyPressed():
    if key == "s":
        saveFrame("####.png")
    if key == " ":
        create_grids()
