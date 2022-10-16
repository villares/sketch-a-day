import py5

def setup():
    py5.size(800, 800)
    py5.background(200)
    py5.no_fill()
    py5.no_loop()
    py5.random_seed(1)

def draw():
    py5.background(200)
    x = y = py5.width / 2
    poligonos_recursivos(x, y, py5.width / 4)

def poligonos_recursivos(xo, yo, r, n=6):
    a = py5.TWO_PI / n
    pontos = [(xo + r * py5.cos(i * a), # + py5.HALF_PI),
               yo + r * py5.sin(i * a)) # + py5.HALF_PI))                 
              for i in range(n)]
    sorteio = py5.random_choice((True, False))
    w = py5.width    
    if r > w / 10 or (sorteio and r > w / 200):
        for x, y in pontos:
            py5.stroke_weight(r / 50)  
            py5.line(x, y, xo, yo)
            poligonos_recursivos(x, y, r / 2, n)
    else:
        py5.stroke_weight(r / 10)    
        with py5.begin_closed_shape():
            py5.vertices(pontos)

def key_pressed(e):
    py5.save_frame('imagem.png')
    py5.redraw()

py5.run_sketch()
