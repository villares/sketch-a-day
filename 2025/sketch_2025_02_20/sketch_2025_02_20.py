# Based on an example by @vsquared from this discussion:
# https://github.com/py5coding/py5generator/discussions/606#discussioncomment-12267883

import py5
import py5_tools
# on module mode you have to import py5 before other Java based libraries.
from controlP5 import ControlP5  # jars on jars sub-directory

def setup():
    py5.size(500, 500, py5.P3D)
    global slider
    global picker
    #py5.hint(py5.ENABLE_DEPTH_SORT)
    #py5.hint(py5.ENABLE_DEPTH_TEST)
    py5.window_title("3D Demo")
    cp5 = ControlP5(py5.get_current_sketch())
    slider = cp5.addSlider("slider", 0, 255, 150, 30, 10, 200, 20)
    picker = cp5.addColorPicker("picker", 270, 10, 100, 20)
    picker.setColorValue(py5.color(50, 155, 110))
    step = 15
    # This works but doesn't record the widgets! (can be useful!)
    #py5_tools.animated_gif(f'out.gif', duration=0.1, frame_numbers=range(1, 360, step))

def draw():
    py5.background(209)
    py5.lights()
    s = slider.getValue()
    c = picker.getColorValue()
    with py5.push_matrix():
        py5.translate(py5.width / 2, py5.height / 2)
        py5.rotate_y(py5.radians(py5.frame_count))
        py5.fill(c)
        py5.box(s)

py5.run_sketch()