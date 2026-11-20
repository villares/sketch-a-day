import py5
from py5_tools import animated_gif

fs = 0.003  # noise scale factor
R = 250  # noise "walk" radius

def setup():
    py5.size(500, 500)
    #py5.noise_seed(1)
    py5.background(0)
    py5.no_stroke()
    animated_gif(
        'out.gif',
        frame_numbers=range(1 + 90, 361 + 90, 2),
        duration=1/30,
    )

def draw():
    #py5.background(0) # replaced by the translucent fade that enables trails
    py5.fill(0, 32)
    py5.rect(0, 0, py5.width, py5.height)
    # making a closed path to walk on noise space
    ang = py5.radians(py5.frame_count)
    x = R + py5.cos(ang) * R
    y = R + py5.sin(ang) * R
    
    W = py5.width / 2
    nx = W + W * py5.os_noise(x * fs, y * fs)
    ny = W + W * py5.os_noise(1000 + x * fs, y * fs)
    py5.fill(255, 0, 0)
    py5.circle(nx, ny, 10)
    nx = W + W * py5.os_noise(0.1 + x * fs, y * fs)
    ny = W + W * py5.os_noise(1000.2 + x * fs, y * fs)
    py5.fill(0, 0, 255)
    py5.circle(nx, ny, 10)
    
py5.run_sketch()
    
