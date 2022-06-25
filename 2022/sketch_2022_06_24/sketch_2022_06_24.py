from math import sin, cos
from itertools import product
import py5

W = 15

def setup():
    py5.size(1803, 507)
    py5.no_cursor()
    py5.blend_mode(py5.SUBTRACT)

def draw():
    py5.background(200)
    cols, rows = 80, 20
    H = W * py5.sqrt(3) * 0.5  # W * sin(radians(60))
    print(py5.degrees(py5.frame_count / 10) % 360)
    for i, j in product(range(cols), range(rows)):
        x = i * W * 1.5 + W - 2
        if i % 2 == 0:
            y = j * H * 2 #+ H
        else:
            y = j * H * 2 + H #* 2
        
        py5.fill(0, 0, 255)
        d = H + H * cos(x / 300 - py5.frame_count / 5)
        star(x, y, d, H, 3 + int(x / H) % 11)
        
        py5.fill(255, 0, 0)
        d = H + H * cos(x / 300 + py5.frame_count / 10)
        star(x, y, d, H, 3 + int(x / H) % 11)
        
        d = H / 2 + H / 2 * cos(x / 300)
        py5.fill(0, 255, 0)
        star(x, y, d, H, 3 + int(x / H) % 11)
        
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
