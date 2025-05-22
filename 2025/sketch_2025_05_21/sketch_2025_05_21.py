import py5
from py5_tools import animated_gif

from villares.geometry_helpers import hatch_poly, draw_poly

pts = [(100, 100), (300, 200), (400, 100), (300, 400), (150, 300)]

def setup():
    py5.size(512, 512, py5.P3D)
    py5.color_mode(py5.HSB)
    animated_gif('out.gif', duration=0.2, frame_numbers=range(1, 361, 5))

def draw():
    py5.background(240)
    py5.no_fill()
    ang = py5.radians(py5.frame_count)
    hatch_poly(pts, ang, spacing=10)
    draw_poly(pts)
    
py5.run_sketch(block=False)

