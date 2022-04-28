# py5.ixora.io imported mode (thonny-py5mode)

from random import randint as r

def setup():
    size(600, 600)
    color_mode(HSB)
    x = 0
    while x < width:
        w = r(2, 32)
        if x + w > width:
            w = width - x
        y = 0
        while y < height:
            h = r(2, 32)
            if y + h > height:
                h = height - y
            fill(w * 8, 256 - h * 8, 200)
            rect(x, y, w, h)
            y += h
        x += w  # つぶやきProcessing

    save_frame("sketch_2022_04_27.png")
