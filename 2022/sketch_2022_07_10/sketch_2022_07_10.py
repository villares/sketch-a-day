import py5
from py5 import background, no_stroke, fill, rect, remap, PI, sin, cos
# Inspired by Antonio Maluf

from villares.helpers import save_png_with_src

def setup():
    py5.size(900, 900)
    background(220)
    no_stroke()
    step = 40
    speed = 1 / (PI * 90)
    xoff = PI
    for y in range(0, py5.height, step):
        for x in range(0, py5.width, step):
            w = (step + step * sin(x * speed * 2 + xoff) * 0.60) / 2
            h = (step + step * sin(y * speed * 2) * 0.60) / 2
            c = (1 + cos(y * speed * 2)) / 2 #remap(y, 0, py5.width, 1, 0)
            hc = h * c
            fill(0, 100, 0)
            rect(x, y, w, hc)
            fill(0, 100, 200)
            rect(x, y + hc, w, h - hc)
            wb = step - w
            hb = step - h
            xb = x + w
            yb = y + h
            c = (1 - cos(x * speed * 2)) / 2 #/remap(x, 0, py5.height, 0, 1)
            wc = wb * c
            fill(240, 0, 0)
            rect(xb, yb, wc, hb)
            fill(255, 200, 0)
            rect(xb + wc, yb, wb - wc, hb)
            fill(180)
            rect(xb, y, wc, hc)
            fill(255) #100, 0, 100)
            rect(x, yb, w, hb)
            fill(255)
            rect(xb + wc, y + hc, wb - wc, h - hc)

py5.run_sketch()
save_png_with_src()
