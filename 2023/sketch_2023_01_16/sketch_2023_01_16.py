"""
Code for py5 (py5coding.org) imported mode
"""

def setup():
    size(880, 600)
    no_loop()
    global H, s
    s = 3
    H = (height * s) / 10

def f(x, m=1):
    y = H * (
        sin(x / 50) *
        sin(x / 13) * 
        sin(x / 97)
        ) * m
    stroke(200, 0, 0, 200)
    line(x,  y, x, -s * height / 2)
    y2 = H * ( #-0.5 +
        sin(x / 70) +
        sin(x / 50) *
        sin(x / 13) * 
        sin(x / 97)
        ) * m
    stroke(0, 0, 200, 200)
    line(x, y2, x, height * s)

def draw():
    background(240)
    translate(width / 2, height / 2)
    scale(1 / s)
    for x in range(-width // 2 * s, width // 2 * s):        
        f(x)
        f(x, m=-1)
        
    save('out.png')
