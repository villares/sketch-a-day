from itertools import product

import py5
from shapely import Polygon, LineString, MultiLineString
from scipy.spatial import Voronoi

def setup():
    global offscreen_text, f
    py5.size(600, 600)
    py5.color_mode(py5.HSB)
    f = py5.create_font('Tomorrow Bold', 300)
    offscreen_text = py5.create_graphics(600, 600)
    offscreen_text.begin_draw()
    offscreen_text.text_font(f)
    offscreen_text.text_align(py5.CENTER, py5.CENTER)
    offscreen_text.text_leading(250)
    offscreen_text.text('20\n25', 300, 300)
    offscreen_text.end_draw()
    new_points()
    
def new_points():
    global seed_points, regions
    R = 3
    W = 30
    seed_points = []
    for i in range(2):
        seed_points.extend((x + (i - 1) * py5.random(-R, R),
                            y + i * py5.random(-R, R)) for x, y
                           in product(range(0, py5.width + W, W),
                                      range(0, py5.height+ W, W)))
    regions = generate_regions(seed_points, py5.width, py5.height)

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
    shapely_regions = (
        Polygon(voronoi.vertices[index] for index in vs if index != -1)
        for vs in voronoi.regions if vs and -1 not in vs
        )
    colored_regions = []
    for r in shapely_regions:
        px = offscreen_text.get_pixels(int(r.centroid.x), int(r.centroid.y))
        if px == -1:
            stroke_color = py5.color(16 * len(r.exterior.coords), 200, 200)
            shp = random_hatch(r)
            colored_regions.append((shp, stroke_color))
    return colored_regions

def random_hatch(region):
    ix, iy, fx, fy = region.bounds
    step = py5.random_choice((3, 4, 5, 6, 7, 8))
    if step % 2 == 0:
        hatch = MultiLineString([LineString([(x, iy), (x, fy)])
                                 for x in range(int(ix), int(fx) + 1, step)])
    else:
        hatch = MultiLineString([LineString([(ix, y), (fx, y)])
                                 for y in range(int(iy), int(fy) + 1, step)])
    return region.intersection(hatch)

def draw():
    py5.background(0)
    for shp, stroke_color in regions:
        py5.stroke(stroke_color)
        py5.shape(py5.convert_cached_shape(shp))


def key_pressed():
    if py5.key == 's':
        py5.save_frame('out###.png')
        new_points()

py5.run_sketch(block=False)

