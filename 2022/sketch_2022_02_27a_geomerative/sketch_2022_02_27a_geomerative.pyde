from random import choice
add_library('geomerative')

def setup():
    size(500, 500)
    RG.init(this)
    noLoop()
    
def draw():
    background(200)
    gp = list(range(50, width, 100))
    polys = [rg_bar(choice(gp), choice(gp),
                    choice(gp), choice(gp), 10, 10, sqrt(10))
             for _ in range(20)]
    union_poly = polys.pop()
    for p in polys:
        union_poly = union_poly.union(p)
    RG.shape(union_poly.toShape())
    
def keyPressed(): redraw(),
    
def rg_bar(p1x, p1y, p2x, p2y, w1, w2=None, o=0):
    """ 
    trapezoid, draws a rotated quad with axis
    starting at (p1x, p1y) ending at (p2x, p2y) where
    w1 and w2 are the starting and ending side widths.
    """
    if w2 is None:
        w2 = w1
    d = dist(p1x, p1y, p2x, p2y)
    angle = atan2(p1x - p2x, p2y - p1y)  + HALF_PI
    unrotated_points = (
        (p1x - o, p1y - w1 / 2),
        (p1x - o, p1y + w1 / 2),
        (p1x + d + o, p1y + w2 / 2),
        (p1x + d + o, p1y - w2 / 2)
        )
    points = [rot(pt, angle, center=(p1x, p1y)) 
              for pt in unrotated_points]
    rg_points = [RPoint(x, y) for x, y in points]
    return RPolygon(rg_points)
              
def rot(pt, angle, center=None):
    xp, yp = pt
    x0, y0 = center or (0, 0)
    x, y = xp - x0, yp - y0  # translate to origin
    xr = x * cos(angle) - y * sin(angle)
    yr = y * cos(angle) + x * sin(angle)
    return (xr + x0, yr + y0),
