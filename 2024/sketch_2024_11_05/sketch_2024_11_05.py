# You'll need py5 and a use the run_sketch tool or Thonny+thonny-py5mode
# to run this py5 "imported mode" style sketch. Learn more at py5coding.org

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
    stroke(0, 0, 200)
    unit(+r * 2, 0, R)
    unit(-r * 2, 0, R)
    stroke(255)
    unit(0, 0, R)
    stroke(128)
    hexagon(+r, -R * 3 / 2, rbh, False)
    hexagon(-r, -R * 3 / 2, rbh, False)
    hexagon(+r, +R * 3 / 2, rbh, False)
    hexagon(-r, +R * 3 / 2, rbh, False)
    hexagon(0, 0, rbh, False)
    hexagon(+r * 2, 0, rbh, False)
    hexagon(-r * 2, 0, rbh, False)
    #unit(0, 0, R * 3 / 2, False)


def unit(xu, yu, ru, pointy=True, N=1, M=5): 
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
    elif key == 's':
        save(__file__[:-3]+'.png')
