# Not exactly what I wanted (like the year 2024 itself)
from itertools import product

import py5
from shapely import Polygon
from scipy.spatial import Voronoi

def setup():
    global imga, imgb, f
    py5.size(600, 600)
    py5.color_mode(py5.HSB)
    f = py5.create_font('Tomorrow Bold', 200)
    imga = py5.create_graphics(600, 600)
    imga.begin_draw()
    imga.text_font(f)
    imga.text_align(py5.CENTER, py5.CENTER)
    imga.text('2024', 300, 300)
    imga.end_draw()
    imgb = py5.create_graphics(600, 600)
    imgb.begin_draw()
    imgb.text_font(f)
    imgb.text_align(py5.CENTER, py5.CENTER)
    imgb.text('2025', 300, 300)
    imgb.end_draw()
    new_points()
    
def new_points():
    global seed_points, shapely_regions, colors
    R = 5
    W = 30
    seed_points = []
    for i in range(4):
        seed_points.extend((x + (i - 1) * py5.random(-R, R),
                            y + i * py5.random(-R, R)) for x, y
                           in product(range(0, py5.width + W, W),
                                      range(0, py5.height+ W, W)))
    shapely_regions, colors = generate_regions(seed_points, py5.width, py5.height)

def generate_regions(seed_points, w, h):
    # add 4 points far from the visible region
    extended_points = seed_points.copy()
    extended_points.extend([
         (-w/2, -h/2),
         (w * 1.5, -h/2),
         (w * 1.5, h * 1.5),
         (-w/2, h * 1.5)
         ])
    voronoi = Voronoi(extended_points)
    shapely_regions = []
    for vs in voronoi.regions:
        if vs and -1 not in vs:
            shapely_regions.append(
                Polygon(voronoi.vertices[index] for index in vs if index != -1)
            )
    colors = []
    for i, r in enumerate(shapely_regions):
        a = imga.get_pixels(int(r.centroid.x), int(r.centroid.y))
        b = imgb.get_pixels(int(r.centroid.x), int(r.centroid.y))
        ca = py5.color(8 * len(r.exterior.coords), 150, 100) if a == -1 else py5.color(100)
        cb = py5.color(16 * len(r.exterior.coords), 200, 200) if b == -1 else py5.color(100)
        colors.append((ca, cb))
    return shapely_regions, colors

def draw():
    t = 1 #py5.remap(py5.mouse_x, 0, py5.width, 0, 1)
    py5.stroke(0)
    for s, (ca, cb) in zip(shapely_regions, colors):
        cc = py5.lerp_color(ca, cb, t)
        py5.fill(cc)
        py5.shape(py5.convert_cached_shape(s))


def key_pressed():
    if py5.key == ' ':
        new_points()
    elif py5.key == 's':
        py5.save_frame('out###.png')
    
            
py5.run_sketch(block=False)

