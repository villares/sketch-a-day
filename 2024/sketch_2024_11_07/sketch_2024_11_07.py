# You'll need py5 and a use the run_sketch tool or Thonny+thonny-py5mode
# to run this py5 "imported mode" style sketch. Learn more at py5coding.org

R = 50
ROWS = 13
COLS = 12

save_pdf = False

def setup():
    size(900, 900)
    
def draw():
    background(200, 240, 240)  # background not included on PDF export!
    
    global save_pdf    
    if save_pdf:
        begin_record(PDF, __file__[:-3]+'.pdf')
    
    stroke_weight(2)
    no_fill()
    w = R * sqrt(3)
    h = R * 1.5
    for row in range(ROWS):
        y = row * h
        for col in range(COLS):
            x = col * w
            if row % 2 == 1:
                x += w / 2
            hex_unit(x, y, R)
   
    if save_pdf:
        end_record()
        save_pdf = False
        print('PDF saved.')
   
def hex_unit(xu, yu, r, pointy=False):
    big_hex_radius = r * sqrt(3) / 2 * sqrt(2)
    draw_hexagon(xu, yu, big_hex_radius, pointy)  # big hexagon
    vs = hexagon_points(xu, yu, r, not pointy) # centers for smaller hexs
    for x, y in vs[2:4]:  # just the third and fourth (indices 2 and 3)
        draw_hexagon(x, y, r / 2, not pointy)  # smaller hexagons
        
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
    global save_pdf
    if key == 'S':
        save_snapshot_and_code()
    elif key == 's':
        save(__file__[:-3]+'.png')
        print('PNG saved.')
    elif key == 'p':
        save_pdf = True
    
   
try:
    from villares.helpers import save_snapshot_and_code
except ImportError:
    def save_snapshot_and_code():
        print('missing the snapshot helper from github.com/villares/villares')
