from itertools import product
import py5

def setup():
    global osb, svg, mask
    py5.size(500, 500)
    py5.color_mode(py5.CMAP, py5.mpl_cmaps.TWILIGHT, 100)
    py5.background('black')
    py5.no_stroke()
    
    step = 25
    for x, y in product(range(0, 500, step), repeat=2):
        py5.fill(py5.random_int(100))
        py5.circle(x + step / 2, y + step / 2, step * 0.9)
   
    py5.save('out.png')
   
py5.run_sketch(block=False)
