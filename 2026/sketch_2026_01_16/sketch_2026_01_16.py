from itertools import product 
import py5

seed = 0

def setup():
    py5.size(900, 900)
    #py5.color_mode(py5.CMAP, 'viridis_r', py5.width / 8)
    py5.no_fill()

def draw():
    py5.random_seed(seed)
    py5.background('black') 
    for (x, y), (a, b) in zip(product((150, 450, 750), repeat=2),
                              product((0, 0.5, 1), repeat=2)):
        recursive_hex(x, y, py5.width / 18, a=a, b=b)
    
def recursive_hex(xo, yo, r, n=6, a=0, b=0):
    rf = r / 5
    pts = [(xo + r * py5.cos(i * py5.TWO_PI / n) + py5.random(-rf, rf) * a,
            yo + r * py5.sin(i * py5.TWO_PI / n) + py5.random(-rf, rf) * a)
           for i in range(n)]
    m = py5.width / 68
    if r > m:
        rr = py5.remap(b, 0, 1,
                       r * 0.52, max(0, r - m * 0.9)) 
        for x, y in pts:
            recursive_hex(x, y, rr, n, a=a, b=b)
    py5.stroke(255, 128) #r, 200) 
    with py5.begin_closed_shape():
        py5.vertices(pts)


def key_pressed():
    if py5.key == 's':
        py5.save_frame('###.png')
    
py5.run_sketch(block=False)

