# Inspired by https://internet-janitor.itch.io/wigglypaint

import py5
from py5_tools import animated_gif

frames = []
mode = 0
mcolor = py5.color(200, 300, 200, 100)

def setup():
     py5.size(600, 600)
     py5.frame_rate(12)
     for _ in range(6):
         frames.append(py5.create_graphics(py5.width, py5.height))
     
def draw():
    py5.background(250, 250, 240)
    py5.image(frames[py5.frame_count % 3], 0, 0)     # first 3
    py5.image(frames[3 + py5.frame_count % 3], 0, 0) # last 3

def mouse_dragged():
    x = py5.mouse_x
    y = py5.mouse_y
    if mode == 0:
        black_lines(x, y, frames[3:]) # last 3
    elif mode == 1:
        dots(x, y, frames[3:]) # last 3
    elif mode == 2:    
        marker(x, y, frames[:3])

def mouse_clicked():
    mouse_dragged()

def dots(x, y, fs):
    for frame in fs:
        with frame.begin_draw():
            frame.fill(0)
            frame.no_stroke()
            r = 20
            rx, ry = r, r
            while (rx ** 2 + ry ** 2) > r ** 2:
                rx = py5.random(-r, r)
                ry = py5.random(-r, r)
            rd = py5.random(2, 3)
            frame.circle(x + rx, y + ry, rd)
    
def black_lines(x, y, fs):
    for frame in fs:
        rx = py5.random(-2, 2)
        ry = py5.random(-2, 2)
        rd = py5.random(2, 3)
        with frame.begin_draw():
            frame.fill(0)
            frame.stroke(0)
            frame.circle(x + rx, y + ry, rd)

def marker(x, y, fs):
    for frame in fs:
        rx = py5.random(-2, 2)
        ry = py5.random(-2, 2)
        rd = py5.random(18, 22)
        with frame.begin_draw():
            frame.fill(mcolor)
            frame.no_stroke()
            frame.circle(x + rx, y + ry, rd)


def key_pressed():
    global mode
    if py5.key == 'r':
        for f in frames:
            with f.begin_draw():
                f.clear()
    elif py5.key == 's':
        animated_gif(
            'out.gif',
            frame_numbers=[py5.frame_count + i for i in range(1, 4)],
            duration=0.1
        )
    elif py5.key == ' ':
        mode = (mode + 1) % 3


py5.run_sketch(block=False)




