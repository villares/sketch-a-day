import math           # for math.isnan

import py5
import pymunk as pm   # the 2D physics engine
from trimesh.creation import triangulate_polygon

from shapely.affinity import translate as shapely_translate
from shapely.affinity import rotate as shapely_rotate
from shapely.affinity import scale as shapely_scale
from shapely import Point, Polygon, MultiPolygon, LineString
from shapely.ops import unary_union
from shapely import GEOSException

from villares.shapely_helpers import polys_from_text, draw_shapely

space = pm.Space()    # the pymunk simulation space
space.gravity = (0, 600)

previous_union = -1
dragged = -1
mirror = False
xo, yo = 10, 100
shapes = []

def setup():
    global letter_shapes, results
    py5.size(600, 400)
    py5.color_mode(py5.HSB)

    font = py5.create_font('Inconsolata Black', 90)
    letter_shapes = polys_from_text(
        'viva o LHC\n12 anos!',
        font, leading=90, alternate_spacing=True
        )

    for shp in letter_shapes:
        add_trianglulated_body(shapely_translate(shp, 50, 100))

    margin = 5
    text_x = margin * 2
    walls = (
        ((margin, py5.height - margin), (py5.width - margin, py5.height - margin)),
        ((margin, py5.height - margin), (margin, margin)),
        ((py5.width - margin, py5.height - margin), (py5.width - margin, margin)),
    )
    for pa, pb in walls:
        wall = pm.Segment(space.static_body, pa, pb, 2)
        wall.friction = 0.4
        space.add(wall)
    
def draw():
    global current_union, previous_union, meshes
    py5.background(0)
    for b in space.bodies:  # draws the objects
        b.draw()
        
    if py5.is_key_pressed:
        space.step(0.01)   # advance simulation

    


class DrawableBody(pm.Body):
    def draw(self):
        with py5.push():
            py5.no_stroke()
            py5.translate(self.position.x, self.position.y)
            py5.rotate(self.angle)
            a = self.position.y
            py5.fill(a % 255, 200, 200, 200)
            draw_shapely(self.poly)

# class DrawableSegment(pm.Segment):
#     def draw(self):
#         with py5.push():
#             py5.stroke(255)    
#             py5.stroke_weight(self.radius*2)
#             py5.line(self.a.x, self.a.y, self.b.x, self.b.y)  

def min_max(pts):
    coords = tuple(zip(*pts))
    return tuple(map(min, coords)), tuple(map(max, coords))

def add_trianglulated_body(poly: Polygon):
    """
    Todo, look at shapely centroid and improve
    DrawableBody class maybe to get the shapely.Poly
    Maybe passe everything t the DrawableBody class?
    """
    vs, faces = triangulate_polygon(poly)
    triangles = [(vs[a], vs[b], vs[c]) for a, b, c in faces]
    (xa, ya), (xb, yb) = min_max(vs)
    centroid = (xa + xb) / 2, (ya + yb) / 2
    cx, cy = centroid
    translated_tris = []
    total_mass = total_moi = 0
    for tri in triangles:
        translated_tri = [(x - cx, y - cy) for x, y in tri]
        mass = poly_area(translated_tri) * 0.1
        total_mass += mass
        moi = pm.moment_for_poly(mass, translated_tri)
        if not math.isnan(moi):
            total_moi += moi
        translated_tris.append(translated_tri)   
    body = DrawableBody(total_mass, total_moi)
    body.poly = shapely_translate(poly, -cx, -cy)
    body.position = centroid
    shapes = []
    for tri in translated_tris:
        shp = pm.Poly(body, tri)
        shp.friction = 0.4
        shapes.append(shp)
    #print(f'shapes: {len(shapes)}')
    space.add(body, *shapes)  # Note critical * operator expands .add(b, s0, s1, s2...)

def poly_area(pts):
    area = 0.0
    for (ax, ay), (bx, by) in zip(pts, pts[1:] + [pts[0]]):
        area += ax * by
        area -= bx * ay
    return abs(area) / 2.0

def is_poly(obj): return isinstance(obj, pm.Poly) 
def is_segment(obj): return isinstance(obj, pm.Segment) 

py5.run_sketch(block=False)

