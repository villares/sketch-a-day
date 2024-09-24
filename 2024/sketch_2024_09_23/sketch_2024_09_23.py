import trimesh
import py5  # check out https://github.com/py5coding 
from py5_tools import animated_gif

def setup():   # py5 will call this once to set things up
    py5.size(600, 600, py5.P3D)
    global shp
    ca = trimesh.primitives.Cylinder(radius=1.0, height=2.0, sections=32)
    cb = trimesh.primitives.Cylinder(radius=1.0, height=2.0, sections=32)
    cb.apply_translation([0.5, 0.5, 0.5])
    #s = trimesh.Scene([ca, cb])
    cc = ca.union(cb)
    py5.stroke_weight(0.0001)
    shp = py5.convert_shape(cc)
    shp.scale(100)
    shp.disable_style()
    py5.stroke(255, 0, 0)
    


def draw():   # py5 will call this in a loop
    py5.background(0)
    py5.lights()
    py5.translate(py5.width / 2, py5.height / 2)
    py5.rotate_y(py5.radians(py5.frame_count))
    py5.shape(shp)

    
def key_pressed():   # py5 will call this when a key is pressed
    if py5.key == 's':
        f = py5.frame_count
        animated_gif('out3.gif', frame_numbers=range(f + 1, f + 361, 4), duration=0.075) 
        
py5.run_sketch()
        
        


