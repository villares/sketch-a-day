import numpy as np
import py5

a = np.array([150, 10, 10, 250])
b = np.array([20, 20, 250, 100]) 
t = np.linspace(0, 1, 20)
# a_expanded = a[:, np.newaxis]  # np.newaxis is an 
# b_expanded = b[:, np.newaxis]  # alias for None!
# r = a_expanded + (b_expanded - a_expanded) * t
r = py5.lerp(a[:,np.newaxis], b[:,np.newaxis], t)

def setup():
    py5.size(300, 300)
    py5.lines(r.T)
    
py5.run_sketch()
