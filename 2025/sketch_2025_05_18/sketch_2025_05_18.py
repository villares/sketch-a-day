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

def setup():
    global cam, picker_map, previous_pixels
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
    cam.setLeftDragHandler(None)      # remove orbit from the left mouse button
    picker_map = np.empty((py5.height, py5.width), dtype=np.short) 
    cs = 100  # cell size
    for i, j, k in product(range(-1, 2), repeat=3):
        cubes.append(Cube(i * cs, j * cs, k * cs))
    previous_pixels = None

def draw():
    global previous_pixels
    py5.background(0)
    picker_map.fill(-1)
    previous_pixels = py5.get_np_pixels(dst=previous_pixels)
    current_pixels = np.empty_like(previous_pixels)
    for cube_index, cube in enumerate(cubes):
        cube.draw()
        py5.get_np_pixels(dst=current_pixels)
        mask = np.any(previous_pixels != current_pixels, axis=-1)
        picker_map[mask] = cube_index
        previous_pixels[:] = current_pixels
    
def mouse_clicked():
    if py5.mouse_button == py5.LEFT:
        cube_index = picker_map[py5.mouse_y, py5.mouse_x]
        if cube_index >= 0:
           cubes[cube_index].clicked()
      
      
class Cube:
    
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        self.on = py5.random_choice((True, False))
        self.color = py5.random_int(126) * 2
        
    def draw(self):
        if self.on:
            py5.fill(self.color, 255, 255)
        else:
            py5.fill(128 + self.color / 2)
        with py5.push_matrix():
            py5.translate(self.x, self.y, self.z)
            py5.box(100 - self.on * 50)

    def clicked(self):
        self.on = not self.on

py5.run_sketch(block=False)

