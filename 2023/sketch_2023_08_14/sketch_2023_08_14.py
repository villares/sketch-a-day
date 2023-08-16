import py5

from tokenize_helper import get_tokens, reassemble_tokens, tokenize
from parse_ansi_strings import parse_ansi_strings

src_lines = []
font_size = 9

def setup():
    """
    Run just once.
    """
    global fr, fb, styled_lines
    py5.size(600, 600)
    fr = py5.create_font("Source Code Pro", font_size)
    fb = py5.create_font("Source Code Pro Bold", font_size)
    with open('sketch_2023_08_14.py') as f: # get source text
        src_lines.extend(f.readlines())
    py5.text_size(font_size)
    tokens = get_tokens(src_lines)
    styles = {
        tokenize.COMMENT: 'PURPLE',
        tokenize.STRING: 'BLUE',
        tokenize.DOCSTRING: 'RED',
        }
    styled_source = (reassemble_tokens(tokens, styles))
    # print(styled_source)
    styled_lines = parse_ansi_strings(styled_source)
    # for li in styled_lines: print(li)
    py5.background(200)
    py5.fill(0)
    draw_text(styled_lines, 50, 50)
    py5.save('out.png')
    
def draw_text(txt, x, y, line_height=font_size):
    py5.text_font(fb)
    py5.fill(0)
    tx, ty = x, y
    for style, li in txt:
        if style == 'NEWLINE':
            tx = x
            ty += line_height
            continue 
        if style == 'END':
            py5.text_font(fr)
            py5.fill(0)
        elif style == 'RED':
            py5.text_font(fb)
            py5.fill(200, 0, 0)
        elif style == 'PURPLE':
            py5.text_font(fb)
            py5.fill(200, 0, 200)
        elif style == 'BLUE':
            py5.text_font(fb)
            py5.fill(0, 0, 200)       
        py5.text(li, tx, ty)
        tx += py5.text_width(li)
    
py5.run_sketch()