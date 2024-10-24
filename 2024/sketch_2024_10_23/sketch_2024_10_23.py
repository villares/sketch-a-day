# check out https://github.com/py5coding 
# matplotlib must be installed for py5 to know the color names!
import py5
from py5 import css4_colors as CSS
from py5_tools import animated_gif

cores = [CSS.RED, CSS.BLUE, CSS.GREENYELLOW,
         CSS.BLUEVIOLET, CSS.BLACK]

def setup():
    py5.size(300, 300)
    animated_gif('out.gif', duration=0.1,
                 frame_numbers=range(1, 360, 4))
    
def draw():
    py5.background(CSS.WHITE)
    d = 250
    for i, cor in enumerate(cores):
        py5.fill(cor)
        fa = py5.radians(py5.frame_count)
        offset = 50 * py5.sin(i * 3.14 / 4 + fa)
        py5.circle(150, 150, d + offset)
        d -= 50
        
    
py5.run_sketch()
        