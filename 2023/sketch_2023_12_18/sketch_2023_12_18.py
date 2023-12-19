import py5
from shapely_helpers import polys_from_text, draw_shapely_objs

from shapely import Polygon, MultiPolygon

pontos = [
    (100, 100),
    (500, 100),
    (500, 300),
    (150, 250),
    ]

rect_pts = [
    (150, 150),
    (300, 150),
    (300, 250),
    (150, 250)
    ]

def setup():
    global polys
    py5.size(800, 400)
    py5.no_stroke()
    p = Polygon(pontos)
    q = Polygon(rect_pts)
    p = p.difference(q)
    for i in range(10):
        py5.fill(200, 128 + i * 12, i * 24)
        pb = p.buffer(60 - i * 5)
        draw_shapely_objs(pb)

    f = py5.create_font('Tomorrow Regular', 100)
    py5.text_font(f)
    texto = 'HHHHHHHHHHHHHHHHHHh\n'
    polys = MultiPolygon(polys_from_text(texto, f, leading=85))
    for i in range(5):
        py5.translate(0, 85)
        py5.fill(128 - i * 24, 128 + i * 24, 255)
        draw_shapely_objs(polys.buffer(4-i))
    py5.save(__file__[:-2] + 'png')
   
py5.run_sketch(block=False)
