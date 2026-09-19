import itertools

import py5
import numpy as np

colors = []
triangles = []
TS = 20  # triangle size
N = 1000  # number of triangles
RS = 2 # amplitude of random movemnt

def setup():
    py5.size(400, 400, py5.P3D)
    py5.no_stroke()
    create_triangles(N) 
    py5.profile_draw()

def create_triangles(n):
    global triangles, shp, colors    
    triangles = []
    for _ in range(n):
        rx = py5.random_int(py5.width)
        ry = py5.random_int(py5.height)
        triangles.append([(rx, ry), (rx + 10, ry), (rx, ry + 10)])
    
    all_vertices = list(itertools.chain.from_iterable(triangles))
    shp = py5.create_shape()
    shp.begin_shape(py5.TRIANGLES)
    shp.vertices(all_vertices)
    shp.end_shape()
    colors = [py5.color(py5.random_int(255),
                        py5.random_int(255),
                        py5.random_int(255)) 
              for triangle in triangles for _ in range(3)]
    shp.set_fills(colors)

def draw():
    py5.background(240)    
    # recreate shape
    rnd_offsets = np.random.randint(-RS, RS, size=(N, 2))
    for i, t in enumerate(triangles):
        x, y = t[0]
        # xo, yo = py5.random_int(-RS, RS), py5.random_int(-RS, RS)
        xo, yo = rnd_offsets[i]
        # nx, ny = (x + xo) % py5.width, (y + yo) % py5.height 
        nx, ny = (x + xo) % 400, (y + yo) % 400     
        t[:] = (nx, ny), (nx + TS, ny), (nx, ny + TS) 
    all_vertices = list(itertools.chain.from_iterable(triangles))
    shp = py5.create_shape()
    shp.begin_shape(py5.TRIANGLES)
    shp.vertices(all_vertices)
    shp.end_shape()
    shp.set_fills(colors)

    # update shape
#     vertex_index = 0
#     rnd_offsets = np.random.randint(-RS, RS, size=(N, 2))
#     for i, t in enumerate(triangles):
#         x, y = t[0]
#         #xo, yo = py5.random_int(-RS, RS), py5.random_int(-RS, RS)
#         xo, yo = rnd_offsets[i]
#         #nx, ny = (x + xo) % py5.width, (y + yo) % py5.height 
#         nx, ny = (x + xo) % 400, (y + yo) % 400     
#         t[:] = (nx, ny), (nx + TS, ny), (nx, ny + TS)
#         shp.set_vertex(vertex_index, nx, ny)
#         shp.set_vertex(vertex_index + 1, nx + TS, ny)
#         shp.set_vertex(vertex_index + 2, nx, ny + TS)
#         vertex_index += 3

    # draw shape
    py5.shape(shp)
    # show frame rate
    py5.window_title(f'{py5.get_frame_rate():.1f}')    

def key_pressed():
    if py5.key == 'p':
        py5.print_line_profiler_stats()
    elif py5.key == 's':
        py5.save_frame('####.png')

py5.run_sketch()

"""
Timer unit: 1e-09 s
"""
