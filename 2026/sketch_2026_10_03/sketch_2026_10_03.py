import py5
from itertools import cycle

M = 30
hor = '001001'
ver = '001011'
colors_x = ['darkred', 'darkgreen']
colors_y = ['purple', 'darkblue']

def setup():
    py5.size(650, 650)
    py5.stroke_weight(5)
    py5.text_font(py5.create_font('Inconsolata Bold', M))
    py5.text_align(py5.CENTER, py5.CENTER)
    py5.text_size(M * 0.7)
    
def draw():
    py5.background(128)
    w = 30
    h = w // 2
    xs = cycle(ver)
    ys = cycle(hor)
    for i, p in enumerate(hor):
        py5.fill(colors_y[int(p)])
        py5.text(p, M + i * h, M / 2)
    for i, p in enumerate(ver):
        py5.fill(colors_x[int(p)])
        py5.text(p, M / 2, M + i * h)
        
    for y in range(M, py5.height - M - 1, h):
        offset_x = next(xs) == '1'
        py5.stroke(colors_x[offset_x])
        for x in range(M, py5.width - M - 1, w):
            py5.line(x + h * offset_x, y,
                     x + h + h * offset_x, y) 
    for x in range(M, py5.width - M - 1, h):
        offset_y = next(ys) == '1'
        py5.stroke(colors_y[offset_y])
        for y in range(M, py5.height - M - 1, w):
            py5.line(x, y + h * offset_y,
                     x, y + h + h * offset_y) 
    py5.no_loop( )

def key_typed():
    if py5.key == 'p':
        py5.save_frame(f'{hor}x{ver}.png')
    py5.redraw()        

py5.run_sketch()


