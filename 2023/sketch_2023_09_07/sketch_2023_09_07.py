from itertools import chain

w = 100
n = 6
pad = 5

def setup():
    size(600, 600)
    grid = {}
    for i in range(n):
        for j in range(n):
            grid[(i, j)] = (
                w / 2 + i * w + random(-10, 10),
                w / 2 + j * w + random(-10, 10)
                )
    faces = []
    for i in range(n - 1):
        for j in range(n - 1):
            a, b, c, d = (
                grid[(i, j)],
                grid[(i + 1, j)],
                grid[(i + 1, j + 1)],
                grid[(i, j + 1)]
                )
            faces.append((
                (a[0] + pad, a[1] + pad),
                (b[0] - pad, b[1] + pad),
                (c[0] - pad, c[1] - pad),
                (d[0] + pad, d[1] - pad),
                ))
    with begin_shape(QUADS):
        vertices(list(chain(*faces)))
        