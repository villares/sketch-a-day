# Using py5coding.org (Processing + Python) and shapely
# you'll need to install py5 and shapely

from shapely.geometry import Polygon, MultiPolygon, GeometryCollection, LineString, Point
from shapely.geos import TopologicalError
from shapely.ops import unary_union

from villares.helpers import save_png_with_src

solid = []
holes = []
boxes = []
seed = 100

def setup():
    size(1000, 500)
    no_stroke()
    prepare(rs=seed)
    
def prepare(big=110, small=90, n=40, rs=1):
    random_seed(rs)
    print(f'random seed: {rs}')
    solid[:] = []
    holes[:] = []
    boxes[:] = []
    for _ in range(n):
        x = 10 * int(random(big, width - big) / 10)
        y = 10 * int(random(big, height - big) / 10) 
        solid.append(Polygon(box_pts(x, y, big)))
        holes.append(Polygon(box_pts(x, y, small)))
        small_box = list(reversed(box_pts(x, y, small)))
        boxes.append(Polygon(box_pts(x, y, big),
                             holes=[small_box]).buffer(10))

def draw():
    background(0, 0, 200)
    fill(255, 64)
    draw_elements(boxes)
    solid_union = unary_union(solid)
    clipped_result = solid_union.difference(unary_union(holes))
    fill(0)
    draw_elements(clipped_result)

    
def draw_elements(element):
    if isinstance(element, (MultiPolygon, GeometryCollection)):
        for p in element.geoms:
            draw_elements(p)
    elif isinstance(element, Polygon):
        with begin_closed_shape():
            #if element.exterior.coords:
            vertices(element.exterior.coords)
            for hole in element.interiors:
                with begin_contour():
                    vertices(hole.coords)        
    elif isinstance(element, list):
        for p in element:
            draw_elements(p)
    elif isinstance(element, LineString):
        stroke(255, 0, 0)
        (xa, ya), (xb, yb) = element.coords
        line(xa, ya, xb, yb)
        no_stroke()
    elif isinstance(element, Point):
        with push_style():
            fill(255, 0, 0)
            x, y = element.coords[0]
            circle(x, y, 15)
    else:
        print(element)
#     else:  # legacy code tuple/points
#         with begin_closed_shape():
#             vertices(element)
                       
def key_pressed():
    if key == ' ':
        global seed
        seed += 1
        prepare(rs=seed)
    elif key == 's':
        save_png_with_src(f'{seed}')

def box_pts(x, y, w, h=None, **kwargs):
    hw = w / 2
    hh = h / 2 if h else w / 2
    return [
        (x - hw, y - hh),
        (x + hw, y - hh),
        (x + hw, y + hh),
        (x - hw, y + hh),
        ]
