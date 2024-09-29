import py5  # check out https://github.com/py5coding 
from py5 import sin, cos, radians
from py5_tools import animated_gif

R = 175
W = 50

def setup():
    py5.size(600, 600)
    py5.no_smooth()
    py5.no_fill()
    #py5.stroke_weight(2)
  
def draw():   # py5 will call this in a loop
    f = py5.frame_count
    py5.translate(py5.width / 2, py5.height / 2)
    py5.background(240)
    for a in range(0, 360, 5):
        raf = radians(a + f)
        ra = radians(a)
        x = R * cos(raf)
        y = R * sin(raf)
        #py5.stroke(0, abs(x // 25) * 25, abs(y // 25) * 25)
        d = W * 2 + W * cos(raf * 2) + W * sin(raf + ra)
        py5.circle(x, y, d)
        
def key_pressed():   # py5 will call this when a key is pressed
    if py5.key == 's':
        f = py5.frame_count
        animated_gif('out3.gif',
                     frame_numbers=range(f + 1, f + 361, 4),
                     duration=0.075) 
        
py5.run_sketch(block=False)
        
        




