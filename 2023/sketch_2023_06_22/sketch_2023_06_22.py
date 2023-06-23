"""
Based on x_0073 by Tom Larrow
https://codeberg.org/TomLarrow/creative-coding-experiments/src/branch/main/x_0073/x_0073.py
"""

import numpy as np
import py5


def setup():
    """py5 setup block. This runs once at the start"""
    py5.size(800, 800)
    py5.no_loop()


def draw():
 
 
    # Draw 4 more layers on top of this background, each one uses a different noise pattern and different alpha
    # to combine everything in one
    for i in range(1, 5):
        layer = py5.create_graphics(py5.width, py5.height)
        layer.begin_draw()
        layer.color_mode(py5.HSB)
        # Desaturate the colors that make up the background so that it looks like a background and isn't too bold
        c = layer.color(i * 16,
                        200,
                        255)
        layer.background(c)
        layer.end_draw()
        layer.load_np_pixels()
        # Replace the alpha values with the noise values. Each subsequent color is remapped less and less so that
        # it has less alpha
        layer.np_pixels[:, :, 0] = py5.remap(
            py5.os_noise(py5.width, py5.height,
                         0.0003 * i + 0.002, 12,
                         50 * i,
                         50 * i),
            -1, 1, 0, 255 - (20 * i))
        layer.update_np_pixels()
        py5.image(layer, 0, 0)

    # Draw a circle with vertical lines masked out of it, this was PAINFUL, there has to be a better way.

    # First we define our circle that we want to display in the color we want
    top_layer = py5.create_graphics(py5.width, py5.height)
    top_layer.begin_draw()
    top_layer.no_stroke()
    top_layer.fill(palette[-1])
    top_layer.circle(py5.width/2, py5.width/2, py5.width * 0.75)
    top_layer.end_draw()

    # Next we define a white background with black lines, we want the above circle to appear where things are white
    mask_layer_2 = py5.create_graphics(py5.width, py5.height)
    mask_layer_2.begin_draw()
    mask_layer_2.background(255)
    mask_layer_2.stroke_weight(18)
    mask_layer_2.stroke(0)
    for i in np.linspace(start=0, stop=py5.width, num=15):
        mask_layer_2.line(i, 0, i, py5.height)
    mask_layer_2.end_draw()

    # When I first did top_layer.mask(mask_layer_2) it generated the colored lines in the circle as I expected,
    # but it also showed the original black lines above and below the circle. As this was not what was desired it
    # seemed that I had to mask my mask to get what I was trying to achieve
    # So we build another mask which is a circle, just like the original top_layer except this is just white
    mask_layer_3 = py5.create_graphics(py5.width, py5.height)
    mask_layer_3.begin_draw()
    mask_layer_3.no_stroke()
    mask_layer_3.fill(255)
    mask_layer_3.circle(py5.width / 2, py5.width / 2, py5.width * 0.75)
    mask_layer_3.end_draw()

    # We then have to mask mask_layer_2 with mask_layer_3
    mask_layer_2.mask(mask_layer_3)

    # Then it seems we have to write this mask of a mask to an additional layer
    # so that it can be a mask for the top layer
    mask_layer = py5.create_graphics(py5.width, py5.height)
    mask_layer.begin_draw()
    mask_layer.image(mask_layer_2, 0, 0)
    mask_layer.end_draw()

    # Now that we have mask_layer, which is mask_layer_2 masked by mask_layer_3, we can use it to mask the top layer
    top_layer.mask(mask_layer)
    py5.image(top_layer, 0, 0)

    # There has to be a much better way to do the above, please help me

    py5.save_frame("x_0073.png")


py5.run_sketch()