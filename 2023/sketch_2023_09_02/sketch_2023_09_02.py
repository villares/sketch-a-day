import numpy as np
import py5

def setup():
    py5.size(1200, 600)
    t = np.arange(600)
    t = np.column_stack((t, t))
    o = np.array([0, 600])
    va = np.array([8, -30])
    vb = np.array([16, -20])
    f = np.array([0, 0.4])    
    pos_a = o + va * t + f * t ** 2
    pos_b = o + vb * t + f * 0.5 * t ** 2
    py5.lines(np.column_stack((pos_a, pos_b)))
    
py5.run_sketch(block=False)