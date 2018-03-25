
"""
sketch 76 180317 - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day

Based on Recursive Tree by Daniel Shiffman.    
"""

add_library('gifAnimation')
from gif_exporter import gif_export

from slider import Slider
A = Slider(0, HALF_PI, QUARTER_PI)
B = Slider(0, 10, 0)
C = Slider(-2, 2, 0)
D = Slider(2, 15, 10)

def setup():
    size(600, 600, P2D)
    frameRate(30)
    A.position(20, height - 60)
    B.position(20, height - 30)
    C.position(width - 180, height - 60)
    D.position(width - 180, height - 30)

def draw():
    global b, c, d
    background(0)
    stroke(255, 100)
    strokeWeight(2)

    a = A.value()  # Angle
    b = B.value()  # branch size randomization
    c = C.value()  # angle randomization
    d = D.value()  # recursion depth

    randomSeed(1)
    translate(width / 2, height / 2)
    branch(d, a, width/30)

    # uncomment next line to export GIF
    if not frameCount % 10: gif_export(GifMaker,
                                       frames=2000,
                                       filename="s076")

def branch(gen, theta, branch_size):
    # Each branch will be 2/3rds the size of the previous one

    strokeWeight(gen)
    # All recursive functions must have an exit condition!!!!
    if gen > 1 and branch_size > 1:
        h = branch_size * (1 + random(b) / 4)
        branch_size *= 1 - random(b) / 10
        # Save the current state of transformation (i.e. where are we now)
        with pushMatrix():
            rotate(theta + c * random(1))  # Rotate by theta
            line(0, 0, 0, -h)  # Draw the branch
            translate(0, -h)  # Move to the end of the branch
            # Ok, now call myself to draw two branches!!
            pushStyle()
            branch(gen - 1, theta, branch_size)
            popStyle()
        # Repeat the same thing, only branch off to the "left" this time!
        with pushMatrix():
            rotate(-theta + c * random(1))
            line(0, 0, 0, -h)
            translate(0, -h)
            pushStyle()
            branch(gen - 1, theta, branch_size)
            popStyle()
