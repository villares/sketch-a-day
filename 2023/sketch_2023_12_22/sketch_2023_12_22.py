import py5

sw = 3
step = 20

def setup():
    py5.size(900, 900)
    py5.blend_mode(py5.ADD)
    py5.stroke_weight(sw)
    
def draw():
    py5.background(0)
    w, hw = py5.width, py5.width // 2
    for x in range(-hw, w + hw , step):
        py5.stroke(0, 0, 250)
        wave(x, 0, x, w, sw + x / sw, n=5)
        py5.stroke(0, 250, 0)
        wave(0, x,  w, x, sw + x / sw, n=5)
        py5.stroke(250, 0, 0)
        py5.line(0, x, w, x)

def key_pressed():
    py5.save(__file__[:-2] + 'png')

def wave(x1, y1, x2, y2, s=None, n=2):
    """
    dois pares (x, y), largura, número de ondas
    """
    L = py5.dist(x1, y1, x2, y2)
    if not s:
        s = 0
    py5.no_fill()
    with py5.push_matrix():
        py5.translate(x1, y1)
        angle = py5.atan2(x1 - x2, y2 - y1)
        py5.rotate(angle)
        offset = 0
        dy = L / (n + 2)
        point_L = []
        point_L.append((0, 0))
        with py5.begin_shape():
            py5.vertex(0, 0)
            for i in range(1, n + 1):
                point_L.append((0, i * dy))
                if i % 2:
                    point_L.append((-s, i * dy + dy / 2))
                    point_L.append((0, i * dy + dy))
                else:
                    point_L.append((s, i * dy + dy / 2))
                    point_L.append((0, i * dy + dy))
            point_L.append((0, L))
            for p1, p2 in zip(
                          point_L[1:-1],
                          point_L[2:]
                          ):
                m12 = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
                if p2 == (0, L):
                    py5.quadratic_vertex(*p1, *p2)
                else:
                    py5.quadratic_vertex(*p1, *m12)

py5.run_sketch()