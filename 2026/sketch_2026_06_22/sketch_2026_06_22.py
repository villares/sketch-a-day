# py5 module mode, learn more at <py5coding.org>
# check https://py5coding.org/how_tos/use_processing_libraries.html

from random import choices

import py5
from py5 import sqrt, radians, sin, cos, TWO_PI, random
#from py5_tools import animated_gif
from shapely import Polygon, Point

from processing.sound import SoundFile

polys = []
attempt = []
solution = []
sounds = []
mode = 0  #  0: start, 2: ineract/play
N = 10 # number of sounds to guess

def setup():
    global pos, cs
    py5.size(800, 800)
    py5.fill(0)
    py5.no_stroke()
    py5.frame_rate(30)
    
    this = py5.get_current_sketch()
    sounds[:] = (
        SoundFile(this, f'{i}.aif') for i in range(1, 6))
    
    A = 9000
    for n in [4, 5, 6, 7, 8]:
        r = sqrt(2 * A / (n * sin(TWO_PI / n)))
        if n == 4:
            rot = radians(45)
        elif n == 5:
            rot = radians(180 + 18)
        elif n == 7:
            rot = radians(-90)
        elif n == 8:
            rot = radians(22.5)
        else:
            rot = 0 # hex
        pts = poly(0, 0, r, n, rot=rot)
        p = Polygon(pts)
        polys.append(p)

    pos = poly(400, 400, 250, n=len(polys), rot=radians(30))
    randomize()

def randomize():
    global cs
    cs = choices(range(len(polys)), k=N)
    solution[:] = (polys[i] for i in cs)
    attempt.clear()
    
def draw():
    global mode, focus
    if mode in (0, 1):
        py5.background(127, 200, 127)
        focus = (py5.frame_count // 36) % len(cs)
        if mode == 1 and focus == 0:
            mode = 2
            return
        for i, (x, y) in enumerate(pos):
            with py5.push_matrix():
                py5.translate(x, y)
                if cs[focus] == i:
                    sounds[i].play()
                    py5.scale(1.5)
                    py5.rotate(10 * radians(py5.frame_count))
                py5.shape(polys[i])
        if focus == len(cs) - 1:  # last presentation
            mode = 1

    else:
        py5.background(127, 127, 200)
        py5.fill(255)
        for i, (x, y) in enumerate(pos):
            with py5.push_matrix():
                py5.translate(x, y)
                if polys[i].contains(Point(
                    py5.mouse_x - x, py5.mouse_y - y)):
                    py5.fill(0)
                    sounds[i].play()
                    py5.rotate(10 * radians(py5.frame_count))
                else:
                    py5.fill(255)
                py5.shape(polys[i])
    if py5.is_key_pressed:  # debug
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
            #sounds[i].play()
            attempt.append(polys[i])
    if solution[:len(attempt)] == attempt:
        print('good!')
    else:
        print('failed!')
        py5.no_loop()
            
def key_pressed():
    global mode
    if py5.key == 's':
        mode = 0
        py5.loop()
        randomize()

def poly(x, y, r, n=6, rot=0, rnd=0):
    vs = []
    for i in range(n):
        ox, oy = random(-rnd, rnd), random(-rnd, rnd)
        sx = x + cos(i * TWO_PI / n + rot) * r + ox
        sy = y + sin(i * TWO_PI / n + rot) * r + oy
        vs.append((sx, sy))
    return vs

py5.run_sketch(block=False)

