import py5
import numpy as np

n_seed = 1
noise_scale = 0.003

def setup():
    global mesh_x, mesh_y, np_colors
    py5.size(600, 600)
#     reds = [py5.color(255 - a * 8, 0, a * 6) for a in range(32)]
#     yellows = [py5.color(255 - a * 8, 255 - a * 4, 0) for a in range(32)]
    reds = [py5.color(a * 8,  a * 2, 255 - a * 8) for a in range(32)]
    yellows = [py5.color(255 - a * 8, 255 - a * 4, a * 2) for a in range(32)]
    colors = (reds + yellows) * 5
    np_colors = np.dstack((
        [c >> 24 & 0xFF for c in colors],
        [c >> 16 & 0xFF for c in colors],
        [c >> 8 & 0xFF for c in colors],
        [c & 0xFF for c in colors]
        ))[0]
    mesh_x, mesh_y = np.meshgrid(
        np.arange(0, py5.width, 1) * noise_scale,
        np.arange(0, py5.height, 1) * noise_scale
    )
    py5.background(0)
    py5.load_np_pixels()

def draw():
    py5.os_noise_seed(n_seed)
    z = py5.mouse_x
    noise_values = py5.os_noise(mesh_x, mesh_y, z * noise_scale)
    idxs = py5.remap(noise_values, -1, 1, 0, len(np_colors)).astype(np.uint32)
    py5.set_np_pixels(np_colors[idxs], bands="ARGB")

def key_pressed():
    py5.save_frame('####.png')

py5.run_sketch()