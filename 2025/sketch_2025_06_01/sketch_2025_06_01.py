import py5
from py5_tools import animated_gif

def setup():
    py5.size(500, 500)
    py5.color_mode(py5.HSB)
    py5.no_stroke()
    animated_gif('out.gif', duration=0.2, frame_numbers=range(1, 361, 10))
    
def draw():
    py5.background(255)
    passo = 0.003
    w = 20
    f = py5.radians(py5.frame_count)
    zo = 1000 + 50 * py5.cos(f)
    yo = 1000 + 50 * py5.sin(f)
    for x in range(-w, py5.width, w):
        for y in range(-w, py5.height, w):
            n = py5.os_noise((x - zo) * passo,
                             (y + yo) * passo,
                             zo * passo * 2,
                             ) 
            h = int(32 - n * 32) * 4
            py5.fill(h)
            with py5.push_matrix():
                py5.rect_mode(py5.CENTER)
                py5.translate(x + w / 2, y + w / 2)
                py5.rotate(n * py5.PI / 2)
                py5.square(0, 0, w * 0.75)
            
py5.run_sketch()
