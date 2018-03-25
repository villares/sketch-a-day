
"""
sketch 74 180315 - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day

Based on Recursive Tree by Daniel Shiffman.    
"""
 
add_library('gifAnimation')
from gif_exporter import gif_export

from slider import Slider
A = Slider(0, HALF_PI, HALF_PI)
B = Slider(0.5, 0.70, 0.66)
C = Slider(-2, 2, 0)
D = Slider(0, 10, 0)

def setup():
    size(600, 600, P2D)
    frameRate(30)
    A.position(20, height - 60)
    B.position(20, height - 30)
    C.position(width - 180, height - 60)
    D.position(width - 180, height - 30)

def draw():
    global c, d
    background(0)
    stroke(255)
    strokeWeight(2)

    a = A.value()  # Angle
    b = B.value()  # branch size factor
    c = C.value()  # angle randomization
    d = D.value()  # branch size randomization
    
    randomSeed(1)
    translate(width / 2, height / 2)
    branch(120, a, b)
    
    # uncomment next line to export GIF
    #if not frameCount % 10: gif_export(GifMaker, frames=3000)

def branch(h, theta, size_factor):
    h *= size_factor
    # All recursive functions must have an exit condition!!!!
    if h > 1.5:
        # Save the current state of transformation (i.e. where are we now)
        with pushMatrix():
            rotate(theta + c * random(1))  # Rotate by theta
            line(0, 0, 0, -h)  # Draw the branch
            translate(0, -h)  # Move to the end of the branch
            # Ok, now call myself to draw two branches!!
            branch(h + random(-d, 0), theta, size_factor)
        # Repeat the same thing, only branch off to the "left" this time!
        with pushMatrix(): # this 'with' context pops matrix on exit
            rotate(-theta + c * random(1))
            line(0, 0, 0, -h)
            translate(0, -h)
            branch(h + random(-d, 0), theta, size_factor)
