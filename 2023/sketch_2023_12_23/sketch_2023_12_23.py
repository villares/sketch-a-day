
import py5
from py5 import sin

step = 10
AMP = 20


def setup():
    py5.size(900, 900, py5.P2D)
    
def draw():
    py5.background(0)
    py5.stroke(255)
    for y in range(step * 2, 900 - step, step):
        wave(0, y, py5.width, y, [10 + 10 * sin(x / 31) for x in range(0, py5.width, step)])
        
def key_pressed():
    py5.save(__file__[:-2] + 'png')

def wave(x1, y1, x2, y2, samples, s=AMP):
    """
    dois pares (x, y), largura, número de ondas
    """
    L = py5.dist(x1, y1, x2, y2)
    n = len(samples)
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
                s = samples[i-1]
                point_L.append((0, i * dy, 0))
                if i % 2:
                    point_L.append((-s, i * dy + dy / 2.0, s))
                    point_L.append((0, i * dy + dy, s))
                else:
                    point_L.append((s, i * dy + dy / 2.0, s))
                    point_L.append((0, i * dy + dy, s))
            point_L.append((0, L, 0))
            for p1, p2 in zip(
                          point_L[1:-1],
                          point_L[2:],
                          ):
                p1x, p1y, s = p1
                p2x, p2y, _ = p2
                m12x, m12y = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
                if p2 == (0, L):
                    py5.quadratic_vertex(p1x, p1y, p2x, p2y)
                else:
                    py5.quadratic_vertex(p1x, p1y, m12x, m12y)

py5.run_sketch()