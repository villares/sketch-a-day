# You'll need shapely and py5 to run this py5 "module mode" style sketch.
# Learn more at https://py5coding.org

import shapely
import py5

def setup():
    py5.size(600, 600)
    py5.stroke_weight(3)
    py5.stroke_join(py5.ROUND)
    
def draw():
    py5.background(0)
    py5.fill(255, 64)
    py5.stroke(0, 0, 200)
    unit(300, 300, 180, 12, py5.radians(15))
    py5.stroke(0, 200, 0)
    unit(300, 300, 180, 6)
    unit(300, 300, 180, 6, py5.radians(60))
    
def unit(xu, yu, r, n=6, rot=0):
    vs = poly_points(xu, yu, r, n, rot)
    unit_vs = []
    for i, (x, y) in enumerate(vs):
        svs = poly_points(x, y, r / 2, n, rot)
        with py5.push_style():
            py5.no_fill()
            with py5.begin_closed_shape():
                py5.vertices(svs)
        if i % 2 == 0:
            unit_vs.append(svs[(n//2+i)%n])
        else:
            for j in range(n-1, n+2): #5, 8):
                unit_vs.append(svs[(i + j) % len(svs)])
#     with py5.begin_closed_shape():
#         py5.vertices(unit_vs)
    p = shapely.geometry.Polygon(unit_vs)
    op = p.buffer(-r / 5)
    py5.shape(py5.convert_shape(p - op))
    
    
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