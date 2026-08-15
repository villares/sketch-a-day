import py5

from py5_tools import animated_gif

from itertools import product

def setup():
    global p
    py5.size(640, 640, py5.P3D)
    py5.no_smooth()
    py5.color_mode(py5.HSB)
    #animated_gif('out.gif', frame_numbers=range(1, 101), duration=0.1)
    
    
def draw():
    py5.translate(320, 320)
    py5.rotate_x(py5.radians(15))
    py5.rotate(py5.radians(-15))
    py5.translate(-320, -320, 200)
    py5.background('k')
    py5.no_stroke()
    #py5.stroke_weight(1)
    for x, y in product(range(10, 640, 20), repeat=2):
        with py5.push_matrix():
            d = 20 + py5.sin(x / 40 + y / 40) * 10
            py5.fill(d * 10, 255, 255, 100)
            py5.translate(0, 0, d)
            py5.circle(x, y, d)
    for x, y in product(range(10, 640, 20), repeat=2):
        with py5.push_matrix():
            d = 20 + py5.cos(x / 40 - y / 40) * 10
            py5.fill(d * 10, 255, 255, 100)
            py5.translate(0, 0, d)
            py5.circle(x, y, d)

        
        
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
