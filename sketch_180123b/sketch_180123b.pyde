"""
s18023b - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day

Slider code by Peter Farell (older version tweeked by me)
https://github.com/hackingmath/python-sliders
"""

from slider import Slider

r1 = Slider(-50,50,0)
r2 = Slider(-50,50,0)
np = Slider(3,50,10)

def setup():
    size(500, 500, P2D) # P2D necessary! I'm changing fill() inside Shape
    background(0)
    stroke(255)
    strokeWeight(5)
    r1.position(20, 20)
    r2.position(20, 60)
    np.position(20, 100)


def draw():
    fill(0, 10)
    rect(0, 0, width, height)
    noFill()
    npoints, rad1, rad2 = np.val, 60, 100
    
    with pushMatrix():
        translate(width / 2, height / 2)
        angle = TWO_PI / npoints
        h_angle = angle / 2.
        beginShape()
        #vertex(0, 0)
        a = 0
        while a < TWO_PI:
            rnd1 = random(r1.val, r2.val)    
            rnd2 = random(r1.val, r2.val) 
            sx = cos(a) * rad2 + rnd1
            sy = sin(a) * rad2
            vertex(sx, sy)
            sx = cos(a + h_angle) * rad1
            sy = sin(a + h_angle) * rad1 + rnd2
            vertex(sx, sy)
            a += angle
        endShape(CLOSE)
    npoints, rad1, rad2 = np.value(), r1.value(), r2.value()  # usual way to get values & draw the sliders

    if not frameCount % 10 and frameCount < 500: # used to make a GIF on Gimp
         saveFrame("###.tga")