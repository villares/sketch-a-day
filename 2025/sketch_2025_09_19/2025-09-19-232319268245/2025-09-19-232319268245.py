
import py5
from py5 import sqrt, sin, cos, PI, TAU, HALF_PI

def setup():
    py5.size(600, 600)
    py5.color_mode(py5.CMAP, py5.mpl_cmaps.TWILIGHT, 7)
    py5.no_stroke()
    
def draw():
    py5.background(7)
    w = 50
    for x in range(11):
        for y in range(11):
            unit(w + x * w,
                 w + y * w, w)
        
def unit(x, y, w):
    # w = r * 2 + r * 2 / (1 + sqrt(2))
    r = w / (2 * sqrt(2))  # octagon inradius
    s = r * 2 / (1 + sqrt(2)) # sq side
    # squ(x, y, w)  # visual debug
    py5.random_seed(int(x * y))
    offset = - r * sqrt(2) / 2
    rot = py5.random_choice((0, 1, 2, 3))
    oct(x + offset, y + offset, r, rot)
    squ(x + r + s / 2 + offset,
           y + offset, s)
    oct(x + w / 2 + offset, y + w / 2 + offset, r, rot)
    squ(x - r - s / 2 + w / 2 + offset,
           y + w / 2 + offset, s)
    # py5.circle(x, y, 5)  # visual debug
    
def squ(x, y, s):
    py5.quad(
        x - s / 2, y - s / 2,
        x + s / 2, y - s / 2,
        x + s / 2, y + s / 2,
        x - s / 2, y + s / 2
    )

def oct(x, y, r, rot):
    s = r * 2 / (1 + sqrt(2)) # sq side
    R = r / cos(PI / 8) # circumradius
    ang = TAU / 8
    vs = [(cos(i * ang + ang / 2) * R,
           sin(i * ang + ang / 2) * R)
           for i in range(8)]
    with py5.push_matrix():
        py5.translate(x, y)
        py5.rotate(rot * HALF_PI)
        x0, y0 = vs[0]    
        x2, y2 = vs[2]
        x7, y7 = vs[7]
        with py5.begin_closed_shape(py5.QUAD):
            py5.fill(0)
            py5.vertices((vs[0], vs[1], vs[2], (x0-s, y0)))
            py5.fill(1)
            py5.vertices((vs[0], (x0-s, y0), (x7-s, y7), vs[7]))
            py5.fill(2)
            py5.vertices((vs[7], (x7-s, y7), vs[5], vs[6]))
            py5.fill(3)
            py5.vertices((vs[2], vs[3], vs[4], (x2, y2-s)))
            py5.fill(4)
            py5.vertices(((x2, y2-s), vs[4],vs[5], (x7-s, y7)))
            py5.fill(5)
            py5.vertices(((x2, y2-s), (x7-s, y7), (x0-s, y0), vs[2]))
       

def key_pressed():
    if py5.key == 's':
        save_snapshot_and_code()
    
def save_snapshot_and_code():
    import shutil
    import datetime
    p = py5.sketch_path()
    stamp = str(datetime.datetime.now()).replace(' ', '-').replace(':', '').replace('.', '')    
    py5.save(p / stamp / (stamp + '.png')) 
    shutil.copyfile(__file__, p / stamp / (stamp + '.py'))
    #py5.save(stamp + '.png')

py5.run_sketch()