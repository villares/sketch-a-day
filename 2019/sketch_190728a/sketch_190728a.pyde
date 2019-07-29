"""Grid study"""

def setup():
    size(500, 500)
    colorMode(HSB)
    create_grids()

def create_grids():
    global shapes
    shapes = []    
    for i in range(10):
        d = int(random(7, 14))
        sp = 25
        x = int(random(-7, 8)) * sp
        y = int(random(-7, 8)) * sp
        si = random(15, 35)
        shapes.extend(grid(pos=(x, y),
                           dims=(d, d),
                           space=sp,
                           elem=(create_element, si))
                      )
def draw():
    background(0)
    translate(width / 2., height / 2.)
    
    for s in shapes:
        shape(s)

def grid(pos, dims, space, elem):
    gx, gy = pos
    col_num, row_num = dims
    func, args = elem[0], elem[1:]
    result = []
    half_w = col_num * space / 2.
    half_h = row_num * space / 2.
    for ix in range(col_num):
        x = gx + ix * space + space / 2. - half_w
        for iy in range(row_num):
            y = gy + iy * space + space / 2. - half_h
            noFill()
            stroke(color_rule(ix, iy, row_num))
            strokeWeight(3)
            result.append(func(x, y, *args))
    return result

def color_rule(ix, iy, row_num):
    return color(row_num * 16 - (ix + iy) % 3 * 24 , 200, 200, 100)


def create_element(x, y, *args):
    return createShape(ELLIPSE, x, y, args[0], args[0])

def keyPressed():
    if key == "s":
        saveFrame("####.png")
    if key == " ":
        create_grids()
