from villares.line_geometry import draw_poly, hatch_poly
from villares.helpers import point_in_screen

def setup():
    size(400, 400)

def draw():
    background(50, 100, 50)
    translate(width / 2, height / 2)
    ax, ay = mouseX - width / 2, mouseY - height / 2
    if point_in_screen(ax - 10, ay - 10):
        fill(200)
        background(255)
    else:
        background(0) 
        fill(255)

    rpts = rect_points(0, 0, 300, 200, mode=CENTER, angle=QUARTER_PI)
    draw_poly(rpts)
    print rotate_point(10, 10, 4)
    print rotate_point((10, 10), 4, (0, 0))
    
    hatch_poly(rpts, QUARTER_PI / 2)
    
    # rotate(QUARTER_PI)
    # rpts = rect_points(0, 0, 300, 200, mode=CENTER)
    # draw_poly(rpts)
    # hatch_poly(rpts, QUARTER_PI / 2)
    

def rect_points(x0, y0, w, h, mode=CORNER, angle=None):
    if mode == CENTER:
        x, y = x0 - w / 2.0, y0 - h / 2.0
    else:
        x, y = x0, y0
    if angle is None:
        return [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
    else:
        return [rotate_point(rx, ry, angle, x0, y0) for rx, ry in
                ((x, y), (x + w, y), (x + w, y + h), (x, y + h))]

def rotate_point(*args):
    if len(args) == 2:
        (xp, yp), angle = args
        x0, y0 = 0, 0
    if len(args) == 3:
        try:
            (xp, yp), angle, (x0, y0) = args
        except TypeError:
            xp, yp, angle = args
            x0, y0 = 0, 0
    if len(args) == 5:
        xp, yp, angle, x0, y0 = args
    x, y = xp - x0, yp - y0  # translate to origin
    xr = x * cos(angle) - y * sin(angle)
    yr = y * cos(angle) + x * sin(angle)
    return (xr + x0, yr + y0)
