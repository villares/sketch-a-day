import py5
from functools import cache

s = 1

def setup():
    py5.size(800, 800, py5.P3D)
    py5.background(200)
    py5.no_fill()
    py5.color_mode(py5.HSB)

def draw():
    py5.background(200)
    py5.random_seed(s)
    py5.translate(py5.width / 2, py5.width / 2)
#     py5.rotate_x(py5.radians(py5.frame_count * 4))
#     py5.rotate_y(py5.radians(py5.frame_count * 4))
    py5.ortho()
    poligonos_recursivos(0, 0, py5.width / 4)
#     if py5.frame_count == 180:
#         py5.exit_sketch()
#     else:
#         py5.save_frame('###.png', use_thread=True)

def poligonos_recursivos(xo, yo, r, n=4):
    with py5.push_matrix():
        z = py5.width / 4 / r
        py5.translate(xo, yo, 0)
#         py5.rotate_x(-py5.radians(py5.frame_count * 2))
        pontos = poly_points(r, n)
        sorteio = py5.random_choice((True, False))
        w = py5.width
        na = py5.random_int(4, 8)
        #print(na)
        if r > w / 10 or (sorteio and r > w / 200):
            for x, y in pontos:
                py5.stroke_weight(max(1, r / 40))  
                py5.stroke((r * 2) % 255, 200, 100)
                py5.line(x, y, 0, 0, 0, 0)
                poligonos_recursivos(x, y, r / 2, na)
        else:
            py5.stroke_weight(max(1, r / 10))    
            with py5.begin_closed_shape():
                py5.vertices(pontos)
   
@cache
def poly_points(r, n):
    a = py5.TWO_PI / n
    return [(r * py5.cos(i * a), # + py5.HALF_PI),
             r * py5.sin(i * a)) # + py5.HALF_PI))                 
            for i in range(n)]


def key_pressed(e):
    global s
    py5.save_frame('###imagem.png')
    s += 1
    py5.redraw()

py5.run_sketch()
