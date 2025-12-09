import py5

seed = 13

def setup():
    py5.size(900, 900)  # tamanho
    py5.color_mode(py5.CMAP, 'viridis_r', 100)
    
def draw():
    py5.background('k')  # fundo branco
    py5.no_fill()  # sem preenchimento 
    py5.random_seed(seed)
    recursive_hex(py5.width / 2, py5.height / 2, py5.width / 4, 6)
    
def key_pressed():
    if py5.key == 's':
        py5.save('out.png')

def recursive_hex(xo, yo, r, n=6):
    if py5.random(2) > 1 and r > py5.width / 100:
        for x, y in poly_points(xo, yo, r, n):
            py5.stroke(r) 
            py5.stroke_weight(0.5 + r / 50)
            #py5.line((x + xo) / 2 , (y + yo) / 2, xo, yo)
            if py5.is_mouse_pressed:
                py5.line((x + xo) / 2, (y + yo) / 2, xo, yo)
            else:
                py5.line(x, y, xo, yo) 
            recursive_hex(x, y, r / 2, n)
    else:
        py5.stroke(r) 
        py5.stroke_weight(0.5 + r / 20)
        with py5.begin_closed_shape():
            py5.vertices(poly_points(xo, yo, r, n))

def poly_points(xo, yo, r, n):
    return [
        (xo + r * py5.cos(i * py5.TWO_PI / n),
         yo + r * py5.sin(i * py5.TWO_PI / n))
        for i in range(n)
    ]

py5.run_sketch()
