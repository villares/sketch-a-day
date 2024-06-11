import py5
import pymunk as pm   # the 2D physics engine
from trimesh.creation import triangulate_polygon
from shapely.affinity import translate as shapely_translate
import shapely

from villares.shapely_helpers import polys_from_text

space = pm.Space()    # the pymunk simulation space
space.gravity = (0, 600)

shapes = []
colors = []

def setup():
    global letter_shapes, results
    py5.size(600, 400)
    py5.color_mode(py5.HSB)
    for i in range(5):
          colors.append(py5.color(i * 255/6, 255, 255))  
    global font, text_x, margin
    font = py5.create_font('D050000L', 90)
#     letter_shapes = polys_from_text(
#         'viva o LHC\n12 anos!',
#         font, leading=90, alternate_spacing=True
#         )
#     for shp in letter_shapes:
#         add_trianglulated_body(shapely_translate(shp, 50, 100))

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
        
def predraw_update():    
    space.step(0.01)   # advance simulation

class DrawableBody(pm.Body):
    def draw(self):
        with py5.push():
            py5.translate(self.position.x, self.position.y)
            py5.rotate(self.angle)
            py5.shape(self.py5_shape, 0, 0)

def add_trianglulated_body(
    poly: shapely.Polygon,
    friction=0.1,
    mass_factor=0.1
    ):
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
    shp = py5.convert_shape(body.poly)
    shp.set_fill(py5.random_choice(colors))
    body.py5_shape = shp
    shapes = []
    vs, faces = triangulate_polygon(poly)
    triangles = [(vs[a], vs[b], vs[c]) for a, b, c in faces]
    for tri in triangles:
        translated_tri = [(x - cx, y - cy) for x, y in tri]
        shp = pm.Poly(body, translated_tri)
        shp.friction = friction
        shapes.append(shp)
    space.add(body, *shapes)  # Note critical * operator expands .add(b, s0, s1, s2...)
   
# WIP   
def add_trianglulated_body_frompolys(
    mpoly: shapely.MultiPolygon,
    friction=0.1,
    mass_factor=0.5):
    """
    Check multi-color solution...
    """
    try:    
        cx, cy = mpoly.centroid.x, mpoly.centroid.y        
        mass = moi = 0
        for poly in mpoly.geoms:    
            p_mass = poly.area * mass_factor
            moi += pm.moment_for_poly(p_mass, poly.exterior.coords)
            mass += p_mass
    except shapely.GEOSException:
        print(mpoly)
        return
    body = DrawableBody(mass, moi)
    body.polys = shapely_translate(mpoly, -cx, -cy)
    body.position = (cx, cy)
    shp = py5.convert_shape(body.polys)
    for child in shp.get_children():
        child.set_fill(py5.random_choice(colors))
    body.py5_shape = shp
    shapes = []    
    for poly in mpoly.geoms:    
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
        for p in polys_from_text(str(py5.key), font):
            pass 
            #add_trianglulated_body(shapely_translate(p, text_x, 0))
        mp = shapely.MultiPolygon(polys_from_text(str(py5.key), font))
        tmp = shapely_translate(mp, text_x, 0)                                  
        add_trianglulated_body_frompolys(tmp)
        text_x += py5.text_width(str(py5.key))
        if text_x > py5.width - py5.text_width('W'):
            text_x = margin * 2


py5.run_sketch(block=False)