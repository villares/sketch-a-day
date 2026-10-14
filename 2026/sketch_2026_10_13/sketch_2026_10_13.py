import py5
import numpy as np

noise_scale = 0.012

def setup():
    py5.size(600, 400, py5.P2D)
    py5.color_mode(py5.CMAP, 'viridis', 255)
    py5.stroke_weight(3)
def draw():
    py5.background('k')
    py5.random_seed(42)
    py5.translate(py5.width/2, py5.height/2)
    distribution = [py5.random_gaussian() * 128 for _ in range(360)]
    for d in distribution: 
        py5.rotate(py5.TWO_PI/len(distribution))
        py5.stroke(d)
        py5.line(0, 0, abs(d), 0)

def key_pressed():
    py5.save_frame('out####.png') 

py5.run_sketch()
