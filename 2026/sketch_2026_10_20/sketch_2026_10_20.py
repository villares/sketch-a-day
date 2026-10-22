"""
Inspired by this sketch from Tom Larrow
https://codeberg.org/TomLarrow/creative-coding-experiments/src/branch/main/x_0000/x_0057
And NumPy examples from https://py5coding.org/how_tos/generate_noise_values.html
"""

import py5
import numpy as np

# How far apart the noise values will be. Lower numbers are more gradual
noise_increment = 0.01


def setup():
    global mesh_x, mesh_y, np_colors
    py5.size(400, 400)
    py5.color_mode(py5.HSB)
    colors = np.array([int(py5.color(i, 255, i))
                       for i in range(255)])
    np_colors = np.dstack(
        (
            [c >> 24 & 0xFF for c in colors],
            [c >> 16 & 0xFF for c in colors],
            [c >> 8 & 0xFF for c in colors],
            [c & 0xFF for c in colors],
        )
    )[0]

    # Builds two 2D arrays, mesh_x and mesh_y which have the dimensions of width x height
    # mesh_x has the values of the x position * noise_increment in the x direction, and is
    # duplicated for every y row, mesh_y has the values of the y position * noise_increment in the y
    # direction, and is duplicated for every x column
    mesh_x, mesh_y = np.meshgrid(
        np.arange(0, py5.width * noise_increment, noise_increment),
        np.arange(0, py5.height * noise_increment, noise_increment),
    )


def draw():
    py5.load_np_pixels()
    # The next line essentially loops through screen width and the screen height and
    # generates a value between 0 and 255 for each point. However because  we're passing
    # in the arrays mesh_x and mesh_y, it is generating an array output all at once instead
    # of calling os_noise over and over in a loop. This dramatically improves performance
    out = py5.remap(
        py5.os_noise(mesh_x, mesh_y, py5.frame_count * noise_increment), -1, 1, 0, 255
    )
    # Now that we have an array with the output, set the sketch's main canvas with it
    # The noise values are converted to int and used to index the color palette
    py5.set_np_pixels(np_colors[out.astype("int8")], bands="ARGB")
    # Write the framerate to the window tile to see the optimization effect
    py5.window_title(str(round(py5.get_frame_rate(), 1)))


def key_pressed():
    py5.save_frame('out.png') 

py5.run_sketch()
