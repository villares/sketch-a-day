
pts = [(100, 100), (500, 150), (500, 400), (200, 500)]

def setup():
    size(600, 600)
    no_fill()
    
def draw():
    background(200)
    poly = pts + [(mouse_x, mouse_y)]
    draw_poly(poly)
    for _ in range(10):
        poly = offset(poly, -10)
        draw_poly(poly)
    
def draw_poly(poly):
    with begin_closed_shape():
        vertices(poly)

def offset(poly, off_d):
    result = []
    for (xa, ya), (xb, yb) in zip(poly, poly[1:] + [poly[0]]):
        ang = atan2(ya - yb, xa - xb) + HALF_PI
        off_d = -20
        off_x = off_d * cos(ang)
        off_y = off_d * sin(ang)
        result.append((xa + off_x, ya + off_y))
    return result


                    
                    