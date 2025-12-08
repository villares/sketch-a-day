import py5

def setup():
    py5.size(900, 900)
    py5.background(255)
    py5.no_fill()
    py5.random_seed(10)
    recursive_hex(py5.width / 2, py5.height / 2, py5.width / 4)
    py5.save('out.png')

def recursive_hex(xo, yo, r, n=6):
    if py5.random(2) > 1 and r > py5.width / 100:
        for x, y in poly_points(xo, yo, r, n):
            py5.stroke(0)
            py5.stroke_weight(0.5 + r / 50)
            #py5.line((x + xo) / 2 , (y + yo) / 2, xo, yo)
            py5.line(x, y, xo, yo)
            with py5.begin_closed_shape():
                py5.vertices(poly_points(xo, yo, r / 2, n))        
            recursive_hex(x, y, r / 2, n)
    else:
        py5.stroke('green' if r > 50 else 'red' if r < 10 else 'blue') 
        py5.stroke_weight(0.5 + r / 10)
        with py5.begin_closed_shape():
            py5.vertices(poly_points(xo, yo, r, n))

def poly_points(xo, yo, r, n):
    return [
        (xo + r * py5.cos((-0.25 + i) * py5.TWO_PI / n),
         yo + r * py5.sin((-0.25 + i) * py5.TWO_PI / n))
        for i in range(n)
    ]

py5.run_sketch()
