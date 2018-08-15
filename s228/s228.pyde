add_library('peasycam')


def setup():
    size(500, 500, P3D)
    # optional PeasyCam setup to allow orbiting with a mouse drag
    cam = PeasyCam(this, 100)
    cam.setMinimumDistance(1000)
    cam.setMaximumDistance(1000)

def draw():
    background(100)
    my_box(100)

def my_box(s):
    f1 = ((-1, +1, -1),
          (-1, +1, +1),
          (+1, +1, +1),
          (+1, +1, -1),
          )
    face(f1, s)
    f2 = ((-1, -1, -1),
          (-1, -1, +1),
          (+1, -1, +1),
          (+1, -1, -1),
          )
    face(f2, s)

def face(vs, s):
    beginShape()
    for pt in vs:
        x, y, z = pt
        vertex(x * s, y * s, z * s)
    endShape(CLOSE)
