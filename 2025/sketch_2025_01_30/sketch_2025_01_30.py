import py5
import numpy as np

noise_increment = 0.003

def setup():
    global mesh_x, mesh_y, rgba_map, rgbb_map
    py5.size(500, 500)
    py5.color_mode(py5.HSB)
    csa = [py5.color(255) if i % 8 else py5.color(i % 255, 200, 200)
          for i in range(512)]

#     csb = [py5.color(i % 255, 200, 200)
#           for i in range(512)]

    rgba_map = colors_to_colorarray(csa)
#     rgbb_map = colors_to_colorarray(csb)
    
    mesh_x, mesh_y = np.meshgrid(
        np.arange(0,  py5.width * noise_increment, noise_increment),
        np.arange(0,  py5.height * noise_increment, noise_increment)
    )

def draw():
    py5.rect(0, 0, 500, 500)
    osna = py5.os_noise(mesh_x + py5.mouse_x * noise_increment,
                       mesh_y + py5.mouse_y * noise_increment,
                       py5.frame_count * noise_increment)
#     osnb = py5.os_noise(1000 + mesh_x + py5.mouse_x * noise_increment,
#                         1000 + mesh_y + py5.mouse_y * noise_increment,
#                         1000 + py5.frame_count * noise_increment)    
#     color_indices = py5.remap(osnb, -1, 1, 0, len(osnb) - 1).astype(np.uint8)
#     npb = rgbb_map[color_indices]
#     py5.set_np_pixels(npb, bands="RGBA")

    color_indices = py5.remap(osna, -1, 1, 0, len(osna) - 1).astype(np.uint8)
    npa = rgba_map[color_indices]
    py5.set_np_pixels(npa, bands="RGBA")
    py5.window_title(str(round(py5.get_frame_rate(), 1)))
    
    
def colors_to_colorarray(color_list):
    return np.dstack((
        [c >> 16 & 0xFF for c in color_list],
        [c >> 8 & 0xFF for c in color_list],
        [c & 0xFF for c in color_list],
        [0 if c == 255 else 255 for c in color_list], # note 255 is not a color...
        ))[0]  # it serves as a sentinel value for

def key_pressed():
    py5.save('out.png')
    
py5.run_sketch(block=False)