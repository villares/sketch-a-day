import py5
import numpy as np

noise_increment = 0.005

def setup():
    global mesh_x, mesh_y, rgb_map, g_map, b_map, cs
    py5.size(500, 500)
    py5.color_mode(py5.HSB)
    cs = [
        py5.color('orange'),
        py5.color('red'),
        # py5.color('white'),
        ]  # you could add more color bands...
    rgb_map =  np.dstack((
        [c >> 16 & 0xFF for c in cs],
        [c >> 8 & 0xFF for c in cs],
        [c & 0xFF for c in cs]
        ))[0]

    mesh_x, mesh_y = np.meshgrid(
        np.arange(0, py5.width * noise_increment, noise_increment),
        np.arange(0, py5.height * noise_increment, noise_increment)
    )

def draw():    
    h = py5.remap(py5.os_noise(mesh_x, mesh_y, py5.frame_count * noise_increment),
              -1, 1, 0, len(cs)).astype(np.uint8)
    npa = rgb_map[h]
    py5.set_np_pixels(npa, bands="RGB")
    py5.window_title(str(round(py5.get_frame_rate(), 1)))
    
py5.run_sketch()