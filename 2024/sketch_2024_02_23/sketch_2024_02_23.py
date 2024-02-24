
area = (200, 250, 300, 200)  
    
def setup():
    size(600, 600)
    
def draw():
    mouse_rect = (mouse_x, mouse_y, 150, 100)
    background(200)
    stroke_weight(3)

    if rect_on_rect(*mouse_rect, *area):
        stroke(255, 0, 0)
    else:
        stroke(0)
    no_fill()
    rect(*area)

    if rect_in_area(*mouse_rect, *area):
        fill(255, 0, 0, 100)
    else:
        fill(0, 100)
    stroke(0)
    rect(mouse_x, mouse_y, 150, 100)

    if point_on_rect(150, 200, *mouse_rect):
        stroke(255, 0, 0)
    else:
        stroke(0)
    stroke_weight(6)
    point(150, 200)
    
def point_on_rect(xa, ya, xb, yb, wb, hb):
    return (xb <= xa <= xb + wb and yb <= ya <= yb + hb)
    
def rect_in_area(xa, ya, wa, ha, xb, yb, wb, hb):
    return (xb < xa < xb + wb - wa and
            yb < ya < yb + hb - ha)
    
def rect_on_rect(rxa, rya, raw, rah, rxb, ryb, rbw, rbh):
    return (rxa + raw >= rxb and rxa <= rxb + rbw and          # ra left edge past rb right
            rya + rah >= ryb and rya <= ryb + rbh) 

def point_inside_poly(*args):
    # rya-casting algorithm based on
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
