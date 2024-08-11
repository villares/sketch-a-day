# You'll need py5 and a use the run_sketch tool or Thonny + thonny-py5mode
# to run this py5 "imported mode" style sketch. Learn more at py5coding.org

def setup():
    size(600, 600)
    rect_mode(CENTER)
    color_mode(HSB)
    
def draw():
    background(0)
    w = 200
    for x in range(-1, 3):
        for y in range(-1, 3):
            unit(w + x * w,
                 w + y * w, w)
        
def unit(x, y, w):
    # w = r * 2 + r * 2 / (1 + sqrt(2))
    r = w / (2 * sqrt(2))  # octagon inradius
    s = r * 2 / (1 + sqrt(2)) # square side
    # square(x, y, w)  # visual debug
    random_seed(int(x * y))
    offset = - r * sqrt(2) / 2
    rot = random_choice((0, 1, 2, 3))
    oct(x + offset, y + offset, r, rot)
    sub_quad(x + r + s / 2 + offset,
           y + offset, s)
    oct(x + w / 2 + offset, y + w / 2 + offset, r, rot)
    sub_quad(x - r - s / 2 + w / 2 + offset,
           y + w / 2 + offset, s)
    # circle(x, y, 5)  # visual debug
    

            
def triangulate(pts):
    xs, ys = tuple(zip(*pts))
    xc, yc = sum(xs) / len(xs), sum(ys) / len(ys)
    triangles = []
    for i, (x, y) in enumerate(pts):
        x0, y0 = pts[i-1]
        triangles.append(((x, y), (x0, y0), (xc, yc)))
    return triangles


def sub_tri(poly_pts):
    for a, b, c in triangulate(poly_pts):
        for sa, sb, sc in triangulate((a, b, c)):
            fill(64 + sa[0] % 128, 255, 128 + sb[0]  % 128)
            triangle(*sa, *sb, *sc)

def sub_quad(x, y, s):
#     for tri in triangulate((
#         (x-s/2, y-s/2), (x+s/2, y-s/2),
#         (x+s/2, y+s/2), (x-s/2, y+s/2)
#         )):
#         sub_tri(tri)
    sub_tri((
        (x-s/2, y-s/2), (x+s/2, y-s/2),
        (x+s/2, y+s/2), (x-s/2, y+s/2)
        ))

def oct(x, y, r, rot):
    s = r * 2 / (1 + sqrt(2)) # square side
    R = r / cos(PI / 8) # circumradius
    ang = TAU / 8
    vs = [(cos(i * ang + ang / 2) * R,
           sin(i * ang + ang / 2) * R)
           for i in range(8)]
    with push_matrix():
        translate(x, y)
        rotate(rot * HALF_PI)
        x0, y0 = vs[0]    
        x2, y2 = vs[2]
        x7, y7 = vs[7]
        sub_tri((vs[0], vs[1], vs[2], (x0-s, y0)))
        sub_tri((vs[0], (x0-s, y0), (x7-s, y7), vs[7]))
        sub_tri((vs[7], (x7-s, y7), vs[5], vs[6]))
        sub_tri((vs[2], vs[3], vs[4], (x2, y2-s)))
        sub_tri(((x2, y2-s), vs[4],vs[5], (x7-s, y7)))
        sub_tri(((x2, y2-s), (x7-s, y7), (x0-s, y0), vs[2]))

# def oct_original(x, y, r):
#     # inradius
#     # r = R * cos(PI / 8)
#     R = r / cos(PI / 8) # circumradius
#     ang = TAU / 8
#     with begin_closed_shape():
#         for i in range(8):
#             vx = x + cos(i * ang + ang / 2) * R 
#             vy = y + sin(i * ang + ang / 2) * R
#             vertex(vx, vy)

def key_pressed():
    save_snapshot_and_code()
    
def save_snapshot_and_code():
    import shutil
    import datetime
    p = sketch_path()
    stamp = str(datetime.datetime.now()).replace(' ', '-').replace(':', '').replace('.', '')    
    #save(p / stamp / (stamp + '.png')) 
    #shutil.copyfile(__file__, p / stamp / (stamp + '.py'))
    save(stamp + '.png')