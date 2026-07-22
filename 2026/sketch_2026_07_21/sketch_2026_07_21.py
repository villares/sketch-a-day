import py5

from py5_tools import animated_gif
from shapely import Point


def setup():
    global p
    py5.size(640, 640)
    animated_gif('out.gif', frame_numbers=range(1, 101), duration=0.1)
    p = Point(256, 256).buffer(128) | Point(384, 384).buffer(128)
    
    
def draw():
    py5.background(100, 100, 128)
    py5.no_fill()
    py5.shape(p)
    py5.fill(255)
    #t = py5.remap(py5.mouse_x, 0, py5.width, 0, 1)
    t = py5.frame_count / 100
    v = p.exterior.interpolate(t, normalized=True) 
    py5.circle(v.x, v.y, 10)

def key_pressed():
    if py5.key == 's':
        py5.save_frame('#####.png')


def lerp_along_points(amt, pts):
    # Based on LerpVectorsExample by Jeremy Douglass
    amt = constrain(amt, 0, 1)  # let's play safe
    if len(pts) == 1:
        return pts[0]
    cunit = 1.0 / (len(pts) - 1)
    return lerp(pts[floor(amt / cunit)],
                pts[ceil(amt / cunit)],
                amt % cunit / cunit)

py5.run_sketch(block=False)