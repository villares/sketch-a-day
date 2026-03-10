# Inspired by https://internet-janitor.itch.io/wigglypaint

import py5
from py5_tools import animated_gif

frames = []

def setup():
     py5.size(600, 600)
     py5.frame_rate(12)
     for _ in range(3):
         frames.append(py5.create_graphics(py5.width, py5.height))
     
def draw():
    py5.background(250, 250, 240)
    f = frames[py5.frame_count % 3]
    py5.image(f, 0, 0)

def mouse_dragged():
    x = py5.mouse_x
    y = py5.mouse_y
    for f in frames:
        f.fill(0)
        rx = py5.random(-2, 2)
        ry = py5.random(-2, 2)
        rd = py5.random(2, 3)
        with f.begin_draw():
            f.circle(x + rx, y + ry, rd)
    
def key_pressed():
    if py5.key == 'r':
        for f in frames:
            with f.begin_draw():
                f.clear()
    if py5.key == 's':
        animated_gif(
            'out.gif',
            frame_numbers=[py5.frame_count + i for i in range(1, 4)],
            duration=0.1
        )

py5.run_sketch(block=False)




