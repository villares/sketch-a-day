"""
This needs py5 version 0.10.5a or greater.
"""
# # Run the following lines before importing py5, and it will add Processing's PeasyCam by Jonathan Feinberg to py5.
# # https:#mrfeinberg.com/peasycam/ "Dead-simple mouse-driven camera for Processing" 
# import py5_tools  
# print(py5_tools.processing.download_library("PeasyCam"))  # need to be done just once

from itertools import product    

import py5
from peasy import PeasyCam  # must be imported after import py5
import numpy as np

cubes = []
update_picker = True
cs = 100  # max cube size

def setup():
    global cam, picker_map, current_pixels, previous_pixels
    py5.size(512, 512, py5.P3D)
    py5.color_mode(py5.HSB)
    
    this_sketch = py5.get_current_sketch()
    cam = PeasyCam(this_sketch, 500)
    cam.setMinimumDistance(400)
    cam.setMaximumDistance(600)    
    orbit_handler = cam.getRotateDragHandler() # get the RotateDragHandler
    pan_handler = cam.getPanDragHandler()      # get the PanDragHandler
    cam.setCenterDragHandler(orbit_handler)    # set the orbit handler to the Center/Wheel drag
    cam.setRightDragHandler(pan_handler)       # set the pan handler to the right-button mouse drag
    #cam.setLeftDragHandler(None)      # remove orbit from the left mouse button
    
    picker_map = np.empty((py5.height, py5.width), dtype=int)
    picker_map.fill(-1)
    previous_pixels = py5.get_np_pixels()
    current_pixels = np.empty_like(previous_pixels)
    setup_cubes()

def setup_cubes():
    cubes.clear()
    for cube_index, (i, j, k) in enumerate(product(range(-1, 2), repeat=3)):
        cubes.append(Cube(i * cs, j * cs, k * cs, cube_index))
    
def draw():
    global update_picker
    try:
        mouse_over = picker_map[py5.mouse_y, py5.mouse_x]
    except IndexError:
        mouse_over = -1
    if update_picker:
        picker_map.fill(-1)
        for cube in cubes:
            cube.update_picker_map()
        update_picker = False  # I'm not sure about this "auto-off update"
    py5.background(0)
    for cube in cubes:
        cube.draw(mouse_over)
    py5.window_title(str(round(py5.get_frame_rate())))
        
def mouse_clicked():
    if py5.mouse_button == py5.LEFT:
        mouse_over = picker_map[py5.mouse_y, py5.mouse_x]
        if mouse_over >= 0:
           cubes[mouse_over].clicked()

def mouse_dragged():
    global update_picker
    update_picker = False

def mouse_released():
    global update_picker
    update_picker = True

# def mouse_wheel():
#     global update_picker
#     update_picker = True

def key_pressed():
    if py5.key == ' ':
        setup_cubes()

class Cube:
    
    def __init__(self, x, y, z, cube_index):
        self.x, self.y, self.z = x, y, z
        self.core = py5.random_choice((True, False))
        self.color = py5.random_int(127) * 2
        self.cube_index = cube_index
                
    def draw(self, mouse_over=-1):
        # show pre-selection hover only when there is no drag / mouse pressed
        if not py5.is_mouse_pressed:
            hover = (self.cube_index == mouse_over)
        else:
            hover = False 
        py5.stroke(hover * 255)
        py5.fill(self.color, 255, 255, 255 - hover * 150)
        self.draw_box(50)
        if not self.core:
            py5.fill(200, 255 - hover * 150)
            self.draw_box(100)
        
    def draw_box(self, s=None):
        s = s or (100 - self.core * 50)
        with py5.push_matrix():
            py5.translate(self.x, self.y, self.z)
            py5.box(s)

    def update_picker_map(self):
        py5.get_np_pixels(dst=previous_pixels) 
        py5.fill(10)
        py5.no_stroke()
        self.draw_box()
        py5.get_np_pixels(dst=current_pixels)
        mask = np.any(previous_pixels != current_pixels, axis=-1)
        picker_map[mask] = self.cube_index

    def clicked(self):
        global update_picker
        self.core = not self.core
        update_picker = True  # if I use the auto-off update, this helps

py5.run_sketch(block=False)

