"""
This is an "module mode" py5 sketch
Learn more at <https://py5coding.org>

Ada's portrait:
https://upload.wikimedia.org/wikipedia/commons/d/dd/Adalovelace.jpg
"""

import py5
import shapely

def setup():
    global img, shp
    py5.size(565, 565)
    py5.no_smooth()
    py5.no_stroke()
    img = py5.load_image('image.jpg')
    els = []
    step = 3 
    for x in range(0, img.width, step):
        for y in range(0, img.height, step):
            b = py5.brightness(img.get_pixels(x, y))
            radius = (b / 255 * step * py5.sqrt(2))
            el = shapely.Point((5 + x * 2.5, 5 + y * 2.5)).buffer(radius, quad_segs=1)
            els.append(el)
    multi_poly = shapely.MultiPolygon(els)
    shp = py5.convert_shape(multi_poly)
    
def draw():
    #py5.image(img, 0, 0)
    py5.background(0)
    py5.shape(shp) 

def key_pressed():
    print(py5.key)
    if py5.key == 'p':
        py5.save_frame('####.png')

py5.run_sketch()

