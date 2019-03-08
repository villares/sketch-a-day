# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
# s229 20180815
add_library('peasycam')


def setup():
    size(500, 500, P3D)
    # optional PeasyCam setup to allow orbiting with a mouse drag
    cam = PeasyCam(this, 100)
    cam.setMinimumDistance(500)
    cam.setMaximumDistance(1000)

def draw():
    background(100)
    my_box(200)

def my_box(side):
    front = ((-1, +1, -1),
             (-1, +1, +1),
             (+1, +1, +1),
             (+1, +1, -1),
             )
    back = ((-1, -1, -1),
            (-1, -1, +1),
            (+1, -1, +1),
            (+1, -1, -1),
            )
    left = ((-1, -1, -1),
            (-1, -1, +1),
            (-1, +1, +1),
            (-1, +1, -1),
            )
    right = ((+1, -1, -1),
             (+1, -1, +1),
             (+1, +1, +1),
             (+1, +1, -1),
             )
    down = ((-1, -1, -1),
            (+1, -1, -1),
            (+1, +1, -1),
            (-1, +1, -1),
            )
    top = ((-1, -1, +1),
           (+1, -1, +1),
           (+1, +1, +1),
           (-1, +1, +1),
           )

    faces = ((top, color(255, 0, 0)),
             (down, color(0, 255, 0)),
             (right, color(0, 0, 255)),
             (left, color(255, 255, 0)),
             (back, color(255, 0, 255)),
             (front, color(0, 255, 255)),
             )

    for pts, shade in faces:
        hs = side / 2  # half side
        fill(shade)
        beginShape()
        for pt in pts:
            x, y, z = pt
            vertex(x * hs, y * hs, z * hs)
        endShape(CLOSE)
