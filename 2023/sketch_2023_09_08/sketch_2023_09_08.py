from itertools import chain

w = 100
n = 6
pad = 5

def setup():
    size(600, 600)
    generate_faces()

def generate_faces():
    global faces
    grid = {}
    face_list = []
    for i in range(n):
        for j in range(n):
            grid[(i, j)] = (
                w / 2 + i * w + random(-10, 10),
                w / 2 + j * w + random(-10, 10)
                )
    for i in range(n - 1):
        for j in range(n - 1):
            a, b, c, d = (
                grid[(i, j)],
                grid[(i + 1, j)],
                grid[(i + 1, j + 1)],
                grid[(i, j + 1)]
                )
            face_list.append((
                (a[0] + pad, a[1] + pad),
                (b[0] - pad, b[1] + pad),
                (c[0] - pad, c[1] - pad),
                (d[0] + pad, d[1] - pad),
                ))
    faces = np.array(face_list)
    
def draw():
    background(150, 150, 250)
    fill(255)
    with begin_shape(QUADS):
        vertices(list(chain(*faces)))
    rect_mode(CORNERS)
    fill(255, 0, 0, 100)
    for f in faces:
        (min_x, min_y), (max_x, max_y) = bounding_box(f)
        rect(min_x, min_y, max_x, max_y)

# def bounding_box(vs):
#     xs = [v.x for v in vs]
#     ys = [v.y for v in vs]
#     return (min(xs), min(ys)), (max(xs), max(ys))
def bounding_box(vs):
#    vs = np.array(vs)
    x_min, y_min = np.min(vs, axis=0)
    x_max, y_max = np.max(vs, axis=0)
    return (x_min, y_min), (x_max, y_max)

def key_pressed():
    generate_faces()