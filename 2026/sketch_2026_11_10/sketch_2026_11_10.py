"""
This is an "module mode" py5 sketch
Learn more at <https://py5coding.org>

Ada's portrait:
https://upload.wikimedia.org/wikipedia/commons/d/dd/Adalovelace.jpg
"""

import py5
import shapely

def setup():
    global img, shp, els
    py5.size(565, 565)
    py5.no_smooth()
    py5.no_stroke()
    py5.fill(0)
    img = py5.load_image('image.jpg')
    els = []
    cuts = []
    step = 7
    sf = 2.5 # scaling factor
    for x in range(0, img.width, step):
        for y in range(0, img.height, step):
            b = py5.brightness(img.get_pixels(x, y))
            radius = ((255 - b) / 255 * step * 2)
            el = shapely.Point(
                (step / 2 + x * sf, step / 2 + y * sf)
            ).buffer(radius, quad_segs=1)
            #el = el.buffer(-1) #, quad_segs=2)
            if el.area > 5:
                els.append(el.buffer(1))
        cuts.append(shapely.LineString(
            ((3.5 * step / 2  + x * sf, 0), (3.5 * step / 2 + x * sf, py5.width))
        ).buffer(1))
    multi_poly = shapely.unary_union(els) - shapely.MultiPolygon(cuts)
    shp = py5.convert_shape(multi_poly.buffer(-1))
    
def draw():
    #py5.image(img, 0, 0)
    py5.background(255)
    py5.shape(shp) 

def key_pressed():
    print(py5.key)
    if py5.key == 'p':
        py5.save_frame('####.png')

py5.run_sketch()

