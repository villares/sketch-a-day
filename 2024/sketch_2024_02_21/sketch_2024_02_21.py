
pt = [200, 300]
    
    
def setup():
    size(600, 600)
    
def draw():
    background(200)
    pts = rect_points(300, 300, 400, 100,
                      angle=radians(frame_count))
    if point_inside_poly(pt, pts):
        fill(255, 0, 0)
    else:
        no_fill()
    stroke(0)
    stroke_weight(3)

    with begin_closed_shape():
        vertices(pts)
    stroke(0, 0, 200)
    stroke_weight(10)
    point(*pt)
     

def rect_points(ox, oy, w, h, mode='CENTER', angle=None):
    if mode == 'CENTER':
        x, y = ox - w / 2.0, oy - h / 2.0
    else:
        x, y = ox, oy
    vs = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
    if angle is None:
        return vs
    else:
        return [rotate_point((x, y), angle, (ox, oy))
                for x, y in vs]

def rotate_point(*args):
    """
    point (tuple/PVector), angle
    x, y, angle (around 0, 0)
    point (tuple/PVector), angle, center (tuple/PVector)
    x, y, angle, x_center, y_center
    """
    if len(args) == 2:
        (xp, yp), angle = args
        x0, y0 = 0, 0
    elif len(args) == 3:
        try:
            (xp, yp), angle, (x0, y0) = args
        except TypeError:
            xp, yp, angle = args
            x0, y0 = 0, 0
    elif len(args) == 5:
        xp, yp, angle, x0, y0 = args
    x, y = xp - x0, yp - y0  # translate to origin
    xr = x * cos(angle) - y * sin(angle)
    yr = y * cos(angle) + x * sin(angle)
    return (xr + x0, yr + y0)

def point_inside_poly(*args):
    # ray-casting algorithm based on
    # https://wrf.ecse.rpi.edu/Research/Short_Notes/pnpoly.html
    if len(args) == 2:
        (x, y), poly = args
    else:
        x, y, poly = args
    inside = False
    for i, p in enumerate(poly):
        pp = poly[i - 1]
        xi, yi = p
        xj, yj = pp
        intersect = ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi)
        if intersect:
            inside = not inside
    return inside
