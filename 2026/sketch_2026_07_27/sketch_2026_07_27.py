import py5

from py5_tools import animated_gif
from shapely import Point, Polygon
from itertools import product

def setup():
    global p
    py5.size(640, 640)
    py5.no_smooth()
    p = Point(256, 256).buffer(128) | Point(384, 384).buffer(128)

    animated_gif('out.gif', frame_numbers=range(1, 141), duration=0.1)

    
def draw():
    #py5.background(100, 100, 128)
    py5.no_fill()
    py5.stroke(0)
    py5.stroke_weight(1)
#     for x, y in product(range(10, 640, 20), repeat=2):
#         py5.circle(x, y, 10 + (x + y) / 20)
#     py5.stroke(255)
#     for x, y in product(range(10, 640, 20), repeat=2):
#         py5.circle(x, y, 10 + (x - y) / 20)        
    t = py5.frame_count / 120
    v = p.exterior.interpolate(t, normalized=True)
    r1 = 20
    r2 = 100
    buffer = 15 * py5.cos((t + 0.5) * py5.TWO_PI)
    
    if t <= 1:
        py5.shape(star(v.x, v.y, 4, r1, r2, buffer))


def star(x, y, n, ra, rb, buffer=0, rot=0):    
    passo = py5.TWO_PI / n
    vs = [] 
    for i in range(n): 
        angulo = i * passo + rot
        vx = x + ra * py5.sin(angulo)
        vy = y + ra * py5.cos(angulo)
        vs.append((vx, vy))
        vx = x + rb * py5.sin(angulo + passo / 2)
        vy = y + rb * py5.cos(angulo + passo / 2)
        vs.append((vx, vy)) 
    return Polygon(vs).buffer(buffer)

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
