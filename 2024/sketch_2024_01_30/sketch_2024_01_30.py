"""
 * Toon Shading.
 * 
 * Example showing the use of a custom lighting shader in order    
 * to apply a "toon" effect on the scene. Based on the glsl tutorial 
 * from lighthouse 3D:
 * http://www.lighthouse3d.com/tutorials/glsl-tutorial/toon-shader-version-ii/
"""

import py5
import trimesh
from sdf import sphere, box, cylinder, X, Y, Z

f = sphere(1) & box(1.5)
c = cylinder(0.5)
f -= c.orient(X) | c.orient(Y) | c.orient(Z)
#f.save('out.stl')
m = trimesh.load_mesh('out.stl')

shader_enabled = True    

def setup():
    global s
    py5.size(500, 500, py5.P3D)
    s = py5.convert_shape(m)
    s.disable_style()
    
    global toon
    toon =  py5.load_shader("ToonFrag.glsl", "ToonVert.glsl")
    
def draw():
    if shader_enabled == True:
        py5.shader(toon)
    py5.background(0)
    #py5.lights()    # breakes shader!
    dirY = (py5.mouse_y / py5.height - 0.5) * 2
    dirX = (py5.mouse_x / py5.width - 0.5) * 2
    #py5.directional_light(204, 204, 204, -dirX, -dirY, -1)
    py5.directional_light(204, 204, 204, 0, 0, -1)
    py5.translate(py5.width / 2, py5.height / 2)
    py5.rotate_y(py5.mouse_x / 10)
    py5.rotate_x(py5.mouse_y / 10)
    py5.fill(204)
    py5.no_stroke()
    py5.scale(200)
    #py5.sphere(120)
    py5.shape(s, 0, 0)
    
    
def mouse_pressed() :
    global shader_enabled
    if shader_enabled:
        shader_enabled = False
        py5.reset_shader()
    else:
        shader_enabled = True

    
py5.run_sketch()
