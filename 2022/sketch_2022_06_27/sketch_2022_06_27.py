from math import sin, cos, pi
from itertools import product
import py5, py5_tools

#from villares.helpers import save_png_with_src


W = 30

def setup():
    py5.size(1806, 496)
    #py5.no_cursor()
    py5.frame_rate(10)
 #   py5_tools.animated_gif('out.gif', count=50, period=0.1, duration=0.1)


def draw():
    py5.background(200)
    cols, rows = 40, 9
    H = W * py5.sqrt(3) * 0.5  # W * sin(radians(60))
    steps = py5.width / 720    # ~5
    for i, j in product(range(cols), range(rows)):
        x = i * W * 1.5 + W - 2
        if i % 2 == 0:
            y = j * H * 2 + H
        else:
            y = j * H * 2 + H * 2
        t = py5.radians(py5.frame_count * 3.6) 
        t2 = py5.radians(py5.frame_count * 7.2) 
        n = round(4 + 4 * sin(py5.radians(x / steps) + t))
        py5.no_stroke()
        py5.fill(100, 200) 
        d = H / 2 + H / 2 * cos(py5.radians(x / steps) / 2 - py5.HALF_PI + t)
        star(x, y, d, H - d, 3 + n,  py5.radians(x))
        
        py5.no_fill()
        py5.stroke(0)
        d = H / 2 + H / 2 * cos(py5.radians(x / steps) + py5.HALF_PI + t)
        star(x, y, d, H / 2, 3 + n, py5.radians(x))
        
        d = H / 2 + H / 2 * cos(py5.radians(x / steps) / 2 + py5.PI + t2)
        py5.stroke(255)
        star(x, y, d, H / 2, (3 + n), py5.radians(x))
        
def star(cx, cy, ra, rb, n=7, start_ang=0):  # estrela
    step = py5.TWO_PI / n  
    py5.begin_shape()
    for i in range(n):  # for each tip/point
        ang = start_ang + step * i # angle
        ax = cx + cos(ang) * ra
        ay = cy + sin(ang) * ra
        py5.vertex(ax, ay)
        bx = cx + cos(ang + step / 2.0) * rb
        by = cy + sin(ang + step / 2.0) * rb
        py5.vertex(bx, by)
    py5.end_shape(py5.CLOSE)


py5.run_sketch()
#save_png_with_src()
