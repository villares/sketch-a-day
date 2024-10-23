# check out https://github.com/py5coding 
# matplotlib must be installed for py5 to know the color names!
import py5
from py5 import css4_colors as CSS

def setup():
    py5.size(300, 300)
    cores = [CSS.RED, CSS.GAINSBORO, CSS.GREENYELLOW,
             CSS.BLUEVIOLET, CSS.ALICEBLUE]
    d = 250
    for cor in cores:
        py5.fill(cor)
        py5.circle(150, 150, d)
        d -= 50
        
    py5.save('out.png')
    
py5.run_sketch()
        