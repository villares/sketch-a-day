"""Grid study"""

from random import choice

def setup():
    size(500, 500)
    rectMode(CENTER)
    colorMode(HSB)
    strokeJoin(ROUND)
    strokeWeight(2)
    create_grids()

def create_grids():
    global shapes
    shapes = []    
    for i in range(10):
        d = int(random(4, 11))
        sp = 20
        x = int(random(-7, 8)) * sp
        y = int(random(-7, 8)) * sp
        si = random(15, 35)
        sh = choice((ELLIPSE, ELLIPSE, RECT, RECT, TRIANGLE, TRIANGLES))
        shapes.extend(grid(pos=(x, y),
                           dims=(d, d),
                           space=sp,
                           elem=(create_element, sh, si))
                      )
def draw():
    background(240)
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
            result.append(func(x, y, *args))
    return result

def color_rule(ix, iy, row_num):
    return color(row_num * 24 - (ix + iy) % 3 * 32 , 255, 100)


def create_element(x, y, *args):
    sh = args[0] # shape
    si = args[1] # size
    if args[0] in (RECT, ELLIPSE):
        return createShape(sh, x, y, si, si)
    elif sh == TRIANGLE:
        return createShape(TRIANGLE, x, y, x + si, y, x, y + si)
    elif sh == TRIANGLES:
        return createShape(TRIANGLE, x, y, x - si, y, x, y - si)

def keyPressed():
    if key == "s":
        saveFrame("####.png")
    if key == " ":
        create_grids()
