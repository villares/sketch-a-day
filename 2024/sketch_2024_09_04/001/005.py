#! /home/villares/thonny-env/bin/python3
# You'll need to install py5 and shapely
# Learn more at py5coding.org
# Press SPACE for a new palette

import py5
from shapely import Polygon

OFFSET = -2
BACKGROUND_COLOR = 0
palette = []

def setup():
    py5.size(1400, 600)
    py5.no_loop()
        
def draw():
    py5.background(BACKGROUND_COLOR)
    new_palette(BACKGROUND_COLOR)
    py5.no_stroke()
    r = 75
    h = r * py5.sqrt(3)
    w = r * 3 / 2
    for i in range(-5, 7):
        x = py5.width / 2 + i * w
        if (i + 2) % 3 == 0:
            new_palette(BACKGROUND_COLOR)
        for j in range(-3, 3):
            y = py5.height / 2 + j * h + (h / 2) * (i % 2)
            hex_unit(x, y, r, py5.radians(90))

def hex_unit(xu, yu, ru, ang=0): 
    vs = regular_poly_points(xu, yu, ru / py5.sqrt(3), 6, ang)
    for i, (x, y) in enumerate(vs):
        tri_unit(x, y, ru /  py5.sqrt(3), ang + py5.radians(60) * (i + 1),
                 i if py5.is_mouse_pressed else 0)

def tri_unit(x, y, r, angle=0, n=0):
    evs = regular_poly_points(x, y, r, 3, angle)
    ivs = regular_poly_points(x, y, r / 4, 3, angle)
    py5.fill(palette[n % 2- 2])
    central_triangle = Polygon(ivs).buffer(OFFSET)
    draw_shapely(central_triangle)
    for i in range(3):
        sax, say = evs[i]
        sbx, sby = evs[i - 1]
        scx, scy = evs[i - 2]
        a = py5.lerp(sax, sbx, 1/4), py5.lerp(say, sby, 1/4)
        b = py5.lerp(sax, sbx, 3/4), py5.lerp(say, sby, 3/4)
        c = ivs[i - 1]
        d = ivs[i]
        py5.fill(palette[(i + n) % 5])
        trapezoid = Polygon((a, b, c, d)).buffer(OFFSET)
        draw_shapely(trapezoid)
        e = evs[i-1]
        f = py5.lerp(sbx, scx, 1/4), py5.lerp(sby, scy, 1/4)
        g = c
        h = b
        py5.fill(palette[n % 2 - 1])        
        diamond = Polygon((e, f, g, h)).buffer(OFFSET)
        draw_shapely(diamond)

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

def new_palette(bgd_color):
    rnd_palette = [
    py5.color(py5.random_int(0, 2) * 127,
              py5.random_int(0, 2) * 127,
              py5.random_int(0, 2) * 127)
    for _ in range(5)] #+ [bgd_color]
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