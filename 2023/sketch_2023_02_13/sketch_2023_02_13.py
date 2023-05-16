import numpy as np
from random import shuffle

noise_increment = 0.005

def setup():
    global mesh_x, mesh_y, r_map, g_map, b_map
    size(500, 500)
    color_mode(HSB)
    cs = [color(int(h / 8) * 4 + 64, 128 + h / 2, 255)
           for h in range(256)]
    shuffle(cs)
    r_map = np.array([c >> 16 & 0xFF for c in cs])
    g_map = np.array([c >> 8 & 0xFF for c in cs])
    b_map = np.array([c & 0xFF for c in cs])
    mesh_x, mesh_y = np.meshgrid(
        np.arange(0, width * noise_increment, noise_increment),
        np.arange(0, height * noise_increment, noise_increment)
    )

def draw():    
    h = remap(os_noise(mesh_x, mesh_y, frame_count * noise_increment),
              -1, 1, 0, 255).astype(np.uint8)
    rgb = np.dstack((r_map[h], g_map[h], b_map[h]))
    set_np_pixels(rgb, bands="RGB")
    window_title(str(round(get_frame_rate(), 1)))
