import py5
import numpy as np

noise_increment = 0.003

def setup():
    global mesh_x, mesh_y, rgba_map, rgbb_map
    py5.size(500, 500)
#    py5.color_mode(py5.HSB)
    csa = [py5.color(128, 0, 0) if i % 8 == 0 else 
           py5.color(i)
           for i in range(256)]


    rgba_map = colors_to_colorarray(csa)
    
    mesh_x, mesh_y = np.meshgrid(
        np.arange(0,  py5.width * noise_increment, noise_increment),
        np.arange(0,  py5.height * noise_increment, noise_increment)
    )

def draw():
    global sa, npa
    py5.rect(0, 0, 500, 500)
    osna = py5.os_noise(mesh_x + py5.mouse_x * noise_increment,
                       mesh_y + py5.mouse_y * noise_increment,
                       py5.frame_count * noise_increment)

    color_indices = py5.remap(osna, -1, 1, 0, len(osna) - 1).astype(np.uint8)
    npa = rgba_map[color_indices]
    sa = sort_columns(npa)
    py5.set_np_pixels(sa, bands="RGBA")
    py5.window_title(str(round(py5.get_frame_rate(), 1)))
    
    
def colors_to_colorarray(color_list):
    return np.dstack((
        [c >> 16 & 0xFF for c in color_list],
        [c >> 8 & 0xFF for c in color_list],
        [c & 0xFF for c in color_list],
        [0 if c == 255 else 255 for c in color_list], # note 255 is not a color...
        ))[0]  # it serves as a sentinel value for

def sort_pixels_lexicographic(image_array):
    global sorted_structured
    # same as reshape (height*width, 4)
    flat_image = image_array.reshape(-1, 4)    
    dtype = [('R', int), ('G', int), ('B', int), ('A', int)]
    structured = np.array([tuple(row) for row in flat_image], dtype=dtype)    
    sorted_structured = np.sort(structured, order=['R', 'G', 'B', 'A'])
    sorted_flat = np.array([tuple(pixel) for pixel in sorted_structured])
    return sorted_structured.reshape(image_array.shape)


def sort_columns(image_array):    
    #image_array = np.asarray(image_array, dtype=np.uint8)
    rows, cols, _ = image_array.shape
    dtype = [('R', np.uint8), ('G', np.uint8), ('B', np.uint8), ('A', np.uint8)]
    structured = np.array([tuple(p) for p in image_array.reshape(-1, 4)], dtype=dtype)
    sorted_structured = np.sort(structured.reshape(rows, cols), axis=0)
    return np.stack([sorted_structured[f] for f in ['R', 'G', 'B', 'A']], axis=-1)
    

def key_pressed():
    py5.save_frame('out###.png')
    
py5.run_sketch(block=False)
