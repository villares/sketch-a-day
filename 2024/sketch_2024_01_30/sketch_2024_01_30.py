"""
You'll need the shader files ToonFrag.glsl & ToonVert.glsl in the data folder of this sketch

Header from the original Processing Java example
 * Toon Shading.
 * 
 * Example showing the use of a custom lighting shader in order    
 * to apply a "toon" effect on the scene. Based on the glsl tutorial 
 * from lighthouse 3D:
 * http://www.lighthouse3d.com/tutorials/glsl-tutorial/toon-shader-version-ii/

2024-02-03 - Adding some suggestions from @GoToLoop at
https://discourse.processing.org/t/py5-loves-3d-pd3-hints-shaders/43821
"""

from pathlib import Path

import py5      # Installation instructions at https://py5coding.org
import trimesh  # `pip install trimesh[easy]` The [easy] part is optional for this sketch

# At first I used `pip install sdf-fork` now I'm using `pip install sdfcad`
from sdf import  sphere, box, cylinder, X, Y, Z  # `pip install sdfcad`

STL_FILE = 'out2.stl'
SCALE_FACTOR = 200

shader_enabled = True    # left button mouse click to toggle
lights_enabled = False   # right button mouse click to toggle

def setup():
    global s
    py5.size(500, 500, py5.P3D)
        
    if not Path(STL_FILE).exists():
        f = sphere(1) & box(1.5)
        c = cylinder(0.5)
        f -= c.orient(X) | c.orient(Y) | c.orient(Z)
        f.save(STL_FILE, step=0.01)

    m = trimesh.load_mesh(STL_FILE)
    s = py5.convert_shape(m)
    s.disable_style()
    
    global toon
    toon =  py5.load_shader("ToonFrag.glsl", "ToonVert.glsl")
    py5.shader(toon)
    
def draw():
    py5.background(0)    
    if lights_enabled: # breakes shader!
        py5.lights()    
    dirY = (py5.mouse_y / py5.height - 0.5) * 2
    dirX = (py5.mouse_x / py5.width - 0.5) * 2
    #py5.directional_light(204, 204, 204, -dirX, -dirY, -1)
    py5.directional_light(204, 204, 204, 0, 0, -1)
    py5.translate(py5.width / 2, py5.height / 2)
    py5.rotate_y(py5.mouse_x / 10)
    py5.rotate_x(py5.mouse_y / 10)
    py5.fill(204)
    py5.no_stroke()
    py5.scale(SCALE_FACTOR)
    #py5.sphere(120)
    py5.shape(s, 0, 0)
    
    
def mouse_pressed() :
    global shader_enabled, lights_enabled
    if py5.mouse_button == py5.LEFT:
        shader_enabled = not shader_enabled
        if shader_enabled:
            py5.shader(toon)
        else:
            py5.reset_shader()
    elif py5.mouse_button == py5.RIGHT:
        lights_enabled = not lights_enabled


py5.run_sketch()
