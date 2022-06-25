from math import sin, cos, pi
from itertools import product
import py5

from villares.helpers import save_png_with_src


W = 15

def setup():
    py5.size(1803, 507)
    #py5.no_cursor()
    py5.blend_mode(py5.ADD)

#def draw():
    py5.background(0)
    cols, rows = 80, 20
    H = W * py5.sqrt(3) * 0.5  # W * sin(radians(60))
    steps = py5.width / 360    # ~5
    for i, j in product(range(cols), range(rows)):
        x = i * W * 1.5 + W - 2
        if i % 2 == 0:
            y = j * H * 2 #+ H
        else:
            y = j * H * 2 + H #* 2        
        n = round(6 + 6 * sin(py5.radians(x / steps)))
        py5.fill(0, 0, 255) 
        d = H / 2 + H / 2 * cos(py5.radians(x / steps) - py5.HALF_PI)
        star(x, y, d, H, 3 + n)
        
        py5.fill(255, 0, 0)
        d = H / 2 + H / 2 * cos(py5.radians(x / steps) + py5.HALF_PI)
        star(x, y, d, H, 3 + n)
        
        d = H / 2 + H / 2 * cos(py5.radians(x / steps))
        py5.fill(0, 255, 0)
        star(x, y, d, H, (3 + n))
        
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
save_png_with_src(__file__[:-2] + '.png')
