import py5
from itertools import cycle

M = 30
W = 30
hor = '001001'
ver = '001011'
colors_x = ['darkred', 'darkgreen']
colors_y = ['purple', 'darkblue']

def setup():
    py5.size(650, 650)
    py5.text_font(py5.create_font('Inconsolata Bold', M))
    py5.text_align(py5.CENTER, py5.CENTER)
    py5.text_size(M * 0.7)
    
def draw():
    py5.background(128)
    h = W // 2
    xs = cycle(ver)
    ys = cycle(hor)

    py5.stroke_weight(5)
    for y in range(M, py5.height - M - 1, h):
        offset_x = next(xs) == '1'
        py5.stroke(colors_x[offset_x])
        for x in range(M, py5.width - M - 1, W):
            py5.line(x + h * offset_x, y,
                     x + h + h * offset_x, y) 
    for x in range(M, py5.width - M - 1, h):
        offset_y = next(ys) == '1'
        py5.stroke(colors_y[offset_y])
        for y in range(M, py5.height - M - 1, W):
            py5.line(x, y + h * offset_y,
                     x, y + h + h * offset_y)
            
    for i, p in enumerate(hor):
        x, y = M + i * h, M / 2
        if mouse_over(x, y):
            py5.no_fill()
            py5.stroke(colors_x[int(p)])
            py5.rect(x - W / 4, y - W / 4,
                     W / 2, W / 2)
        py5.fill(colors_y[int(p)])
        py5.text(p, x, y) 
        
    for i, p in enumerate(ver):
        x, y = M / 2, M + i * h
        if mouse_over(x, y):
            py5.no_fill()
            py5.stroke(colors_x[int(p)])
            py5.rect(x - W / 4, y - W / 4,
                     W / 2, W / 2)
        py5.fill(colors_x[int(p)])
        py5.text(p, x, y)


def mouse_over(x, y):
    mx, my = py5.mouse_x, py5.mouse_y
    return (x - W / 4 < mx < x + W / 4 and
            y - W / 4 < my < y + W / 4)    
    
def mouse_clicked():
    global ver, hor
    for i, p in enumerate(hor):
        x, y = M + i * W / 2, M / 2
        if mouse_over(x, y):
            hor = update_pattern(hor, i)
            print('hor', hor)
    for i, p in enumerate(ver):
        x, y = M / 2, M + i * W / 2
        if mouse_over(x, y):
            ver = update_pattern(ver, i)
            print('ver', ver)
            
def update_pattern(s, i):
    t = '0' if s[i] == '1' else '1'
    return s[:i] + t + s[i+1:]
    
def key_typed():
    if py5.key == 'p':
        py5.save_frame(f'{hor}x{ver}.png')
    elif py5.key == 'i':
        py5.redraw()        

py5.run_sketch()


