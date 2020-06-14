# inspired by https://twitter.com/beesandbombs/status/1247567578802855938?s=20
#
# add_library('GifAnimation')
# from gif_animation_helper import gif_export

s_size = 50
COLORS = [color(255, 255, 0),
          color(255, 0, 0),
          color(0, 0, 255),
          ]

def setup():
    size(400, 400)
    blendMode(ADD)  # DIFFERENCE # EXCLUSION
    rectMode(CENTER)
    init()

def init():
    from itertools import product
    global origin, target, current
    origin = []
    target = []
    # grid = ((-1, -1), (-1, 0), (0, 0), (0, -1))
    grid = product(range(-2, 2), repeat=2)

    for p in grid:
        h_size = s_size / 2
        off_x, off_y = h_size + p[0] * s_size, h_size + p[1] * s_size
        for _ in COLORS:
            origin.append((width / 2. + off_x,
                           height / 2. + off_y,
                           0,
                           s_size))
            target.append((random(s_size, width - s_size),
                           random(s_size, height - s_size),
                           random(-HALF_PI, HALF_PI),
                           random(s_size, s_size * 1.5)))
    current = origin[:]

def draw():
    background(0)
    noFill()
    strokeWeight(5)
    t = .5 - cos(radians(frameCount % 360)) / 2.  # map(mouseX, 0, width, 0, 1)
    for i, origin_i in enumerate(origin):
        stroke(COLORS[i % len(COLORS)])
        x, y, r, s = lerp_sequence(origin_i, target[i], t)
        pushMatrix()
        translate(x, y)
        rotate(r)
        circle(0, 0, s)
        popMatrix()

    # if frameCount < 360:
    #     if frameCount % 2:
    #        gif_export(GifMaker, "animation")
    # else:
    #     gif_export(GifMaker, "animation", finish=True)
    #
    # if frameCount % 360 == 0:
    #     init()

def lerp_sequence(a, b, t):
    c = []
    for c_a, c_b in zip(a, b):
        c.append(lerp(c_a, c_b, t))
    return c

def keyPressed():
    init()
