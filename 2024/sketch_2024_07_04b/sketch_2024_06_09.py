import math           # for math.isnan

import py5
import pymunk as pm   # the 2D physics engine
from trimesh.creation import triangulate_polygon
from shapely.affinity import translate as shapely_translate
import shapely

from villares.shapely_helpers import polys_from_text, draw_shapely

space = pm.Space()    # the pymunk simulation space
space.gravity = (0, 600)

shapes = []
colors = []
fonts = []

def setup():
    global letter_shapes, results
    py5.size(700, 700)
    py5.color_mode(py5.HSB)
    for i in range(5):
          colors.append(py5.color(i * 255/6, 255, 255))  
    global font, text_x, margin
    for t in (360, 180, 90, 45, 30):
        font = py5.create_font('Droid Serif Bold Italic', t)
        fonts.append(font)
#     letter_shapes = polys_from_text(
#         'viva o LHC\n12 anos!',
#         font, leading=90, alternate_spacing=True
#         )
#     for shp in letter_shapes:
#         add_triangulated_body(shapely_translate(shp, 50, 100))

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
    py5.background(255)
    for b in space.bodies:  # draws the objects
        b.draw()
        
def predraw_update():    
    space.step(0.01)   # advance simulation

class DrawableBody(pm.Body):
    def draw(self):
        with py5.push():
            py5.no_stroke()
            py5.translate(self.position.x, self.position.y)
            py5.rotate(self.angle)
            py5.fill(0) #self.color)
            draw_shapely(self.poly)

def add_triangulated_body(poly: shapely.Polygon, friction=0.1, mass_factor=0.1):
    """
    Maybe make this a DrawableBody class thing?
    How about the graphic attributes?
    """
    cx, cy = poly.centroid.x, poly.centroid.y        
    mass = poly.area * mass_factor
    moi = pm.moment_for_poly(mass, poly.exterior.coords)
    body = DrawableBody(mass, moi)
    body.poly = shapely_translate(poly, -cx, -cy)
    body.position = (cx, cy)
    body.color = py5.random_choice(colors)
    shapes = []
    vs, faces = triangulate_polygon(poly)
    triangles = [(vs[a], vs[b], vs[c]) for a, b, c in faces]
    for tri in triangles:
        translated_tri = [(x - cx, y - cy) for x, y in tri]
        shp = pm.Poly(body, translated_tri)
        shp.friction = friction
        shapes.append(shp)
    space.add(body, *shapes)  # Note critical * operator expands .add(b, s0, s1, s2...)

def is_poly(obj): return isinstance(obj, pm.Poly) 
def is_segment(obj): return isinstance(obj, pm.Segment) 

def key_typed():
    global text_x
    if py5.key == py5.DELETE:
        # clear everything but the "box" walls
        for obj in reversed(space.shapes):
            if not is_segment(obj):
                space.remove(obj)
    elif py5.key == py5.ENTER:
        text_x = margin * 2
    else:
        font = py5.random_choice(fonts)
        for p in polys_from_text(str(py5.key), font):
            add_triangulated_body(shapely_translate(p, text_x, 0))
        #add_triangulated_body_frompolys(polys_from_text(str(py5.key), font))
        text_x += py5.text_width(str(py5.key))
        if text_x > py5.width - py5.text_width('W'):
            text_x = margin * 2

py5.run_sketch(block=False)