"""
Inspired by x_0073 by Tom Larrow
https://codeberg.org/TomLarrow/creative-coding-experiments/src/branch/main/x_0073/x_0073.py
"""

import numpy as np
import py5

def setup():
    global striped_circle
    py5.size(800, 800)
    py5.image_mode(py5.CENTER) # draw images from center
    striped_circle = make_circle()

def make_circle():
    # circle
    c = py5.create_graphics(py5.width, py5.height)
    c.begin_draw()
    c.clear()  # transparent background NOW THIS IS NECESSARY!
    c.stroke_weight(10)
    c.stroke(0, 100, 0)
    c.fill(0, 0, 100, 50) # check ou this translucent fill!
    for shrink in range(10):
        c.circle(c.width / 2, c.height / 2, c.width * (0.75 - shrink / 12))
    c.end_draw()
    # mask with stripes
    m = py5.create_graphics(py5.width, py5.height)
    m.begin_draw()
#     m.fill(255) # visible circle
#     m.circle(c.width / 2, c.height / 2, c.width * 0.75)
    m.fill(0)  # transparent stripes
    for x in range(0, m.width, 150):
        m.rect(x, 0, 50, m.height)
    m.end_draw()
    # apply mask and return image
    c.load_np_pixels()
    m.load_np_pixels()
    c.np_pixels[:, :, 0] = np.where(m.np_pixels[:, :, 0] < c.np_pixels[:, :, 0],
                                    m.np_pixels[:, :, 0], c.np_pixels[:, :, 0])
    c.update_np_pixels()
    return c

def draw():
     py5.background(0, 100 , 0)
     py5.stroke_weight(30)
     py5.stroke(0, 0, 100)
     for y in range(0, py5.height + 1, 40):
         r = 20 * py5.noise(y * 0.03, py5.frame_count * 0.03)
         py5.line(0, y + r, py5.width, y - r)
     py5.translate(py5.width / 2, py5.height / 2)
     py5.rotate(py5.radians(py5.frame_count))
     py5.image(striped_circle, 0, 0)


py5.run_sketch()
