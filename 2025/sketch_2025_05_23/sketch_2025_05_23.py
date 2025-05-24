import py5
from py5_tools import animated_gif

from shapely import Polygon, LineString, MultiLineString

from villares.geometry_helpers import Line, lerp_tuple, rotate_point, rect_points

pts = [(100, 100), (300, 200), (400, 100), (300, 400), (150, 300)]
hole = [ (250, 200), (200, 200), (200, 250),  (250, 250)]

def setup():
    py5.size(512, 512)
    animated_gif('out.gif', duration=0.2, frame_numbers=range(1, 361, 10))

def draw():
    py5.background(240)
    
    py5.fill(255, 200)
    py5.stroke(0, 0, 200)
    draw_poly(pts, [hole])
    
    py5.stroke(200, 0, 0)        
    py5.no_fill()
    hatch_poly(
        pts, holes=[hole],
        angle=py5.radians(py5.frame_count),
        spacing=10
    )

def draw_poly(pts, holes=[]):
    py5.shape(py5.convert_cached_shape(Polygon(pts, [hole])))

# WIP converting old hatch function... 
def hatch_poly(pts, angle=0, holes=[], spacing=5):
    p = Polygon(pts, holes)
    cx, cy = p.centroid.x, p.centroid.y
    d = py5.dist(*p.bounds)  # diagonal length
    num = int(d / spacing)
    rr = [rotate_point(x, y, angle, cx, cy)
          # square with side length of d (bounding box diagonal)
          for x, y in rect_points(cx, cy, d, d, mode=py5.CENTER)]
    py5.stroke(0, 255, 0)   # debug mode
    ab = Line(rr[0], rr[1])   ;ab.draw()  # debug mode
    cd = Line(rr[3], rr[2])   ;cd.draw()  # debug mode
    lines = []
    for i in range(num + 1):
        abp = ab.line_point(i / float(num))  # + EPSILON)
        cdp = cd.line_point(i / float(num))  # + EPSILON)
        ls = LineString((abp, cdp))
        lines.append(ls)
    py5.stroke(200, 0, 0)
    mls = MultiLineString(lines)
    hatch = mls.intersection(p)
    py5.shape(py5.convert_cached_shape(hatch))

def key_pressed():
    py5.save('out.png')

py5.run_sketch(block=False)

