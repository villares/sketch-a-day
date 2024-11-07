# You'll need py5 and a use the run_sketch tool or Thonny+thonny-py5mode
# to run this py5 "imported mode" style sketch. Learn more at py5coding.org
from shapely import Polygon

def setup():
    size(600, 600)
    
def draw():
    background(100)
    translate(300, 300)
    stroke_weight(3)
    no_fill()
    stroke(255)
    R = 100
    r = R * sqrt(3) / 2
    rbh =  r * sqrt(2)
    hex_unit(+r, -R * 3 / 2, rbh, False)
    hex_unit(-r, -R * 3 / 2, rbh, False)
    hex_unit(+r, +R * 3 / 2, rbh, False)
    hex_unit(-r, +R * 3 / 2, rbh, False)
    hex_unit(0, 0, rbh, False)
    hex_unit(+r * 2, 0, rbh, False)
    hex_unit(-r * 2, 0, rbh, False)
   

def hex_unit(x, y, r, pointy):
    unit(x, y, 2  * r / sqrt(2) / sqrt(3), not pointy)
    hexagon(x, y, r, pointy)


def unit(xu, yu, ru, pointy=True, N=2, M=4): 
    vs = hex_points(xu, yu, ru, pointy=pointy)
    for x, y in vs[N:M]:
        hexagon(x, y, ru / 2, pointy=pointy)
        
def hexagon(x, y, r, pointy=True):
    vs = hex_points(x, y, r, pointy)
    with begin_closed_shape():
            vertices(vs)

def hex_points(x, y, cr, pointy=True):
    # cr is the circumradius
    ang = TAU / 6
    return [(x+cos(i * ang+pointy * ang / 2) * cr,
             y+sin(i * ang+pointy * ang / 2) * cr)
           for i in range(6)]

def key_pressed():
    if key == 'S':
        save_snapshot_and_code()
    elif key == 's':
        save(__file__[:-3]+'.png')
   
try:
    from villares.helpers import save_snapshot_and_code
except ImportError:
    def save_snapshot_and_code():
        print('missing the snapshot helper from github.com/villares/villares')