"""
Experiments based on Tom Larrow's py5 noise + numpy explorations: 
https://codeberg.org/TomLarrow/creative-coding-experiments/raw/branch/main/x_0057/x_0057.py
"""

import numpy as np

noise_increment = 0.01

def setup():
    global img, mesh_x, mesh_y
    size(640, 360)
    mesh_x, mesh_y = np.meshgrid(
        np.arange(0, width * noise_increment, noise_increment),
        np.arange(0, height * noise_increment, noise_increment)
    )

def draw():    
    R = remap(os_noise(mesh_x, mesh_y, frame_count * noise_increment), -1, 1, 0, 255)
    G = remap(os_noise(mesh_x, mesh_y, (10 + frame_count) * noise_increment), -1, 1, 0, 255)
    B = remap(os_noise(mesh_x, mesh_y, (-10 + frame_count) * noise_increment), -1, 1, 0, 255)
#     npa = np.zeros((height, width, 3), dtype=np.uint8)
#     npa[:, :, 0] = R
#     npa[:, :, 1] = G
#     npa[:, :, 2] = B
    npa = np.dstack((R, G, B))
     
    set_np_pixels(npa, bands="RGB")
    window_title(str(round(get_frame_rate(), 1)))
    
    
    
@np.vectorize
def vred(c):
    return c >> 16 & 0xFF 

@np.vectorize
def vgreen(c):
    return c >> 8 & 0xFF 

@np.vectorize
def vblue(c):
    return c & 0xFF 

