# From @solub https://discourse.processing.org/t/shape-from-stroke/14893/7
# Based on @MBo's solution suggested here ->
# https://stackoverflow.com/questions/54033808/how-to-offset-polygon-edges


ITER = 5  # up to 7 max
SW = 25.0
to_move = None


def setup():
    size(1000, 600, P2D)
    smooth(8)
    no_fill()
    stroke_weight(2)

    global cntrl_pts, pts

    cntrl_pts = [
        Py5Vector(100, 100),
        Py5Vector(450, 150), Py5Vector(610, 200),
        Py5Vector(850, 280), Py5Vector(500, 400),
        Py5Vector(540, 480), Py5Vector(260, 500)]
    pts = cntrl_pts
    subdivide()


def draw():
    background('#FFFFFF')

    # Draw lines between control points
    push_style()
    stroke_weight(1)
    stroke(40, 40, 255)
    for i, p in enumerate(cntrl_pts):
        line(p.x, p.y, cntrl_pts[(i+1) %
                                len(cntrl_pts)].x, cntrl_pts[(i+1) %
                                                           len(cntrl_pts)].y)
    pop_style()

    # Draw control points
    push_style()
    stroke(255, 30, 90)
    stroke_weight(10)
    for p in cntrl_pts:
        point(p.x, p.y)
    pop_style()

    # Draw Catmull-Clark subdivided polyline (spline)
    for i in range(len(pts)):
        p1 = pts[i]
        p2 = pts[(i+1) % len(pts)]
        line(p1.x, p1.y, p2.x, p2.y)

    # Draw P_shape from quads
    push_style()
    stroke_weight(.7)
    fill(95, 250, 90, 60)
    begin_shape(QUAD_STRIP)
    for i in range(len(pts)+1):
        p1 = pts[i-1]  # last point
        pm = pts[i % len(pts)]  # midpoint
        p2 = pts[(i+1) % len(pts)]  # next point
        theta = atan2(p2.y - p1.y, p2.x - p1.x) + HALF_PI

        px = (SW*.5) * cos(theta)
        py = (SW*.5) * sin(theta)

        vertex(pm.x - px, pm.y - py)  # vertices for the outer edge of path
        vertex(pm.x + px, pm.y + py)  # vertices for the inner edge of path
    end_shape()
    pop_style()


def mouse_pressed():
    global to_move
    for p in cntrl_pts:
        if dist(p.x, p.y, mouse_x, mouse_y) < 12:
            to_move = p
            break
        
def mouse_dragged():
    if to_move:
        to_move.xy = mouse_x, mouse_y

def mouse_released():
    global to_move
    do = False
    for p in cntrl_pts:
        if dist(p.x, p.y, mouse_x, mouse_y) < 12:
            do = True
            break
    if do:
        to_move = None
        subdivide()


def subdivide():

    global pts
    pts = cntrl_pts

    # Catmull-Clark subdivision
    for j in range(ITER):
        newpts = []
        for i in range(len(pts)):
            p1 = pts[i]
            p2 = pts[(i+1) % len(pts)]
            p3 = pts[(i+2) % len(pts)]
            qp = p1 * .5 + p2 * .5
            # (Catmull-Clark subdivision = degree 3)
            rp = p1 * .125 + p2 * .75 + p3 * .125
            newpts.append(qp)
            newpts.append(rp)

        pts = newpts
