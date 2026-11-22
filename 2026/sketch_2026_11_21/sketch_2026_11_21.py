import py5
from py5_tools import animated_gif
import numpy as np

fs = 0.001  # noise scale factor
R = 600     # noise "walk" radius for looping paths
TR = 200    # noise "walk" radius for animation loop

def setup():
    global cs,angles, indices
    py5.size(500, 500, py5.P2D)
    py5.color_mode(py5.HSB)
    py5.noise_seed(1)
    py5.background(0)
    py5.stroke_weight(3)
    hues = np.tile(np.arange(8) * 32, 360)
    cs = [py5.color(h, 255, 255) for h in hues]
    animated_gif('out.gif',
                 frame_numbers=range(1 + 90, 361 + 90, 2), duration=1/20)
    angles = np.radians(np.arange(360)) 
    indices = np.arange(8)
#     global angle_grid, index_grid 
#     angle_grid, index_grid = np.meshgrid(angles, indices, indexing="ij")


def draw():
    global x, y, indices, angles
    py5.background(0)
    W = py5.width / 2
    f = py5.frame_count
    t = py5.radians(py5.frame_count)    
    tx = W + np.cos(t) * TR
    ty = W + np.sin(t) * TR
    for a in range(360):
        ang = py5.radians(a)    
        nsx = R + py5.cos(ang) * R 
        nsy = R + py5.sin(ang) * R  
        for i in range(8):
            x = W + W * py5.os_noise(
                (i * 50 + nsx) * fs,
                nsy * fs,
                tx * fs,
                ty * fs)
            y = W + W * py5.os_noise(
                (i * 50 + nsx) * fs + 1000,
                nsy * fs - 1000,
                tx * fs,
                ty * fs)
            py5.stroke(i * 32, 255, 255)
            py5.point(x, y)

#     # this ended up slow...
#
#     nsx = R + np.cos(angle_grid) * R     
#     nsy = R + np.sin(angle_grid) * R
#     x = W + W * py5.os_noise(
#         (index_grid * 50 + nsx) * fs,
#         nsy * fs,
#         tx * fs,
#         ty * fs)
#     y = W + W * py5.os_noise(
#         (index_grid * 50 + nsx) * fs,
#         100 + nsy * fs,
#         tx * fs,
#         ty * fs)
#     coords = np.column_stack((x.ravel(), y.ravel()))
#     shp = py5.create_shape()
#     with shp.begin_shape(py5.POINTS):
#         shp.stroke_weight(3)
#         shp.vertices(coords)
#     shp.set_strokes(cs)
#     py5.shape(shp, 0, 0)
  
py5.run_sketch(block=False)
