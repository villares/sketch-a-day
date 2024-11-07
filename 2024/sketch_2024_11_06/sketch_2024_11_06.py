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
    w = R * sqrt(3)
    h = R * 1.5
    main_radius = w / 2 * sqrt(2)

    rows = 3
    cols = 3
    for row in range(rows):
        y = (row - 1) * h
        for col in range(cols):
            x = (col - 1) * w
            if row % 2 == 1:
                x += w / 2
            hex_unit(x, y, main_radius)
    

#     r = R * sqrt(3) / 2
#     hex_unit(+r, -R * 3 / 2, main_radius)
#     hex_unit(-r, -R * 3 / 2, main_radius)
#     hex_unit(+r, +R * 3 / 2, main_radius)
#     hex_unit(-r, +R * 3 / 2, main_radius)
#     hex_unit(0, 0, main_radius)
#     hex_unit(+r * 2, 0, main_radius)
#     hex_unit(-r * 2, 0, main_radius)
   

def hex_unit(xu, yu, ru, pointy=False):
    draw_hexagon(xu, yu, ru, pointy)  # big hexagon
    sur = 2  * ru / sqrt(2) / sqrt(3)
    vs = hexagon_points(xu, yu, sur, not pointy)
    for x, y in vs[2:4]:
        draw_hexagon(x, y, sur / 2, not pointy)  # smaller hexagons
        
def draw_hexagon(x, y, r, pointy=True):
    vs = regular_polygon_points(x, y, r, 6, pointy)
    with begin_closed_shape():
            vertices(vs)

def hexagon_points(x, y, cr, pointy=True):
    # returns a list of tuples for the coords of vertices of hexagon
    return regular_polygon_points(x, y, cr, 6, pointy)

def regular_polygon_points(x, y, cr, n, pointy=True):
    # cr is the circumradius
    ang = TAU / n
    return [(x+cos(i * ang + pointy * ang / 2) * cr,
             y+sin(i * ang + pointy * ang / 2) * cr)
           for i in range(n)]


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
