import itertools

import py5
from py5_tools import animated_gif
import numpy as np

colors = []
positions = []
TS = 10  # triangle size
N = 5000  # number of positions
RS = 2 # amplitude of random movemnt

def setup():
    py5.size(400, 400, py5.P3D)
    py5.no_stroke()
    create_positions(N) 
    py5.profile_draw()
    animated_gif('out.gif', count=15, period=0.2, duration=0.2)

def create_positions(n):
    global positions, shp, colors    
    positions = np.array([
        (py5.random_int(py5.width),py5.random_int(py5.height))
        for _ in range(N)
    ])
    all_vertices = list(itertools.chain.from_iterable(
        ((rx, ry), (rx + TS, ry), (rx, ry + TS))
        for rx, ry in positions
        ))
    shp = py5.create_shape()
    shp.begin_shape(py5.TRIANGLES)
    shp.vertices(all_vertices)
    shp.end_shape()
    colors = []
    for i in range(N * 3):
        if i % 3 == 0:
            rc = py5.color(py5.random_int(32, 255),
                           py5.random_int(32, 255),
                           py5.random_int(32, 255))
        colors.append(rc)
    shp.set_fills(colors)

#def predraw_update():
def draw():

    global shp, positions
    # recreate shape
    rnd_offsets = np.random.randint(-RS, RS, size=(N, 2))
    positions += rnd_offsets
    positions %= 400, 400
    all_vertices = np.empty((N * 3, 2), dtype=positions.dtype)
    all_vertices[0::3] = positions             
    all_vertices[1::3] = positions + [TS, 0]   
    all_vertices[2::3] = positions + [0, TS] 
    shp = py5.create_shape()
    shp.begin_shape(py5.TRIANGLES)
    shp.vertices(all_vertices)
    shp.end_shape()
    shp.set_fills(colors)

# def draw():
    py5.background(0)    

#     # update shape
#     rnd_offsets = np.random.randint(-RS, RS, size=(N, 2))
#     positions += rnd_offsets
#     positions %= 400, 400
#     for i, (nx, ny) in enumerate(positions):
#         shp.set_vertex(i * 3, nx, ny)
#         shp.set_vertex(i * 3 + 1, nx + TS, ny)
#         shp.set_vertex(i * 3 + 2, nx, ny + TS)

    # draw shape
    py5.shape(shp)
    # show frame rate
    py5.window_title(f'{py5.get_frame_rate():.1f}')    

    if py5.frame_count == 1001:
        py5.print_line_profiler_stats()

py5.run_sketch()





