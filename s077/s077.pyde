
"""
sketch 77 180318 - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day

Based on Recursive Tree by Daniel Shiffman.    
"""

add_library('gifAnimation')
from gif_exporter import gif_export

from slider import Slider
A = Slider(0, HALF_PI, QUARTER_PI)
B = Slider(0, 10, 0)
C = Slider(-2, 2, 0)
D = Slider(2, 10, 10)

def setup():
    size(600, 600, P2D)
    A.position(20, height - 60)
    B.position(20, height - 30)
    C.position(width - 180, height - 60)
    D.position(width - 180, height - 30)

def draw():
    global b, c, d
    background(200)
    frameRate(30)
    stroke(0)
    strokeWeight(2)

    a = A.value()  # Angle
    b = B.value()  # branch size randomization
    c = C.value()  # angle randomization
    d = D.value()  # recursion depth

    randomSeed(int(d*10))
    translate(width / 2, height / 2)
    branch(d, a, width/25 + (width/75)*b)

    # #uncomment next lines to export GIF
    # if not frameCount % 10: gif_export(GifMaker,
    #                                    frames=2000,
    #                                    filename="s077")

def branch(gen, theta, branch_size):
    strokeWeight(gen)
    # All recursive functions must have an exit condition!!!!
    if gen > 1:# and branch_size > 1:
        with pushMatrix():
            h = branch_size  * (1 - random(b/3,b) / 15)
            rotate(theta + c * random(1))  # Rotate by theta
            line(0, 0, 0, -h)  # Draw the branch
            translate(0, -h)  # Move to the end of the branch
            # Ok, now call myself to draw two branches!!
            with pushStyle():
                branch(gen - 1, theta, h)
        with pushMatrix():
            h = branch_size  * (1 - random(b/3, b) / 15)
            rotate(-theta + c * random(1))
            line(0, 0, 0, -h)
            translate(0, -h)
            with pushStyle():
                branch(gen - 1, theta, h)
