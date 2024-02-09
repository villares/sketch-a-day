import py5
from shapely import Polygon, MultiPolygon
import trimesh

from villares.shapely_helpers import polys_from_text, draw_shapely_objs


pontos = [
    (100, 100),
    (300, 100),
    (300, 300),
    (150, 250),
    ]

quadradinho = [
    (150, 150),
    (200, 150),
    (200, 200),
    (150, 200)
    ]

def setup():
    global polys
    py5.size(800, 400)
    p = Polygon(pontos)
    q = Polygon(quadradinho)
    pb = p.buffer(50)
    pd = pb.difference(q)
    draw_shapely_objs(pd)

    f = py5.create_font('Tomorrow Regular', 100)
    py5.text_font(f)
    texto = 'Hello shapely!'
    polys = MultiPolygon(polys_from_text(texto, f))
    py5.translate(100, 300)
    py5.fill(0, 0, 200)
    draw_shapely_objs(polys.buffer(3))
    py5.save(__file__[:-2] + 'png')
   
   
   
py5.run_sketch(block=False)