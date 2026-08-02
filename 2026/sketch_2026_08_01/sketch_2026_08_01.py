import py5
from py5_tools import animated_gif

import numpy as np
import trimesh

import io

ds = """o Durers_Solid, courtesy of João Antonio <introscopia.github.io>
v 0.000000 -0.719944 0.347016
v 0.000000 -0.411397 0.644458
v -0.356280 0.205698 0.644458
v -0.623490 0.359972 0.347016
v -0.623490 -0.359972 -0.347016
v 0.000000 0.719944 -0.347016
v 0.000000 0.411397 -0.644458
v -0.356280 -0.205698 -0.644458
v 0.623490 -0.359972 -0.347016
v 0.356280 -0.205698 -0.644458
v 0.623490 0.359972 0.347016
v 0.356280 0.205698 0.644458
s 0
f 3 4 5 1 2
f 8 5 4 6 7
f 7 6 11 9 10
f 2 1 9 11 12
f 10 9 1 5 8
f 12 11 6 4 3
f 8 7 10
f 12 3 2
"""

mesh = trimesh.load(io.StringIO(ds), file_type='obj')

faces_in_facets = np.zeros(len(mesh.faces), dtype=bool)
for facet in mesh.facets:
    faces_in_facets[facet] = True
single_triangle_faces = np.nonzero(~faces_in_facets)[0]

face_groups = [*mesh.facets, *single_triangle_faces[:, None]]
for face_group in face_groups:
    mesh.visual.face_colors[face_group] = trimesh.visual.random_color()

def setup():
    py5.size(600, 600, py5.P3D)
    py5.no_smooth()
    animated_gif('out.gif', frame_numbers=range(1, 181, 4), duration=0.15)

def draw():
    py5.background('black')
    py5.lights()
    py5.translate(py5.width / 2, py5.height / 2, 0)
    py5.scale(200)
    py5.rotate_y(py5.radians(py5.frame_count * 2))
    py5.rotate_x(py5.radians(py5.frame_count * 4))
    py5.shape(mesh)

def key_pressed():
    if py5.key == 's':
        py5.save_frame('#####.png')

py5.run_sketch(block=False)
