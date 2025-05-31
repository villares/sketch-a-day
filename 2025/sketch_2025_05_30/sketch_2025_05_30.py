import py5
from py5_tools import animated_gif

def setup():
    py5.size(500, 500)
    py5.color_mode(py5.HSB)
    py5.stroke_weight(2)
    animated_gif('out.gif', duration=0.2, frame_numbers=range(1, 361, 10))
    
def draw():
    py5.background(0)
    passo = 0.002
    f = py5.radians(py5.frame_count)
    xo = 250 + 50 * py5.cos(f)
    yo = 250 + 50 * py5.sin(f)
    for x in range(0, 500, 20):
        for y in range(0, 500, 20):
            n = py5.os_noise((x + xo) * passo,
                             (y + yo) * passo) # precisa x, y
            h = 125 + n * 125
            py5.stroke(h, 200, 200)
            with py5.push_matrix():
                py5.translate(x, y)
                py5.rotate(n * py5.PI)
                py5.line(-10, 0, 10, 0)
            
py5.run_sketch()
