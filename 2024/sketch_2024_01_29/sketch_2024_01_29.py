import py5
import trimesh
from sdf import sphere, box, cylinder, X, Y, Z

f = sphere(1) & box(1.5)
c = cylinder(0.5)
f -= c.orient(X) | c.orient(Y) | c.orient(Z)
#f.save('out.stl')
m = trimesh.load_mesh('out.stl')
#m.show()  # trimesh viewer

def setup():
    global s
    py5.size(500, 500, py5.P3D)
    s = py5.convert_shape(m)
    s.disable_style()
    #py5.shape_mode(py5.CENTER)
    
def draw():
    py5.background(200)
    py5.lights()
    py5.translate(py5.width / 2, py5.height / 2)
    py5.rotate_y(py5.mouse_x / 10)
    py5.fill(255, 0, 0)
    py5.no_stroke()
    py5.scale(200)
    py5.shape(s, 0, 0)
    
py5.run_sketch()

    