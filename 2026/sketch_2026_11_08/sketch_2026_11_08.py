"""
This is an "module mode" py5 sketch
Learn more at <https://py5coding.org>

https://upload.wikimedia.org/wikipedia/commons/d/dd/Adalovelace.jpg
"""

import py5
import shapely
import trimesh

def setup():
    global mesh, img, shp
    py5.size(600, 600, py5.P3D)
    img = py5.load_image('image.jpg')
    prisms = []
    step = 5
    for x in range(0, img.width, step):
        for y in range(0, img.height, step):
            b = py5.brightness(img.get_pixels(x, y))
            radius = (b / 255 * step)
            base = shapely.Point((x * 2, y * 2)).buffer(radius, quad_segs=2)
            prism = trimesh.creation.extrude_polygon(base, radius * 10)
            prisms.append(prism)
    mesh = trimesh.util.concatenate(prisms)
    shp = py5.convert_shape(mesh)
    
def draw():
    py5.background(0)
    #py5.image(img, 0, 0)
    py5.translate(400, 375)
    py5.rotate_y(py5.radians(20)) 
    py5.shape(shp, -300, -300) 

def key_pressed():
    print(py5.key)
    if py5.key == 'p':
        py5.save_frame('####.png')

py5.run_sketch()

