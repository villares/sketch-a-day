"""
This is an "module mode" py5 sketch
Learn more at <https://py5coding.org>

https://upload.wikimedia.org/wikipedia/commons/d/dd/Adalovelace.jpg
"""

import py5
import shapely
import numpy as np

def setup():
    global img, shp, els
    py5.size(900, 900)
    #py5.no_smooth()
    py5.no_stroke()
    py5.fill(0)
    img = py5.load_image('image.jpg')
    cuts = []
    step = 2
    sf = py5.width / img.width # scaling factor
    for y in range(0, img.height, step):
        cut =  []
        reversed_cut = []
        for x in range(0, img.width, step):           
            b = py5.brightness(img.get_pixels(x, y))
            offset = py5.remap(b, 0, 255, step / 2, 0)
            cut.append((x * sf, (y - offset) * sf))
            reversed_cut.append((x * sf, (y + offset) * sf))
        reversed_cut.reverse()
        els = cut + reversed_cut
        cuts.append(shapely.Polygon(els))    
#         v.append(shapely.LineString(
#             ((3.5 * step / 2  + x * sf, 0), (3.5 * step / 2 + x * sf, py5.width))
#         ).buffer(1))
    multi_poly = shapely.MultiPolygon(cuts)
    shp = py5.convert_shape(multi_poly) #.buffer(-1))
    
def draw():
    #py5.image(img, 0, 0)
    py5.background(255)
    py5.shape(shp) 

def key_pressed():
    print(py5.key)
    if py5.key == 'p':
        py5.save_frame('####.png')

py5.run_sketch()

