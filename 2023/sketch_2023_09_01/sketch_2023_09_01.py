import numpy as np
import py5

def setup():
    py5.size(600, 600)
    py5.stroke_weight(3)
    t = np.arange(6000) / 10
    t = np.column_stack((t, t))
    o = np.array([0, 600])
    v = np.array([8, -30])
    f = np.array([0, 0.4])    
    pos = o + v * t + f * t ** 2
    py5.points(pos)
    
py5.run_sketch()