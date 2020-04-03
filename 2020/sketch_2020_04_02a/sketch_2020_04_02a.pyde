"""
Draw a rotating cube
https://rosettacode.org/wiki/Draw_a_rotating_cube#Processing
Processing 3.4
2020-04 Alexandre Villares

Task:

Draw a rotating cube.

It should be oriented with one vertex pointing straight up, and its opposite
vertex on the main diagonal (the one farthest away) straight down. It can be
solid or wire-frame, and you can use ASCII art if your language doesn't have
graphical capabilities. Perspective is optional.
"""

# Create a cube in Processing with box(), rotate the scene with rotate(),
# and drive rotation with either the built-in millis() or frameCount timers.

def setup():
    size(500, 500, P3D)

def draw():
    background(0)
    # position
    translate(width / 2, height / 2, -width / 2)
    # optional fill and lighting colors
    noStroke()
    strokeWeight(4)
    fill(192, 255, 192)
    pointLight(255, 255, 255, 0, -500, 500)
    # rotation driven by built-in timer
    rotateY(millis() / 1000.0)
    # rotateY(frameCount/60.0)
    # draw box
    box(300, 300, 300)
