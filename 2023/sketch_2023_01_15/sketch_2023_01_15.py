"""
Code for py5 (py5coding.org) imported mode
"""

from villares.helpers import save_png_with_src
def setup():
   size(880, 600)
   no_loop()
   
def draw():
    background(240)
    s = 3
    H = (height * s) / 10
    scale(1 / s)
    for x in range(width * s):
        y = H * (
#             sin(x / 30) +
            sin(x / 50) *
            sin(x / 13) * 
            sin(x / 97)
            )
        stroke(200, 0, 0, 200)
        line(x, s * height / 2 + y, x, 0)
        y2 = H * ( #-0.5 +
            sin(x / 70) +
            sin(x / 50) *
            sin(x / 13) * 
            sin(x / 97)
            )
        stroke(0, 0, 200, 200)
        line(x, s * height / 2 + y2, x, height * s)
        
    
    save_png_with_src()

def key_pressed():
    print(key)
    redraw()
