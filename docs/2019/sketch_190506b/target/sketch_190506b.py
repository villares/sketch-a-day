from pytop5js import *

"""
 * 3D Knot (2017/Dec)
 * Daniel Shiffman
 * https://YouTu.be/r6YMKr1X0VA
 *
 * Mod GoToLoop (v1.0.3) (2018/Oct/16)
 * https://OpenProcessing.org/sketch/608725 (pjs)
 * https://OpenProcessing.org/sketch/608726 (p5js)
 *
 * https://Discourse.Processing.org/t/
 * vertex-loop-and-draw-along-a-vertex-path/4545/4
"""

"""
 * http://PaulBourke.net/geometry/knots/
 * Knot 4 (1992/Oct):
 *
 * r(beta) = 0.8 + 1.6 * sin(6 * beta)
 * theta(beta) = 2 * beta
 * phi(beta) = 0.6 * pi * sin(12 * beta)
 *
 * x = r * cos(phi) * cos(theta)
 * y = r * cos(phi) * sin(theta)
 * z = r * sin(phi)
"""

ANGLE_STEP, BETA_STEP = .02, .01
MAG, SEGS_LIMIT = 100.0, PI + BETA_STEP
PI_DOT_6 = PI * .6

angle = beta = 0.0
paused = False

knots = []

def setup():
    createCanvas(600, 600, 'webgl')
    smooth(8)
    colorMode('hsb')
    noFill()
    strokeWeight(8.0)


def draw():
    global angle, beta

    background(0)
    rect(20,20, 20,20)
    translate(width>>1, height>>1)
    rotateY(angle)
    angle += ANGLE_STEP

    if beta <= SEGS_LIMIT:
     addKnot()
    beta += BETA_STEP

    beginShape()
    for k in knots:
            #stroke(frameCount % 100, 255, 255)
            stroke(k.c)
            vertex(k.v[0], k.v[1], k.v[2])
    endShape()

def mousePressed():
    global paused
    paused = not paused
    noLoop() if paused else loop()

# def keyPressed(): mousePressed()

def addKnot():
    r = MAG * (.8 + 1.6 * sin(6 * beta))
    theta = 2 * beta
    phi = PI_DOT_6 * sin(12 * beta)
    rCosPhi = r * cos(phi)

    x = rCosPhi * cos(theta)
    y = rCosPhi * sin(theta)
    z = r * sin(phi)

    knot = Knot(x, y, z)
    knots.append(knot)
    # quebrado:
    #print('%d: %s' % (len(knots), knot))


class Knot:
    def __init__(self, *vec):
        self.v = vec[0] if len(vec) else tuple(*vec)
        x, y, z = self.v
        mag = sqrt(x*x + y*y + z*z)
        self.c = color(mag, 255, 255)
        
    def __str__(self):
        return 'Vec: %s   \tHSB: %d' % (self.v, self.c)

# This is required by pyp5js to work
start_p5(setup, draw)
