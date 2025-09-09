import py5

def setup():
    py5.size(900, 900)
    py5.color_mode(py5.HSB)
    py5.background(240)
    py5.no_fill()
    py5.random_seed(10)
    x = y = py5.width / 2
    poligonos_recursivos(x, y, py5.width / 4)
    py5.save('out.png')

def poligonos_recursivos(xo, yo, r, n=6):
    a = py5.TWO_PI / n
    pontos = [(xo + r * py5.cos(i * a), yo + r * py5.sin(i * a))
              for i in range(n)]
    sorteio = py5.random_choice((True, False))
    w = py5.width
    py5.no_stroke()
    py5.fill(r * 6, 200, 150, 200)
    if r > w / 10 or (sorteio and r > w / 100):
        for x, y in pontos:
            py5.stroke_weight(r / 50)
            py5.stroke(0)
            py5.line(x, y, xo, yo)
            poligonos_recursivos(x, y, r / 2, n)
    else:
        py5.stroke_weight(r / 10)
        with py5.begin_closed_shape():
            py5.circle(xo, yo, r * 2)
#             py5.curve_vertices(
#                 [pontos[-1]] + pontos + pontos[:2])

py5.run_sketch()
