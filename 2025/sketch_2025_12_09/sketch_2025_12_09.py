import py5

def setup():
    py5.size(900, 900)
    py5.color_mode(py5.CMAP, 'magma_r', py5.width / 3)
    py5.background('black') 
    py5.no_stroke() 
    py5.random_seed(1)
    recursive_hex(py5.width / 2, py5.height / 2, py5.width / 4)
    
def recursive_hex(xo, yo, r, n=6):
    pts = [(xo + r * py5.cos(i * py5.TWO_PI / n),
            yo + r * py5.sin(i * py5.TWO_PI / n)) for i in range(n)]
    if py5.random(2) > 1 and r > py5.width / 100:
        for x, y in pts:
            py5.stroke(r) 
            py5.stroke_weight(0.5 + r / 50)
            if py5.is_mouse_pressed:
                py5.line((x + xo) / 2, (y + yo) / 2, xo, yo)
            else:
                py5.line(x, y, xo, yo) 
            recursive_hex(x, y, r / 2, n)
    else:
        py5.no_stroke()
        py5.fill(r, 200) 
        #py5.stroke_weight(0.5 + r / 20)
        with py5.begin_closed_shape():
            py5.vertices(pts)


def key_pressed():
    if py5.key == 's':
        py5.save('out.png')

py5.run_sketch()

