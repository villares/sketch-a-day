"""
Koch Curve
https://www.rosettacode.org/wiki/Koch_curve#Processing
Processing 3.4
2020-02-26 Noel
2020-03-03 Jeremy Douglass
2020-03-12 Alexandre Villares (Python Mode)
Task: Draw a Koch curve. See details: https:#en.wikipedia.org/wiki/Koch_snowflake
"""

l = 300

def setup():
    size(400, 400)
    background(0, 0, 255)
    stroke(255)
    # draw from center of screen
    translate(width / 2.0, height / 2.0)
    # center curve from lower - left corner of base equilateral triangle
    translate(-l / 2.0, l * sqrt(3) / 6.0)
    for i in range(4):
        kcurve(0, l)
        rotate(radians(120))
        translate(-l, 0)


def kcurve(x1, x2):
    s = (x2 - x1) / 3.0
    if s < 5:
        pushMatrix()
        translate(x1, 0)
        line(0, 0, s, 0)
        line(2 * s, 0, 3 * s, 0)
        translate(s, 0)
        rotate(radians(60))
        line(0, 0, s, 0)
        translate(s, 0)
        rotate(radians(-120))
        line(0, 0, s, 0)
        popMatrix()
        return

    pushMatrix()
    translate(x1, 0)
    kcurve(0, s)
    kcurve(2 * s, 3 * s)
    translate(s, 0)
    rotate(radians(60))
    kcurve(0, s)
    translate(s, 0)
    rotate(radians(-120))
    kcurve(0, s)
    popMatrix()
