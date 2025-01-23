import py5
from py5_tools import animated_gif

def setup():
    py5.size(600, 600,py5.P2D)
    py5.color_mode(py5.HSB)
#     animated_gif('out.gif', duration=0.2,
#                  frame_numbers=range(1, 361, 5),
#                  optimize=False)
    
def draw():
    py5.background(0)
    ang = py5.radians(py5.frame_count)
    a = 30 * py5.cos(ang) + 300
    b = 30 * py5.sin(ang) + 300
    escala_noise = 0.005
    with py5.begin_shape(py5.LINES):
        for x in range(600):
            n = py5.os_noise(x * escala_noise,
                             a * escala_noise,
                             b * escala_noise) # -1 a 1
            y = 150 + n * 150
            py5.stroke(50 + y / 5 % 255, 200, y)
            py5.vertex(x, 300-y, x, 300+y)
            py5.stroke(50 + (x + y) / 5 % 255, 200, 255)
            py5.vertex(x, 300+y)
    
    if py5.frame_count in range(1, 361, 5):
        py5.save_frame('###.png')



py5.run_sketch()
        