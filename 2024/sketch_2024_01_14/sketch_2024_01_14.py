# py5coding.org imported mode
import py5_tools

curvas = []
n = 3

def setup():
    size(30, 30)
    no_smooth()
    no_fill()
    stroke(255)
    curvas[:] = []
    for i in range(n):
        curvas.append((
              random(-height / 7, height / 7),
              random(-height / 7, height / 7),
              random(.33, 3),
              random(.33, 3),
              random(.33, 3),
             ))
    py5_tools.animated_gif('out.gif',
                           frame_numbers=range(1,11),
                           duration=0.1)
        
def key_pressed():
    if key == "s":
        save_frame("###.gif")

def draw():
    background(0)
    f = radians(frame_count) * 360
    translate(0, height / 2)
    for i, (h, a, f1, f2, f3) in enumerate(curvas):
        begin_shape()
        for x in range(width):
            ang = (f +  x) / 30
            ang2 = (f * 2 + x) / 30
            s = sin(ang * f1) + sin(ang2 * f2) * sin(ang2 * f3) + cos(ang * f3) 
            vertex(x, h + s * a)
        end_shape()
        