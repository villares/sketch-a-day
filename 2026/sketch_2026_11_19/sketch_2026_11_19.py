import py5
from py5_tools import animated_gif

def setup():
    py5.size(500, 500)
    py5.background(0)
    py5.no_stroke()
    animated_gif(
        'out2.gif',
        frame_numbers=range(1 + 90, 361 + 90, 2),
        duration=1/30,
    )
    
def draw():
    #py5.background(0)
    py5.fill(0, 32)
    py5.rect(0, 0, py5.width, py5.height)
    ang = py5.radians(py5.frame_count)
    R = 250
    x = R + py5.cos(ang) * R
    y = R + py5.sin(ang) * R
    fs = 0.003
    
    nx = 250 + 250 * py5.os_noise(x * fs, y * fs)
    ny = 250 + 250 * py5.os_noise(1000 + x * fs, y * fs)
    py5.fill(255, 0, 0)
    py5.circle(nx, ny, 10)
    
    nx = 250 + 250 * py5.os_noise(0.1 + x * fs, y * fs)
    ny = 250 + 250 * py5.os_noise(1000.2 + x * fs, y * fs)
    py5.fill(0, 0, 255)
    py5.circle(nx, ny, 10)
    
py5.run_sketch()
    
