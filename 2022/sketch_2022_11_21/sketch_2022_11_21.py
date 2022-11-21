# Using py5coding.org (Processing + Python) and shapely
# you'll need to install py5 and shapely

from shapely.geometry import Polygon, MultiPolygon
from shapely.geos import TopologicalError
from shapely.ops import unary_union

solid = []
holes = []
boxes = []

def setup():
    size(1000, 500)
    no_stroke()
    prepare()
    
def prepare(big=130, small=100):
    solid[:] = []
    holes[:] = []
    boxes[:] = []
    for _ in range(50):
        x, y = random(big, width - big), random(big, height - big)
        solid.append(Polygon(box_pts(x, y, big)))
        holes.append(Polygon(box_pts(x, y, small)))
        boxes.append(Polygon(box_pts(x, y, big),
                             holes=[box_pts(x, y, small)]))

def draw():
    background(0, 64, 128)
    intersections = []
    for b in boxes:
        for other in boxes:
            if b is not other:
                intersection_result = b.intersection(other)
                if intersection_result:
                    intersections.append(intersection_result)
            else:
                break
    fill(255, 128, 0, 128)
    draw_elements(intersections)
    solid_union = unary_union(solid)
    clipped_result = solid_union.difference(unary_union(holes))
    fill(255)
    draw_elements(clipped_result)

def draw_elements(element):
    if isinstance(element, MultiPolygon):
        for p in element.geoms:
            draw_elements(p)
    elif isinstance(element, Polygon):
        with begin_closed_shape():
            vertices(element.exterior.coords)
            for hole in element.interiors:
                with begin_contour():
                    vertices(hole.coords)        
    elif isinstance(element, list):
        for p in element:
            draw_elements(p)
    else:  # legacy code tuple/points
        with begin_closed_shape():
            vertices(element)
                       
def key_pressed():
    prepare()

def box_pts(x, y, w, h=None, **kwargs):
    hw = w / 2
    hh = h / 2 if h else w / 3
    return [
        (x - hw, y - hh),
        (x + hw, y - hh),
        (x + hw, y + hh),
        (x - hw, y + hh),
        ]