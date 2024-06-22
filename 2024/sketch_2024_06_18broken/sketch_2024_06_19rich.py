import builtins

import py5

from rich.syntax import Syntax
from rich.console import Console
console = Console(record=True)

def rich_render(rich_markup):
    with console.capture() as capture:
        console.print(rich_markup)
    #return capture.get()
    print(capture.get())
    console.save_svg('temp.svg')


def setup():
    py5.size(800, 500)
    rich_render('[bold]Hello[/] [red]World')    
    
    shp = py5.load_shape('temp.svg')
    
    py5.shape(shp, 0, 0)
# console = Console()
# with open(__file__, "rt") as code_file:
#     syntax = Syntax(code_file.read(), "python")
# console.print(syntax)


# from parse_ansi_strings import parse_ansi_strings, STYLE
# 
# src_lines = []
# col = False
# 
# def setup():
#     py5.size(900, 900)
#     with open(__file__) as f: # get source text
#         src_lines.extend(f.readlines())
#     source = ''.join(src_lines)
#     styled_source = source.replace('py5', '[red]py5[/]')
# #     for name in dir(builtins):
# #         styled_source = styled_source.replace(
# #         name, STYLE['RED'] + name + STYLE['END']
# #         )
#     styled_source = rich_render(styled_source)
#     print(styled_source)
#     py5.background(200)
#     py5.fill(0)
#     prepare_styled_text()
#     draw_styled_text(styled_source, 20, 20, line_height=12 * 1.1)
#     py5.save('out.png')
#     
# def prepare_styled_text(font_size=12):
#     global font, bold_font
#     font = py5.create_font("Source Code Pro Bold", font_size)
#     bold_font = py5.create_font("Source Code Pro", font_size)
# 
# 
# # ---COL-BREAK---
# def draw_styled_text(ansi_marked_txt, x, y, font_size=12, line_height=None):
#     segments = parse_ansi_strings(ansi_marked_txt)
#     line_height = line_height or font_size
#     draw_text_segments(segments, x, y, font_size, line_height)
# 
# def draw_text_segments(segments, x, y, font_size, line_height):
#     col = False
#     py5.text_font(font)
#     py5.text_size(font_size)
#     py5.fill(0)
#     tx, ty = x, y
#     for style, li in segments:
#         if li.startswith('# ---COL-BREAK---'):  # magic col comment
#             li = ''
#             col = True
#         elif style == 'NEWLINE':
#             tx = x
#             ty += line_height
#             continue 
#         elif style == 'END':
#             py5.text_font(font)
#             py5.fill(0)
#         elif style == 'BOLD':
#             py5.text_font(bold_font)
#         else:
#             try:
#                 py5.fill(style)
#             except:
#                 print(style)
#         py5.text(li, tx, ty)
#         tx += py5.text_width(li)
#         if ty > py5.height - line_height or col:
#             x += x + py5.width / 2
#             ty = y
#             col = False
# 
# 
py5.run_sketch(block=False)


