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
flag_delete = False
margin = 5

def setup():
    py5.size(300, 300, py5.P2D)
    walls = (
        ((margin, py5.height - margin), (py5.width - margin, py5.height - margin)),
        ((margin, py5.height - margin), (margin, margin)),
        ((py5.width - margin, py5.height - margin), (py5.width - margin, margin)),
    )
    for pa, pb in walls:
        wall = pm.Segment(space.static_body, pa, pb, 2)
        wall.friction = 0.4
        space.add(wall)
  
    global shp, path, poly
    shp = py5.load_shape('a.svg')
    path = shp.get_children()[1].get_children()[0]
    poly = shapely.Polygon((v.x * 3.5, v.y * 3.5) for i in range(path.get_vertex_count())
                           if bool(v:=path.get_vertex(i)))
        
def predraw_update():
    check_delete()
    space.step(0.01)   # advance simulation

def draw():
    global current_union, previous_union, meshes
    py5.background(0)
    for b in space.bodies:  # draws the objects
        b.draw()

class DrawableBody(pm.Body):
    def draw(self):
        with py5.push():
            py5.translate(self.position.x, self.position.y)
            py5.rotate(self.angle)
            py5.shape(self.py5_shape, 0, 0)
            py5.shape_mode(py5.CENTER)
            py5.shape(shp, 0, 0)

def add_triangulated_body(
    poly: shapely.Polygon,
    friction=0.1,
    mass_factor=0.1,
    py5_shape=None,
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
    if py5_shape is None:
        py5_shape = py5.convert_shape(body.poly)
    body.py5_shape = py5_shape
    shapes = []
    vs, faces = triangulate_polygon(poly)
    triangles = [(vs[a], vs[b], vs[c]) for a, b, c in faces]
    for tri in triangles:
        translated_tri = [(x - cx, y - cy) for x, y in tri]
        shp = pm.Poly(body, translated_tri)
        shp.friction = friction
        shapes.append(shp)
    space.add(body, *shapes)  # Note critical * operator expands .add(b, s0, s1, s2...)
   
def add_triangulated_body_frompolys(
    mpoly: shapely.MultiPolygon | list[shapely.Polygon],
    friction=0.1,
    mass_factor=0.5):
    """
    Try to think another multi-color solution...
    ... maybe passing them a keyword argument.
    """
    mpoly = shapely.MultiPolygon(mpoly)
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

def check_delete():
    global flag_delete
    if flag_delete:
        flag_delete = False
        for shp in reversed(space.shapes):
            if not is_segment(shp):
                space.remove(shp)
        for body in reversed(space.bodies):
            space.remove(body)

def key_typed():
    global text_x, flag_delete
    if py5.key == 'd':
        flag_delete = True
    elif py5.key == py5.ENTER:
        text_x = margin * 2
    else:
        add_triangulated_body(poly)


py5.run_sketch(block=False)

