#! /home/villares/thonny-env/bin/python3
# You'll need to install py5 and shapely
# Learn more at py5coding.org
# Press SPACE for a new palette

import py5
from shapely import Polygon
from random import shuffle

OFFSET = 0
BACKGROUND_COLOR = 0
palette = []

def setup():
    py5.size(1200, 600)
    py5.no_loop()
    py5.stroke_weight(0.5)
        
def draw():
    py5.background(BACKGROUND_COLOR)
    new_palette(BACKGROUND_COLOR)
    r = 75
    h = r * py5.sqrt(3)
    w = r * 3 / 2
    #hex_unit(600, 300, 120, py5.radians(90))
    for i in range(-5, 7):
        x = py5.width / 2 + i * w
        #if (i + 2) % 2 == 0:
        shuffle(palette)
        for j in range(-3, 3):
            y = py5.height / 2 + j * h + (h / 2) * (i % 2)
            hex_unit(x, y, r, py5.radians(90))

def hex_unit(xu, yu, ru, ang=0): 
    vs = regular_poly_points(xu, yu, ru / py5.sqrt(3), 6, ang)
    for i, (x, y) in enumerate(vs):
        tri_unit(x, y, ru /  py5.sqrt(3), ang + py5.radians(60) * (i + 1),
                 #i % 2 #if py5.is_mouse_pressed else 0
                 )

def tri_unit(x, y, r, angle=0, n=0):
    evs = regular_poly_points(x, y, r, 3, angle)
    main_tris = triangulate2(evs)
    for n, main_tri in enumerate(main_tris):
        tris = triangulate2(main_tri)
        for i, tri in enumerate(tris):
    #for i, tri in enumerate(main_tris):
            py5.fill(palette[(i + n) % 6])
            py5.stroke(palette[(i + n) % 6])
            tp = Polygon(tri).buffer(OFFSET)
            draw_shapely(tp)
            

def draw_shapely(obj):
    shp = py5.convert_cached_shape(obj)
    shp.disable_style()
    py5.shape(shp)

def regular_poly_points(x, y, cr, n, rot=0):
    # cr is the circumradius
    ang = py5.TAU / n
    return [(x + py5.cos(i * ang + rot) * cr,
             y + py5.sin(i * ang + rot) * cr)
            for i in range(n)]

def triangulate(pts):
    xs, ys = tuple(zip(*pts))
    xc, yc = sum(xs) / len(xs), sum(ys) / len(ys)
    triangles = []
    for i, (x, y) in enumerate(pts):
        x0, y0 = pts[i-1]
        triangles.append(((x, y), (x0, y0), (xc, yc)))
    return triangles

def triangulate2(pts):
    triangles = []
    mid_points = []
    for i, (x1, y1) in enumerate(pts):
        x0, y0 = pts[i - 1]
        xm, ym = (x0 + x1) / 2, (y0 + y1) / 2
        mid_points.append((xm, ym))
    triangles.append(mid_points)
    for i, ((x, y), (xm1, ym1)) in enumerate(zip(pts, mid_points)):
        xm0, ym0 = mid_points[i - 2]
        triangles.append(((xm0, ym0), (x, y), (xm1, ym1)))
    return triangles


def new_palette(bgd_color):
    rnd_palette = [
    py5.color(py5.random_int(0, 2) * 127,
              py5.random_int(0, 2) * 127,
              py5.random_int(0, 2) * 127)
    for _ in range(5)] + [bgd_color]
    palette[:] = py5.random_sample(rnd_palette * 2, 6)

def key_pressed():
    if py5.key == ' ':
        new_palette(BACKGROUND_COLOR)
        py5.redraw()
    elif py5.key == 'S':
        save_snapshot_and_code()
    elif py5.key == 's':
        py5.save(__file__[:-3]+'.png')
    
def save_snapshot_and_code():
    import shutil
    from py5 import sketch_path, Path, save
    path = sketch_path()
    has_image = Path(__file__[:-3]+'.png').is_file()
    number = len(list(path.iterdir())) - has_image
    snap_name = f'{number:03d}'  # 001, 002 ....
    save(path / snap_name / (snap_name + '.png')) 
    shutil.copyfile(__file__, path / snap_name / (snap_name + '.py'))


import thonny
thonny.get_runner()
py5.run_sketch(block=False) 