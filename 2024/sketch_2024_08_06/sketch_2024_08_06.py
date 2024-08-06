from itertools import product

import py5

def setup():
    py5.size(600, 600)
    py5.rect_mode(py5.CENTER)
    py5.no_fill()

def draw():
    py5.background(100)
    for i, j in product(range(5), repeat=2):
        s = 100
        h = py5.sqrt(3) * s
        v = s * 1.5
        x = i * h + (h / 4 if j % 2 else -h / 4)
        y = j * v
        py5.stroke(0)
        #poly(x, y, h) # 173.2
        poly(x, y, 177)
        py5.stroke(255)
        poly(x, y, 122)  
    
def poly(x, y, r, n=8):
    with py5.push_matrix():
        py5.translate(x, y)
        with py5.begin_closed_shape():
            for i in range(n):
                sx = py5.cos(i * py5.TWO_PI / n) * r
                sy = py5.sin(i * py5.TWO_PI / n) * r
                py5.vertex(sx, sy)
        
def key_pressed():
    py5.save('out.png')

py5.run_sketch(block=False)
