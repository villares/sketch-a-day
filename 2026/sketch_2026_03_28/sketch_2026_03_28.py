# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org

import py5
import py5_tools
import shapely

from matplotlib.font_manager import FontProperties
from matplotlib.textpath import TextPath
from py5.shape_conversion import textpath_to_shapely_converter as tp_to_sly

fp = FontProperties(family="DejaVu Sans",style="normal", size=120)
polys = (tp_to_sly(TextPath((20, -120), "tosconf", prop=fp)) |
         tp_to_sly(TextPath((20, -240), "LHC", prop=fp)))

def setup():
    py5.size(500, 500)
    py5.no_stroke()
    py5_tools.animated_gif('out.gif',
                            frame_numbers=range(1, 37),
                            duration=0.03) 
 
def draw():
    py5.background(0)
    w = py5.width
    h = 26
    gap = 10
    start = py5.frame_count % (h + gap)
    for y in range(-start, py5.height, h + gap):
        pontos = ((0, y), (w, y), (w, y + h), (0, y + h))
        p = shapely.Polygon(pontos).buffer(-1)
        pi = polys.intersection(p).buffer(5)
        py5.color_mode(py5.HSB)
        py5.fill(y % 255, 255, 255)
        py5.shape(pi, 0, 200)

def key_pressed():
    py5.save_frame('out.png')

py5.run_sketch(block=False)


