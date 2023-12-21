def setup():
    size(600, 600)
    smooth(4)
    
def draw():
    background(0)
    stroke(255)
    stroke_weight(1)
    for x in range(-300, 900, 10):
        wave(x, 0, x, 600, 5 + x / 5, n=8)
        wave(0, x,  600, x, 5 + x / 5, n=8)
        line(x, 0, x, height)
#     stroke(200, 0, 0)
#     wave(100, 100, 500, 500, mouse_x, 8)
#     stroke(0, 0, 200)
#     wave(500, 500, 100, 100, mouse_x, 8)

def key_pressed():
    save('out.png')

def wave(x1, y1, x2, y2, s=None, n=2):
    """
    dois pares (x, y), largura, número de ondas
    """
    L = dist(x1, y1, x2, y2)
    if not s:
        s = 0
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
            for p1, p2 in zip(
                          point_L[1:-1],
                          point_L[2:]
                          ):
                m12 = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
                if p2 == (0, L):
                    quadratic_vertex(*p1, *p2)
                else:
                    quadratic_vertex(*p1, *m12)

