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
#     rnd_offsets = np.random.randint(-RS, RS, size=(len(triangles), 2))
#     for i, t in enumerate(triangles):
#         x, y = t[0]
#         # xo, yo = py5.random_int(-RS, RS), py5.random_int(-RS, RS)
#         xo, yo = rnd_offsets[i]
#         # nx, ny = (x + xo) % py5.width, (y + yo) % py5.height 
#         nx, ny = (x + xo) % 400, (y + yo) % 400     
#         t[:] = (nx, ny), (nx + TS, ny), (nx, ny + TS) 
#     all_vertices = list(itertools.chain.from_iterable(triangles))
#     shp = py5.create_shape()
#     shp.begin_shape(py5.TRIANGLES)
#     shp.vertices(all_vertices)
#     shp.end_shape()
#     shp.set_fills(colors)

    # update shape
    vertex_index = 0
    rnd_offsets = np.random.randint(-RS, RS, size=(len(triangles), 2))
    for i, t in enumerate(triangles):
        x, y = t[0]
        #xo, yo = py5.random_int(-RS, RS), py5.random_int(-RS, RS)
        xo, yo = rnd_offsets[i]
        #nx, ny = (x + xo) % py5.width, (y + yo) % py5.height 
        nx, ny = (x + xo) % 400, (y + yo) % 400     
        t[:] = (nx, ny), (nx + TS, ny), (nx, ny + TS)
        shp.set_vertex(vertex_index, nx, ny)
        shp.set_vertex(vertex_index + 1, nx + TS, ny)
        shp.set_vertex(vertex_index + 2, nx, ny + TS)
        vertex_index += 3

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

Total time: 15.47 s
File: /home/villares/GitHub/sketch-a-day/2026/sketch_2026_09_18/sketch_2026_09_18.py
Function: draw at line 37

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    37                                           def draw():
    38      6609 1105995112.0 167346.8      7.1      py5.background(240)    
    39                                               # update shape
    40      6609  602589723.0  91177.1      3.9      rnd_offsets = np.random.randint(-RS, RS, size=(len(triangles), 2))
    41    667509  426690336.0    639.2      2.8      for i, t in enumerate(triangles):
    42    660900  431473444.0    652.9      2.8          x, y = t[0]
    43                                                   # xo, yo = py5.random_int(-RS, RS), py5.random_int(-RS, RS)
    44    660900 1639815771.0   2481.2     10.6          xo, yo = rnd_offsets[i]
    45                                                   # nx, ny = (x + xo) % py5.width, (y + yo) % py5.height 
    46    660900  660588101.0    999.5      4.3          nx, ny = (x + xo) % 400, (y + yo) % 400     
    47    660900  819860899.0   1240.5      5.3          t[:] = (nx, ny), (nx + TS, ny), (nx, ny + TS) 
    48      6609  156422469.0  23668.1      1.0      all_vertices = list(itertools.chain.from_iterable(triangles))
    49      6609  456773426.0  69113.8      3.0      shp = py5.create_shape()
    50      6609  182590249.0  27627.5      1.2      shp.begin_shape(py5.TRIANGLES)
    51      6609 5187167985.0 784864.3     33.5      shp.vertices(all_vertices)
    52      6609  506066891.0  76572.4      3.3      shp.end_shape()
    53      6609  347752293.0  52618.0      2.2      shp.set_fills(colors)
    54                                           
    55                                               # update shape
    56                                           #     vertex_index = 0
    57                                           #     rnd_offsets = np.random.randint(-RS, RS, size=(len(triangles), 2))
    58                                           #     for i, t in enumerate(triangles):
    59                                           #         x, y = t[0]
    60                                           #         #xo, yo = py5.random_int(-RS, RS), py5.random_int(-RS, RS)
    61                                           #         xo, yo = rnd_offsets[i]
    62                                           #         #nx, ny = (x + xo) % py5.width, (y + yo) % py5.height 
    63                                           #         nx, ny = (x + xo) % 400, (y + yo) % 400     
    64                                           #         t[:] = (nx, ny), (nx + TS, ny), (nx, ny + TS)
    65                                           #         shp.set_vertex(vertex_index, nx, ny)
    66                                           #         shp.set_vertex(vertex_index + 1, nx + TS, ny)
    67                                           #         shp.set_vertex(vertex_index + 2, nx, ny + TS)
    68                                           #         vertex_index += 3
    69                                           
    70                                               # draw shape
    71      6609 2946237902.0 445791.8     19.0      py5.shape(shp)
"""
