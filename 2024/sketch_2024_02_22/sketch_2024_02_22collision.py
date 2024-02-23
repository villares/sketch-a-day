
area = [200, 200, 300, 200]  
    
def setup():
    size(600, 600)
    
def draw():
    background(200)
    no_fill()
    rect(*area)
    if rect_in_area(mouse_x, mouse_y, 150, 100, *area):
        fill(200, 0, 0)
    else:
        fill(255)
    rect(mouse_x, mouse_y, 150, 100)
    

def rect_in_area(xm, ym, wm, hm, xa, ya, wa, ha):
    return (xa < xm < xa + wa - wm and
            ya < ym < ya + ha - hm)

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
