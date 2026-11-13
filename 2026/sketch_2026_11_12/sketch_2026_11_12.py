"""
This is an "module mode" py5 sketch
Learn more at <https://py5coding.org>

Ada's portrait:
https://upload.wikimedia.org/wikipedia/commons/d/dd/Adalovelace.jpg
"""

import py5
import shapely
import numpy as np

def setup():
    global img, shp, els
    py5.size(900, 900)
    py5.no_smooth()
    py5.no_stroke()
    py5.fill(255)
    img = py5.load_image('image.jpg')
    bands = []
    step = 2
    sf = py5.width / img.width # scaling factor
    for y in range(0, img.height, step):
        vs_up =  []
        vs_down = []
        for x in range(0, py5.width, step):
            b = py5.brightness(img.get_pixels(x, y))
            offset = py5.remap(b, 255, 0, step * 0.5, 0.25) 
            vs_up.append((x * sf, (y - offset) * sf))
            vs_down.append((x * sf, (y + offset) * sf))
            if (x / step) % 2 == 0:
                bands.append(shapely.LineString(
                    ((x * sf, 0), (x * sf, py5.width))
                ).buffer(0.5)) 
        vs_down.reverse() 
        band_vs = vs_up + vs_down
        bands.append(shapely.Polygon(band_vs))    
        
    multi_poly = shapely.MultiPolygon(bands)
    shp = py5.convert_shape(multi_poly) #.buffer(-1))
    
def draw():
    py5.background(0)
    py5.shape(shp) 
    #py5.image(img, 0, 0)

def key_pressed():
    if py5.key == 'p':
        print('saved.')
        py5.save_frame('####.png')
        

py5.run_sketch()

