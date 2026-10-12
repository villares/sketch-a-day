import py5
import numpy as np

noise_scale = 0.012

def setup():
    py5.size(600, 400, py5.P2D)
    py5.color_mode(py5.CMAP, 'magma', 255)

def draw():
    py5.background('k')
    x_offset = py5.mouse_x * 0.1

    os_shp = py5.create_shape()
    os_shp.begin_shape(py5.LINES)
    
    all_xs = np.arange(py5.width)
    base_ys = np.ones(py5.width) * py5.height / 2
    os_noise_values = py5.os_noise(x_offset + all_xs * noise_scale, 1)
    noise_ys = py5.remap(os_noise_values, -1, 1, 0, py5.height / 2)

    lines_array = np.column_stack([  # remember Y is flipped!
        all_xs,               # xa
        base_ys,              # ya (all start at height / 2)
        all_xs,               # xb (same as xa)
        base_ys - noise_ys   # yb (the random ends)
    ])
    os_shp.vertices(lines_array.reshape(-1, 2))
    os_shp.end_shape()
    colors = py5.remap(noise_ys, 0, py5.height / 2, 0, 255)
    os_shp.set_strokes([py5.color(c) for c in np.repeat(colors, 2)])
    py5.shape(os_shp)

    shp = py5.create_shape()
    shp.begin_shape(py5.LINES)

    all_xs = np.arange(py5.width)
    base_ys = np.ones(py5.width) * py5.height
    os_noise_values = py5.os_noise(x_offset + all_xs * noise_scale,
                                   #py5.mouse_y * noise_scale,
                                   1
                                   )
    o2_noise_values = py5.os_noise(x_offset + all_xs * noise_scale,
                                   #py5.mouse_y * noise_scale,
                                   3
                                   )
    os_noise_values = os_noise_values * o2_noise_values
    noise_ys = py5.remap(os_noise_values, -0.66, 0.66, 0, py5.height / 2)
    lines_array = np.column_stack([ # remember Y is flipped!
        all_xs,             # xa
        base_ys,            # ya (all start at height)
        all_xs,             # xb (same as xa)
        base_ys - noise_ys  # yb (the noise end)
    ])
    shp.vertices(lines_array.reshape(-1, 2))
    shp.end_shape()
    colors = py5.remap(os_noise_values, -1, 1, 0, 255)
    shp.set_strokes([py5.color(c) for c in np.repeat(colors, 2)])
    py5.shape(shp)

def key_pressed():
    py5.save_frame('out####.png') 

py5.run_sketch()
