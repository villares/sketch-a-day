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
    py5.blend_mode(py5.ADD)
    py5.no_stroke()
    py5.fill(255)
    img = py5.load_image('image.jpg')
    r_bands = []
    g_bands = []
    b_bands = []
    step = 3
    sf = py5.width / img.width # scaling factor
    for y in range(0, img.height, step):
        rvs_up =  []
        rvs_down = []
        gvs_up =  []
        gvs_down = []
        bvs_up =  []
        bvs_down = []
        hf = 0.33
        for x in range(0, py5.width, step):
            r = py5.red(img.get_pixels(x, y))
            offset = py5.remap(r, 255, 0, step * hf, 0.25) 
            rvs_up.append((x * sf, (y - offset) * sf))
            rvs_down.append((x * sf, (y + offset) * sf))
            g = py5.green(img.get_pixels(x, y))
            offset = py5.remap(g, 255, 0, step * hf, 0.25) 
            gvs_up.append((x * sf, (y - offset) * sf))
            gvs_down.append((x * sf, (y + offset) * sf))
            b = py5.green(img.get_pixels(x, y))
            offset = py5.remap(b, 255, 0, step * hf, 0.25) 
            bvs_up.append((x * sf, (y - offset) * sf))
            bvs_down.append((x * sf, (y + offset) * sf))
        rvs_down.reverse()  
        r_bands.append(shapely.Polygon(rvs_up + rvs_down))    
        gvs_down.reverse()  
        g_bands.append(shapely.Polygon(gvs_up + gvs_down))    
        bvs_down.reverse()  
        b_bands.append(shapely.Polygon(bvs_up + bvs_down))    

    py5.background(0)

    py5.fill(255, 0, 0)
    multi_poly = shapely.MultiPolygon(r_bands)
    shp = py5.convert_shape(multi_poly) #.buffer(-1))    
    py5.shape(shp)
    py5.translate(0, 4)
    py5.fill(0, 255, 0)
    multi_poly = shapely.MultiPolygon(g_bands)
    shp = py5.convert_shape(multi_poly) #.buffer(-1))    
    py5.shape(shp) 
    py5.translate(0, 4)
    py5.fill(0, 0, 255)
    multi_poly = shapely.MultiPolygon(b_bands)
    shp = py5.convert_shape(multi_poly) #.buffer(-1))    
    py5.shape(shp) 

def key_pressed():
    if py5.key == 'p':
        print('saved.')
        py5.save_frame('####.png')
        

py5.run_sketch()
