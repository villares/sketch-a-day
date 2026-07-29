import py5

from py5_tools import animated_gif
from shapely import Point, Polygon
from itertools import product

def setup():
    global p
    py5.size(640, 640, py5.P3D)
    py5.no_smooth()
    p = Point(256 + 25, 256 + 25).buffer(128) | Point(384 + 50, 384 + 50).buffer(128)
    py5.color_mode(py5.CMAP, 'plasma')
    animated_gif('out.gif', frame_numbers=range(1, 181, 3), duration=0.15)
    py5.background(float('nan'))

    
def draw():
    py5.background('black')
    py5.stroke_weight(2)
    py5.translate(py5.width / 2, py5.height / 2, -150)
    py5.rotate_y(py5.radians(py5.frame_count * 2))
    py5.translate(-py5.width / 2, -py5.height / 2)    
    for t in (i / 120 for i in range(120)):
        v = p.exterior.interpolate(t, normalized=True)
        buffer = 15 * py5.sin((t) * py5.TWO_PI)
        r1 = 100
        r2 = 40 + buffer
        rot = t * py5.TWO_PI * 3    
        py5.fill(t)
        py5.shape(star(v.x, v.y, 5, r1, r2, buffer, rot))
        py5.translate(0, 0, 2)

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
