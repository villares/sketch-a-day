
add_library('serial')
add_library('arduino')
from inputs import Slider

def setup():
    size(512, 512)
    Slider.create_defaults(Arduino)
    
def draw():
    background(0)
    v0 = Slider.get_val(0) / 2
    v1 = Slider.get_val(1) / 2
    v2 = Slider.get_val(2) / 2
    v3 = Slider.get_val(3) / 2
    rectMode(CENTER)
    fill(255, 100)
    rect(256, 256, v0, v1)
    ellipse(256, 256, v2, v3)
    Slider.update_all()

    
    
    
