import py5

zen_lines = []
src_lines = []
font_size = 9

def setup():
    global fr, fb
    py5.size(600, 600)
    
    fr = py5.create_font("Source Code Pro", font_size)
    fb = py5.create_font("Source Code Pro Bold", font_size)
 
    with open('zen.txt') as f: # get text
        zen_lines.extend(f.readlines())
    with open('sketch_2023_08_13.py') as f: # get text
        src_lines.extend(f.readlines())
        
    py5.text_size(font_size)
    py5.no_loop()

def draw():
    py5.background(200)
    py5.fill(0)
    py5.text_font(fr)
    draw_text(zen_lines, 50, 50)
    py5.text_font(fb)
    draw_text(src_lines, 250, 250)
    py5.save('out.png')
    
def draw_text(txt, x, y, line_height=font_size):
    tx, ty = x, y
    for li in txt:
        py5.text(li, tx, ty)
        ty += line_height
    
py5.run_sketch()