# You'll need py5 and a use the run_sketch tool or Thonny + thonny-py5mode
# to run this py5 "imported mode" style sketch. Learn more at py5coding.org

def setup():
    size(600, 600)
    rect_mode(CENTER)
    
def draw():
    background(0)
    w = 100
    for x in range(5):
        for y in range(5):
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
    square(x + r + s / 2 + offset,
           y + offset, s)
    oct(x + w / 2 + offset, y + w / 2 + offset, r, rot)
    square(x - r - s / 2 + w / 2 + offset,
           y + w / 2 + offset, s)
    # circle(x, y, 5)  # visual debug
    


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
#         line(x0-s, y0, x0, y0)
#         line(x2, y2-s, x2, y2)
#         line(x7-s, y7, x7, y7)
#         circle(x7, y7, 10)
        with begin_closed_shape(QUAD):
            fill(200, 0, 0)
            vertices((vs[0], vs[1], vs[2], (x0-s, y0)))
            fill(0, 200, 0)
            vertices((vs[0], (x0-s, y0), (x7-s, y7), vs[7]))
            fill(200, 0, 200)
            vertices((vs[7], (x7-s, y7), vs[5], vs[6]))
            fill(200, 200, 0)
            vertices((vs[2], vs[3], vs[4], (x2, y2-s)))
            fill(0, 0, 200)
            vertices(((x2, y2-s), vs[4],vs[5], (x7-s, y7)))
            fill(0, 200, 200)
            vertices(((x2, y2-s), (x7-s, y7), (x0-s, y0), vs[2]))
        fill(200)

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