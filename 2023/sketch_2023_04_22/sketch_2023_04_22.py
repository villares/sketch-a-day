scale_factor = 1.78
line_height = 16

import py5
import matplotlib.colors as mcolors

named_palettes = (
    'CSS4_COLORS',
    'BASE_COLORS',
    'TABLEAU_COLORS',
    'XKCD_COLORS',
    )

def setup():
    py5.size(1024, 1024)        
    svg = py5.create_graphics(
        int(py5.width * scale_factor), int(py5.height * scale_factor), py5.SVG, 'out.svg')
    py5.scale(1 / scale_factor) # smallor on screen than on SVG file
    py5.begin_record(svg)
    py5.background(255)
    py5.text_align(py5.LEFT, py5.CENTER)
    x = y = line_height / 2
    for name in named_palettes:
        palette_dict = getattr(mcolors, name)
        color_names = sorted(palette_dict, key=lambda c: tuple(mcolors.rgb_to_hsv(mcolors.to_rgb(c))))
        py5.fill(0)
        py5.text(name, x, y)
        y += line_height
        for color_name in color_names:
            hex_color_str = palette_dict[color_name]
            py5.fill(color_name)
            py5.rect(x, y, 40, 12)
            py5.fill(0)
            py5.text(color_name, x + 45, y + 6)
            y += line_height
            if y > py5.height * scale_factor - line_height:
                y = line_height / 2  # back to top
                x += 180  # next collumn
        y += line_height # adds vertical space before next palette 

    py5.end_record() 
        
py5.run_sketch()


