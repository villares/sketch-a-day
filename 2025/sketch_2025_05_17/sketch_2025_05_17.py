"""
This is new on py5 version 0.10.5a. Run the following lines before importing py5,
and it will add Processing's PeasyCam by Jonathan Feinberg to py5.
https://mrfeinberg.com/peasycam/ "Dead-simple mouse-driven camera for Processing" 
"""
import py5_tools
print(py5_tools.processing.download_library("PeasyCam"))

from itertools import product    

import py5
# 
from peasy import PeasyCam 

def setup():
    global cam 
    py5.size(512, 512, py5.P3D)
    this_sketch = py5.get_current_sketch()
    cam = PeasyCam(this_sketch, 400)
    cam.setMinimumDistance(300);
    cam.setMaximumDistance(500);

def draw():
    py5.background(0)
    py5.color_mode(py5.HSB)
    py5.random_seed(1)
    cs = 32
    for i, j, k in product(range(-3, 4), repeat=3):
        x, y, z = i * cs, j * cs, k * cs 
        bs = py5.random_choice((4, 8, 16, 32))
        py5.fill(bs * 4, 255, 150)
        with py5.push_matrix():
            py5.translate(x,  y, z)
            py5.box(bs)
            
    cam.beginHUD()
    py5.fill(255)
    py5.text_size(20)
    py5.text('PeasyCam demo', 15, 15)
    cam.endHUD()
   
   
py5.run_sketch(block=False)
