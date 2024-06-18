import py5

from parse_ansi_strings import parse_ansi_strings, STYLE

src_lines = []
font_size = 12
col = False

def setup():
    """
    Run just once.
    """
    global fr, fb, styled_lines
    py5.size(900, 450)
    fb = py5.create_font("Source Code Pro Bold", font_size)
    fr = py5.create_font("Source Code Pro", font_size)
    with open(__file__) as f: # get source text
        src_lines.extend(f.readlines())
    py5.text_size(font_size)
    styled_source = ''.join(src_lines).replace(
        'py5',
        STYLE['BLUE'] + 'py5' + STYLE['END']
        ) 
    print(styled_source)
    styled_lines = parse_ansi_strings(styled_source)
    #for li in styled_lines: print(li)
    py5.background(200)
    py5.fill(0)
    draw_text(styled_lines, 20, 20, line_height=font_size * 1.1)
    py5.save('out.png')
# --- 

def draw_text(txt, x, y, line_height=font_size):
    global col
    py5.text_font(fr)
    py5.fill(0)
    tx, ty = x, y
    for style, li in txt:
        if li.startswith('# ---'):  # magic col comment
            col = True
            continue
        if style == 'NEWLINE':
            tx = x
            ty += line_height
            continue 
        elif style == 'END':
            py5.text_font(fr)
            py5.fill(0)
        elif style == 'BOLD':
            py5.text_font(fb)
        else:
            try:
                py5.fill(style)
            except:
                print(style)
        py5.text(li, tx, ty)
        tx += py5.text_width(li)
        if ty > py5.height - line_height or col:
            x += x + py5.width / 2
            ty = y
            col = False


py5.run_sketch(block=False)


