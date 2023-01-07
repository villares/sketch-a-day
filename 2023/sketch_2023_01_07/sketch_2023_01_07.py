"""
A reticule of colored circles forms The Beatles's Abbey Road album cover

Code for py5 (py5coding.org) 
"""
import py5

def setup():
    py5.size(1000, 1000)
    py5.color_mode(py5.HSB)
    img = py5.load_image('ar.jpg')
    py5.no_stroke()
    py5.background(0)
    s = 10
    w = py5.width // s
    for i in range(w):
        for j in range(w):
            x, y = s // 2 + i * s, s // 2 + j * s
            px = img.get(x, y)
            h = py5.hue(px)
            sat = py5.saturation(px)
            b = 0.36 + py5.brightness(px) / 400
            py5.fill(h, sat * 2, 255)
            py5.circle(x, y, s * b)
    py5.save('out.png')

py5.run_sketch()
