import py5
import numpy as np

noise_scale = 0.01

def setup():
    py5.size(400, 400, py5.P2D)
    py5.color_mode(py5.CMAP, 'viridis', 255)

def draw():
    py5.background('k')
    x_offset = py5.mouse_x

    rnd_shp = py5.create_shape()
    rnd_shp.begin_shape(py5.LINES)
    
    np.random.seed(1001)
    all_xs = np.arange(py5.width)
    random_ys = np.random.uniform(0, py5.height / 2, py5.width)
    base_ys = np.ones(py5.width) * py5.height / 2
    lines_array = np.column_stack([  # remember Y is flipped!
        all_xs,               # xa
        base_ys,              # ya (all start at height / 2)
        all_xs,               # xb (same as xa)
        base_ys - random_ys   # yb (the random ends)
    ])
    rnd_shp.vertices(lines_array.reshape(-1, 2))
    rnd_shp.end_shape()
    colors = py5.remap(random_ys, 0, py5.height / 2, 0, 255)
    rnd_shp.set_strokes([py5.color(c) for c in np.repeat(colors, 2)])
    py5.shape(rnd_shp)

    shp = py5.create_shape()
    shp.begin_shape(py5.LINES)

    all_xs = np.arange(py5.width)
    base_ys = np.ones(py5.width) * py5.height
    noise_values = py5.noise(x_offset + all_xs * noise_scale)
    noise_ys = py5.lerp(0, py5.height / 2, noise_values)
    lines_array = np.column_stack([ # remember Y is flipped!
        all_xs,             # xa
        base_ys,            # ya (all start at height)
        all_xs,             # xb (same as xa)
        base_ys - noise_ys  # yb (the noise end)
    ])
    shp.vertices(lines_array.reshape(-1, 2))
    shp.end_shape()
    colors = py5.remap(noise_values, 0, 1, 0, 255)
    shp.set_strokes([py5.color(c) for c in np.repeat(colors, 2)])
    py5.shape(shp)

def key_pressed():
    py5.save_frame('out####.png') 

py5.run_sketch()
