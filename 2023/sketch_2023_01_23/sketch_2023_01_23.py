from villares.arcs import arc_corner

def setup():
    size(600, 600, P2D)
    smooth(8)
    background(240)
    for x in range(-600, 600, 4):
        stroke(0, 255, 0)
        wave(x,  - x, x + 600, 600 - x, 1 +abs(x /10), n=8)
        stroke(0, 0, 255)
        wave(x + 600,  x, x, 600 + x, 1 + abs(x / 5), n=8)
        stroke(0)
        line(x, 0, x, height)
        
    save('out.png')

def wave(x1, y1, x2, y2, s=None, n=2, r=19):
    """
    dois pares (x, y), largura, número de ondas
    """
    L = dist(x1, y1, x2, y2)
    if not s:
        s = int(max(L / 5, 10))
    no_fill()
    with push_matrix():
        translate(x1, y1)
        angle = atan2(x1 - x2, y2 - y1)
        rotate(angle)
        offset = 0
        dy = L / (n + 2.)
        point_L = []
        point_L.append((0, 0))
        with begin_shape():
            vertex(0, 0)
            for i in range(1, n + 1):
                point_L.append((0, i * dy))
                if i % 2:
                    point_L.append((-s, i * dy + dy / 2.))
                    point_L.append((0, i * dy + dy))
                else:
                    point_L.append((s, i * dy + dy / 2.))
                    point_L.append((0, i * dy + dy))
            point_L.append((0, L))
            for p0, p1, p2 in zip(point_L[:-2],
                                  point_L[1:-1],
                                  point_L[2:]
                                  ):
                m01 = (p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2
                m12 = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
                arc_corner(p1, m12, m01, r)
            vertex(0, L)
