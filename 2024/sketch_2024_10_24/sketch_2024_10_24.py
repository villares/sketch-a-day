# check out https://github.com/py5coding/py5generator 
# matplotlib must be installed for py5 to know the color names!
import py5
from py5_tools import animated_gif


def setup():
    py5.size(400, 400)
    py5.frame_rate(30)
    animated_gif('out.gif', duration=4/30,
                 frame_numbers=range(1, 180, 4))
    # I get away with 180° because I used squared cos :)
    
def draw():
    py5.background(240)
    for _ in range(20):
        py5.translate(200, 200)
        py5.rotate(py5.radians(18))
        py5.translate(-200, -200)
        for i in range(10):
            f = 20 + 20 * py5.cos(py5.radians(py5.frame_count)) ** 2
            x =  i * f
            py5.line(x, 400 - x, x - 200, 400 - x - 200)
     
py5.run_sketch()
        