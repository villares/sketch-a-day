import numpy as np
import py5
from py5_tools import animated_gif
from skimage import measure

n_seed = 1
noise_scale = 0.01


def setup():
    global mesh_x, mesh_y
    py5.size(400, 400)
    py5.os_noise_seed(n_seed)
    mesh_x, mesh_y = np.meshgrid(
        np.arange(0, py5.width, 1) * noise_scale,
        np.arange(0, py5.height, 1) * noise_scale,
    )
    animated_gif('out.gif',
                  frame_numbers=range(1, 361, 6),
                  duration=0.15
                  )
    global pixels_array
    pixels_array = py5.get_np_pixels()


def draw():
    #py5.background(255)
    #py5.load_np_pixels()
    #print(pixels_array.shape)
    delta = 0.05
    t = py5.radians(py5.frame_count)
    k = py5.sin(t) * 1
    w = py5.cos(t) * 1
    noise_for_R = py5.os_noise(mesh_x, mesh_y, delta * 1 + k, w)
    noise_for_G = py5.os_noise(mesh_x, mesh_y, delta * 2 + k, w)
    noise_for_B = py5.os_noise(mesh_x, mesh_y, delta * 3 + k, w)
    pixels_array[:, :, 1] = py5.remap(noise_for_R, -1, 1, 0, 255)
    pixels_array[:, :, 2] = py5.remap(noise_for_G, -1, 1, 0, 255)
    pixels_array[:, :, 3] = py5.remap(noise_for_B, -1, 1, 0, 255)
    pixels_array[pixels_array[:, :, :] < 128] = 255
    py5.set_np_pixels(pixels_array) 

def key_pressed():
    py5.save_frame("####.png")


py5.run_sketch()
