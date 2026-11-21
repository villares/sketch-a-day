import py5
from py5_tools import animated_gif

fs = 0.004  # noise scale factor
R = 120  # noise "walk" radius

def setup():
    py5.size(500, 500)
    py5.color_mode(py5.HSB)
    py5.noise_seed(1)
    py5.background(0)
    py5.no_stroke()
    animated_gif('out.gif',
                 frame_numbers=range(1 + 90, 361 + 90, 2), duration=1/30)

def draw():
    #py5.background(0) # replaced by the translucent fade that enables trails
    py5.fill(0, 32)
    py5.rect(0, 0, py5.width, py5.height)
    # making a closed path to walk on noise space
    ang = py5.radians(py5.frame_count)
    nsx = R + py5.cos(ang) * R 
    nsy = R + py5.sin(ang) * R  
    
    W = py5.width / 2
    for i in range(8):
        x = W + W * py5.os_noise(i / 10 + nsx * fs, nsy * fs)
        y = W + W * py5.os_noise(i / 10 + 1000 + nsx * fs, 100 + nsy * fs)
        py5.fill(i * 32, 255, 255)
        py5.circle(x, y, 10)
    
py5.run_sketch()
    
