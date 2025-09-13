

import py5

def setup():
    py5.size(500, 500)
    py5.color_mode(py5.CMAP, py5.mpl_cmaps.VIRIDIS, 255)
    for r in range(100):
        y = py5.random_int(-50, 450)
        x = py5.random_int(-128, 255 + 128)
        for i in range(255):
            py5.stroke(i)
            py5.line(x + i, y, x + i, y + 100)
    py5.save('out.png')
    
py5.run_sketch(block=False)
