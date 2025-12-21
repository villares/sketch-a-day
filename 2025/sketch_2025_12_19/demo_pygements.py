import py5

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import SvgFormatter

import cairosvg # failed with: "ValueError: The SVG size is undefined"
from wand.image import Image

def source_to_svg(source_file, output_file, language='python'):
    """
    Convert source code file to syntax-highlighted SVG
    """
    with open(source_file, 'r') as file:
        source_code = file.read()
    lexer = get_lexer_by_name(language)
    formatter = SvgFormatter(
        style='monokai',#, full=True, linenos=True
        width=800
    )
    
    highlighted_code = highlight(source_code, lexer, formatter)
    with open(output_file, 'w') as svg_file:
        svg_file.write(highlighted_code)

def setup():
    py5.size(800, 800)
    py5.background(0)
    source_to_svg(__file__, 'temp.svg')
    #img = py5.convert_image('temp.svg', scale=0.5, parent_width=800) 
#     with open('temp.svg') as svg_file:
#         cairosvg.svg2png(
#             bytestring=svg_file.read(), 
#             write_to='temp.png',
#             background_color='transparent'
#         )
    svg = Image(filename='temp.svg')
    svg.save(filename='temp.png')
    img = py5.load_image('temp.png')
    py5.image(img, 0, 0)
    
py5.run_sketch(block=False)