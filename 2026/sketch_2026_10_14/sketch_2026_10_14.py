import py5
import numpy as np
from py5_tools import animated_gif

noise_scale = 0.012

def setup():
    py5.size(600, 400, py5.P3D)
    py5.no_smooth()
    py5.color_mode(py5.CMAP, 'viridis', 255)
    py5.stroke_weight(3)
    animated_gif(
        'out.gif',
         frame_numbers=range(1, 361, 6),
        duration=0.1
    )
    
def draw():
    py5.background('k')
    py5.random_seed(42)
    py5.translate(py5.width/2, py5.height/2)
    py5.rotate_y(py5.radians(py5.frame_count))
    N = 720        
    distribution = [abs(py5.random_gaussian()) * 128 for _ in range(N)]
    ang = py5.TWO_PI/len(distribution)
    for d in distribution:
        py5.rotate_x(py5.random(0, py5.PI))
        py5.rotate_z(py5.random(0, py5.PI)) 
        py5.stroke(d)
        py5.line(0, 0, abs(d), 0)

def key_pressed():
    py5.save_frame('out####.png') 

py5.run_sketch()
