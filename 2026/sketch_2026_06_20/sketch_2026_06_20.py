from random import choices

import py5
from py5_tools import animated_gif
from shapely import Polygon, Point
from py5 import sqrt, radians, sin, cos, TWO_PI, random

polys = []
attempt = []
solution = []
mode = -2

def setup():
    global pos, cs
    py5.size(800, 800)
    py5.fill(0)
    py5.no_stroke()
    A = 9000
    for n in [3, 4, 5, 6, 7, 8]:
        r = sqrt(2 * A / (n * sin(TWO_PI / n)))        
        if n == 7:
            rot = radians(-90)
        elif n == 8:
            rot = radians(22.5)
        elif n == 5:
            rot = radians(180 + 18)
        else:
            rot = 0
        pts = poly(0, 0, r, n, rot=rot)
        p = Polygon(pts)
        polys.append(p)

    N = len(polys)
    pos = poly(400, 400, 250, n=N, rot=radians(30))
    randomize()
#     animated_gif('out.gif',
#                  frame_numbers=range(1, 361, 4),
#                  duration=0.05
#                  )

def randomize():
    N = len(polys)
    cs = choices(range(N), k=10)
    solution[:] = (polys[i] for i in cs)   
    
def draw():
    global mode, focus
    if mode in (0, 1):
        py5.background(127, 200, 127)
        focus = (py5.frame_count // 36) % len(cs)
        #print(focus)
        for i, (x, y) in enumerate(pos):
            with py5.push_matrix():
                py5.translate(x, y)
                if cs[focus] == i:
                    py5.scale(1.5)
                    py5.rotate(10 * radians(py5.frame_count))
                py5.shape(polys[i])
        if focus == len(cs) - 1:
            print(focus, mode)
            mode = 1
        if mode == 1 and focus == 1:
            print(focus, mode) 
            mode = 2        
    else:
        py5.background(127, 127, 200)
        py5.fill(255)
        for i, (x, y) in enumerate(pos):
            with py5.push_matrix():
                if polys[i].contains(Point(
                    py5.mouse_x - x, py5.mouse_y - y)):
                    py5.fill(0)
                else:
                    py5.fill(255)
                py5.translate(x, y)
                py5.shape(polys[i])
    if mode == -2:
        py5.translate(50, 700)
        py5.scale(1/5, 1/5)
        py5.fill(0)
        with py5.push_matrix():
            for p in solution:
                py5.shape(p)
                py5.translate(150, 0)
        py5.translate(0, 100)
        py5.fill(255)
        for p in attempt:
            py5.shape(p)
            py5.translate(150, 0)


def mouse_clicked():
    for i, (x, y) in enumerate(pos):
        if polys[i].contains(Point(
            py5.mouse_x - x, py5.mouse_y - y)):
            attempt.append(polys[i])
            
def key_pressed():
    py5.save_frame('out###.png')

def poly(x, y, r, n=6, rot=0, rnd=0):
    vs = []
    for i in range(n):
        ox, oy = random(-rnd, rnd), random(-rnd, rnd)
        sx = x + cos(i * TWO_PI / n + rot) * r + ox
        sy = y + sin(i * TWO_PI / n + rot) * r + oy
        vs.append((sx, sy))
    return vs

py5.run_sketch(block=False)
