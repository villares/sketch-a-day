import py5
from py5_tools import animated_gif

def setup():
    py5.size(500, 500)
    py5.color_mode(py5.HSB)
    py5.no_stroke()
    animated_gif('out.gif', duration=0.2, frame_numbers=range(1, 361, 10))
    
def draw():
    py5.background(0)
    passo = 0.003
    f = py5.radians(py5.frame_count)
    xo = 1000 + 50 * py5.cos(f)
    yo = 1000 + 50 * py5.sin(f)
    for x in range(-20, 521, 20):
        for y in range(-20, 521, 20):
            n = py5.os_noise((x + xo) * passo,
                             (y + yo) * passo,
                             (py5.sqrt(xo * yo)) * passo * 2,
                             ) 
            h = 125 + n * 125
            py5.fill(h, 200, 200)
            with py5.push_matrix():
                py5.translate(x + 10, y + 10)
                py5.rotate(n * py5.PI)
                py5.square(0, 0, 15)
            
py5.run_sketch()
