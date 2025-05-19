"""
Couldm't make the Picking library work well with PeasyCam...
also: OpenGL error 1282 at top endDraw(): invalid operation
"""
import py5_tools
print(py5_tools.processing.download_library("PeasyCam"))
print(py5_tools.processing.download_library("Picking"))


from itertools import product    

import py5
 
from peasy import PeasyCam   # the only tricky part is to find the module name!
from picking import Picker

cubes = []

def setup():
    global cam, picker
    py5.size(512, 512, py5.P3D)
    this_sketch = py5.get_current_sketch()
    
#     cam = PeasyCam(this_sketch, 400)
#     cam.setMinimumDistance(300)
#     cam.setMaximumDistance(500)    
#     orbit_handler = cam.getRotateDragHandler() # get the RotateDragHandler
#     pan_handler = cam.getPanDragHandler()      # get the PanDragHandler
#     cam.setCenterDragHandler(orbit_handler)    # set the orbit handler to the Center/Wheel drag
#     cam.setRightDragHandler(pan_handler)       # set the pan handler to the right-button mouse drag
#     cam.setLeftDragHandler(None)      # remove orbit from the left mouse button
    
    picker = Picker(this_sketch)

    cs = 64  # cell size
    for i, j, k in product(range(-2, 3), repeat=3):
        cubes.append(Cube(i * cs, j * cs, k * cs))

def draw():
    py5.background(255)
    py5.translate(py5.width / 2, py5.height / 2) # disable if trying PeasyCam
    for i, cube in enumerate(cubes):
        picker.start(i)        
        cube.draw()
        #picker.stop()
   
def mouse_clicked():
  i = picker.get(py5.mouse_x, py5.mouse_y)
  if i >= 0:
      cubes[i].clicked()
  

class Cube:
    
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        self.size = py5.random_choice((8, 32))
        self.on = False
        
    def draw(self):
        py5.fill(128 - self.on * 128, self.on * 255, 255)
        with py5.push_matrix():
            py5.translate(self.x, self.y, self.z)
            py5.box(self.size)

    def clicked(self):
        self.on = not self.on

py5.run_sketch(block=False)

