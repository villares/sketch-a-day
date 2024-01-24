from itertools import product

from matplotlib.colors import LinearSegmentedColormap
import py5, py5_tools
import numpy as np

fx = 300
fy = 300
N = 128 // 2
pts = np.array(list(product(range(-N, N), repeat=2)), dtype='float64')

# colors = [py5.xkcd_colors.RICH_BLUE,
#           py5.xkcd_colors.LIGHT_BLUE,
#           py5.xkcd_colors.BRIGHT_RED,
#           py5.xkcd_colors.BRIGHT_RED]
# nodes = [0.0, 0.5, 0.75, 1.0]
# 
# py5_colormap = LinearSegmentedColormap.from_list(
#     'py5 example colormap',
#     list(zip(nodes, colors))
# )

def setup():
    py5.size(400, 400, py5.P2D)
    py5.stroke(255)
    py5.stroke_weight(3)
    py5.color_mode(py5.HSB)
    py5_tools.animated_gif('out.gif', count=120, period=0.1, duration=0.1)

def draw():
    global fx, fy
    py5.background('black')
    py5.translate(200, 200)
    scaled_pts = pts.copy()
    spx = scaled_pts[:, 0]
    spy = scaled_pts[:, 1]
    spx *= fx
    spy *= fy
    s = py5.create_shape()
    with s.begin_shape(py5.POINTS):
        s.vertices(scaled_pts)
    s.set_strokes(py5.color(((x + 64) + y) % 256, 255, 255) for x, y in  pts)
    py5.shape(s)
    
    if fx > 1:
        fx *= 0.9
    elif fy > 1:
        fy *= 0.9

py5.run_sketch()