# From @solub https://discourse.processing.org/t/shape-from-stroke/14893/7
# Based on @MBo's solution suggested here ->
# https://stackoverflow.com/questions/54033808/how-to-offset-polygon-edges

SW = -50.0  # Stroke width of path/PShape (-/+ for inner/outer offset)

def setup():
    size(1000, 600)
    smooth(8)

def draw():
    background(0, 100, 0)
    fill(230)

    # List of vertices (polygon)
    pts = [
        Py5Vector(mouse_x, mouse_y),
        Py5Vector(450, 150), Py5Vector(610, 200),
        Py5Vector(850, 280), Py5Vector(500, 400),
        Py5Vector(540, 480), Py5Vector(260, 500)]

    begin_shape(QUAD_STRIP)
    for i in range(len(pts)+1):
        pp = pts[(i-1) % len(pts)]  # previous vertex
        pc = pts[i % len(pts)]  # current vertex
        pn = pts[(i+1) % len(pts)]  # next vertex

        theta_a = atan2(pc.y - pp.y, pc.x - pp.x) + \
            HALF_PI  # right angle with the edge pp-pc
        theta_b = atan2(pn.y - pc.y, pn.x - pc.x) + \
            HALF_PI  # right angle with the edge pc-pn

        # vector pointing perpendicularly to edge pp-pc
        a = Py5Vector(cos(theta_a), sin(theta_a))
        # vector pointing perpendicularly to edge pc-pn
        b = Py5Vector(cos(theta_b), sin(theta_b))

        nsum = (a + b).normalize()  # normalized sum

        l = SW / sqrt(1 + Py5Vector.dot(a, b))  # desired length
        po = pc + (l * nsum)  # offsetted vertex

        vertex(pc.x, pc.y)
        vertex(po.x, po.y)
    end_shape(CLOSE)
