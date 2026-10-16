import numpy as np
import py5

n_seed = 1
noise_scale = 0.005


def setup():
    global mesh_x, mesh_y
    py5.size(600, 600)
    py5.os_noise_seed(n_seed)
    mesh_x, mesh_y = np.meshgrid(
        np.arange(0, py5.width, 1) * noise_scale,
        np.arange(0, py5.height, 1) * noise_scale,
    )

def draw():
    py5.background(0)
    pixels_array = py5.get_np_pixels()

    noise_for_R = py5.os_noise(mesh_x, mesh_y, py5.mouse_x * noise_scale)
    pixels_array[:, :, 1] = py5.remap(noise_for_R, -1, 1, 0, 255)

#     noise_for_B = py5.os_noise(mesh_x, mesh_y, py5.mouse_y * noise_scale)
#     pixels_array[:, :, 3] = py5.remap(noise_for_B, -1, 1, 0, 255)

    py5.set_np_pixels(pixels_array)

def key_pressed():
    py5.save_frame("####.png")


py5.run_sketch()
