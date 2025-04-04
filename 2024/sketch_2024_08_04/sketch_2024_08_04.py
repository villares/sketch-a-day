# You'll need shapely and py5 to run this py5 "module mode" style sketch.
# Learn more at https://py5coding.org
from itertools import product
import shapely
import py5

def setup():
    py5.size(550, 550)
    py5.stroke_weight(3)
    py5.stroke_join(py5.ROUND)
    py5.background(0)
    sshp2 = unit(0, 0, 100, 6)
    sshp3 = unit(0, 0, 100, 6, py5.radians(60))
    main_shape = sshp2 | sshp3
    py5.no_stroke()
    py5.fill(255, 64)
    for i, j in product(range(3), repeat=2):
        w, h = 152, 178
        x = w + i * w
        y = j * h + (h if i % 2 else h / 2) 
        py5.shape(py5.convert_cached_shape(main_shape), x, y)

def unit(xu, yu, r, n=6, rot=0):
    py5.stroke(0, 0, 100)
    vs = poly_points(xu, yu, r, n, rot)
    unit_vs = []
    for i, (x, y) in enumerate(vs):
        svs = poly_points(x, y, r / 2, n, rot)
        if i % 2 == 0:
            unit_vs.append(svs[(n//2+i)%n])
        else:
            for j in range(n-1, n+2): #5, 8):
                unit_vs.append(svs[(i + j) % len(svs)])
    p = shapely.geometry.Polygon(unit_vs)
    op = p.buffer(-r / 5, join_style=2)
    # join_style 1 "round" 2 "mitre" 3 "bevel"
    return p - op
    
    
def poly_points(x, y, cr, n=6, rot=0):
    from py5 import TAU, sin, cos
    # cr is the circumradius for hex
    # ir = cr * cos(TAU / 12)  # to be confirmed
    # a = cr * 2 * sin(TAU / 12) # to be confirmed
    ang = TAU / n
    return [(x + cos(i * ang + ang / 2 + rot) * cr,
             y + sin(i * ang + ang / 2 + rot) * cr)
           for i in range(n)]

def key_pressed():
    py5.save_frame('out.png')

py5.run_sketch()