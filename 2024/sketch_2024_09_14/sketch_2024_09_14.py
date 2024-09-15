"""
trimesh.creation.icosphere(
    subdivisions: int | integer | unsignedinteger = 3,
    radius: float | floating | int | integer | unsignedinteger = 1.0,
    **kwargs)
# 'Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r',
# 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2',
# 'Dark2_r', 'GnBu', 'GnBu_r', 'Grays', 'Greens', 'Greens_r', 'Greys',
'Greys_r',
'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired',
'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG',
'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r',
'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_grey', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gist_yerg', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'grey', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight',
'twilight_r', 'twilight_shifted', 'twilight_shifted_r',
    'viridis', 'viridis_r', 'winter', 'winter_r'
"""

import py5
import trimesh
import numpy as np

Z_OFFSET = -200
R = 300

def setup():
    global icosphere, ico
    py5.size(600, 600, py5.P3D)
#    cs = [trimesh.visual.color.random_color() for _ in range(5120)]
#     cs = trimesh.visual.color.interpolate(np.linspace(0, 1, 5120),
#                                           #color_map='twilight_shifted'
#                                           )
#    icosphere = trimesh.creation.icosphere(4, R, face_colors=cs)
#     cs = [trimesh.visual.color.random_color() for _ in range(2562)]
    icosphere = trimesh.creation.icosphere(4, R,
#                                            #vertex_colors=cs
                                            )
    pts = trimesh.PointCloud(icosphere.vertices)
    py5.stroke_weight(3)
    ico = py5.convert_cached_shape(pts)
#     cs = [py5.color(py5.random_int(128, 255),
#                     py5.random_int(128, 255),
#                     py5.random_int(128, 255))
#           for _ in range(2562)]
    cs = [py5.color(abs(x), abs(y), abs(z))
          for x, y, z in icosphere.vertices]
    ico.set_strokes(cs)
 
#def draw():
    py5.background(0)
    py5.lights()
    py5.translate(py5.width / 2, py5.height / 2, Z_OFFSET)
    #py5.stroke(255)

    py5.shape(ico)
#     py5.translate(py5.width / 2, 0, 0)
#     py5.sphere(R)
    py5.save('out.png')

py5.run_sketch(block=False)
