import tokenize

import py5

from parse_ansi_strings import parse_ansi_strings, STYLE

from tokenize_helper import get_tokens, reassemble_tokens

src_lines = []
col = False


def setup():
    py5.size(1000, 500)
    with open(__file__) as f: # get source text
        src_lines.extend(f.readlines())
    py5.background(200)
    py5.fill(0)
    tokens = get_tokens(src_lines)
    styles = {
        tokenize.COMMENT: 'DARKCYAN',
        tokenize.STRING: 'BLUE',
        tokenize.DOCSTRING: 'PURPLE',
        'KEYWORD': 'RED',
        'BUILTIN': 'GREEN',
        }
    styled_source = reassemble_tokens(tokens, styles)   
    prepare_styled_text()
    draw_styled_text(styled_source, 20, 20, line_height=12 * 1.1)
    py5.save('out.png')


def prepare_styled_text(font_size=12):
    global font, bold_font
    font = py5.create_font("Source Code Pro Bold", font_size)
    bold_font = py5.create_font("Source Code Pro", font_size)


def draw_styled_text(ansi_marked_txt, x, y, font_size=12, line_height=None):
    segments = parse_ansi_strings(ansi_marked_txt)
    line_height = line_height or font_size
    draw_text_segments(segments, x, y, font_size, line_height)


def draw_text_segments(segments, x, y, font_size, line_height):
    py5.text_font(font)
    py5.text_size(font_size)
    py5.fill(0)
    tx, ty = x, y
    for style, li in segments:
        if style == 'NEWLINE':
            tx = x
            ty += line_height
            continue 
        elif style == 'END':
            py5.text_font(font)
            py5.fill(0)
        elif style == 'BOLD':
            py5.text_font(bold_font)
        else:
            try:
                py5.fill(style)
            except:
                print(style)
        py5.text(li, tx, ty)
        tx += py5.text_width(li)
        if ty > py5.height - line_height or col:
            x += x + py5.width / 2
            ty =  y


py5.run_sketch(block=False)


