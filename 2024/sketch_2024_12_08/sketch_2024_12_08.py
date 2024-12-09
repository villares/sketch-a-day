"""
# Raster to Vector Graphics Converter built on top of visioncortex 
import vtracer  # https://pypi.org/project/vtracer/

# Minimal example: use all default values, generate a multicolor SVG
vtracer.convert_image_to_svg_py(inp, out)
# Single-color example. Good for line art, and much faster than full color:
vtracer.convert_image_to_svg_py(inp, out, colormode='binary')
# Convert from raw image bytes
input_img_bytes: bytes = get_bytes() # e.g. reading bytes from a file or a HTTP request body
svg_str: str = vtracer.convert_raw_image_to_svg(input_img_bytes, img_format = 'jpg')
# Convert from RGBA image pixels
from PIL import Image
img = Image.open(input_path).convert('RGBA')
pixels: list[tuple[int, int, int, int]] = list(img.getdata())
svg_str: str = vtracer.convert_pixels_to_svg(pixels)
# All the bells & whistles, also applicable to convert_raw_image_to_svg and convert_pixels_to_svg. 
vtracer.convert_image_to_svg_py(inp,
                                out,
                                colormode = 'color',        # ["color"] or "binary"
                                hierarchical = 'stacked',   # ["stacked"] or "cutout"
                                mode = 'spline',            # ["spline"] "polygon", or "none"
                                filter_speckle = 4,         # default: 4
                                color_precision = 6,        # default: 6
                                layer_difference = 16,      # default: 16
                                corner_threshold = 60,      # default: 60
                                length_threshold = 4.0,     # in [3.5, 10] default: 4.0
                                max_iterations = 10,        # default: 10
                                splice_threshold = 45,      # default: 45
                                path_precision = 3          # default: 8
                                )
"""

import py5
from py5_tools import animated_gif
import vtracer


raster_input = 'logo.png'
svg_output = 'logo.svg'

vtracer.convert_image_to_svg_py(raster_input,
                                svg_output,
                                mode='polygon',
                                hierarchical='cutout', )
shapes = []

def setup():
    global shp
    py5.size(512, 512, py5.P3D)
    shp = py5.load_shape(svg_output)
    #py5.shape(shp)
    for child in shp.get_children():
        shapes.append(child)
    animated_gif(svg_output + '.gif', duration=0.15, frame_numbers=range(1,361,5))
        
def draw():
    py5.background(0)
    py5.translate(256, 256, -256)
    py5.rotate_y(py5.radians(py5.frame_count))
    py5.translate(-256, -256)
    for shp in shapes:
        py5.shape(shp)
        py5.translate(0, 0, 10)# 0.05)
    
py5.run_sketch(block=False)

