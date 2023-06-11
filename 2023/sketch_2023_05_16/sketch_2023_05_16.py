import numpy as np
from random import shuffle

noise_increment = 0.005
img_txt = None

def setup():
    global mesh_x, mesh_y, rgb_map, s
    size(500, 500, P3D)
    no_stroke()
    s = create_shape(SPHERE, 100)
    s.set_ambient("#FF0000")

    color_mode(HSB)
    cs = [color(h / 2 + 64, 128 + h / 2, 255)
           for h in range(256)]
    color_mode(RGB)
    shuffle(cs)
    rgb_map =  np.dstack(np.broadcast_arrays(
        [c >> 16 & 0xFF for c in cs],
        [c >> 8 & 0xFF for c in cs],
        [c & 0xFF for c in cs]
        )).astype(np.uint8)[0]

    mesh_x, mesh_y = np.meshgrid(
        np.arange(0, width * noise_increment, noise_increment),
        np.arange(0, height * noise_increment, noise_increment)
    )

def draw():
    global img_txt
    background(0)
    lights()
    point_light(255, 255, 255, 0, 0, 500 * sin(frame_count / 20))
    h = remap(os_noise(mesh_x, mesh_y, frame_count * noise_increment),
              -1, 1, 0, 255).astype(np.uint8)
    npa = rgb_map[h]
    img_txt = create_image_from_numpy(npa, bands="RGB", dst=img_txt)
    #image(img_txt, 0, 0)
    
    s.set_texture(img_txt)
    shape(s, 350, 350)
    #window_title(str(round(get_frame_rate(), 1)))
    
