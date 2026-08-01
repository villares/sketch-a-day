import py5
from py5_tools import animated_gif
from shapely import Point, Polygon
from trimesh.creation import extrude_polygon

step_thickness = 20
star_points = 10

def setup():
    global p, shapes
    py5.size(600, 600, py5.P3D)
    py5.no_smooth()
    #p = Point(256 + 25, 256 + 25).buffer(128) | Point(384 + 50, 384 + 50).buffer(128)
    p =  Point(320, 320).buffer(256)
    py5.color_mode(py5.CMAP, 'plasma')
    animated_gif('out.gif', frame_numbers=range(1, 181, 4), duration=0.15)
    py5.background(float('nan'))
    #group = py5.create_shape(py5.GROUP)
    shapes = []
    for t in (i / 60 for i in range(60)):
        v = p.exterior.interpolate(t, normalized=True)
        buffer = 10 * py5.cos((t + 0.5) * py5.TWO_PI)
        r1 = 250
        r2 = 150 + buffer
        rot = t * py5.TWO_PI  
        py5.fill(t)
        shp = star(v.x, v.y, star_points, r1, r2, buffer, rot)
        shp = shp - shp.buffer(-20)
        mesh = extrude_polygon(shp, step_thickness)
        shapes.append(py5.convert_shape(mesh, min_edge_angle=0.15))
        #group.add_child(py5.convert_shape(mesh))
    
def draw():
    py5.background('black')
    py5.stroke_weight(2)
    py5.translate(py5.width / 2, py5.height / 2, -900)
    py5.rotate_y(py5.radians(py5.frame_count * 2))
    py5.translate(-py5.width / 2, -py5.height / 2, -900)    
    for shp in shapes:
        py5.shape(shp)
        py5.translate(0, 0, step_thickness)

def star(x, y, n, ra, rb, buffer=0, rot=0):    
    passo = py5.TWO_PI / n
    vs = [] 
    for i in range(n): 
        angulo = i * passo + rot
        vx = x + ra * py5.sin(angulo)
        vy = y + ra * py5.cos(angulo)
        vs.append((vx, vy))
        vx = x + rb * py5.sin(angulo + passo / 2)
        vy = y + rb * py5.cos(angulo + passo / 2)
        vs.append((vx, vy)) 
    return Polygon(vs).buffer(buffer)

def key_pressed():
    if py5.key == 's':
        py5.save_frame('#####.png')


def lerp_along_points(amt, pts):
    # Based on LerpVectorsExample by Jeremy Douglass
    amt = constrain(amt, 0, 1)  # let's play safe
    if len(pts) == 1:
        return pts[0]
    cunit = 1.0 / (len(pts) - 1)
    return lerp(pts[floor(amt / cunit)],
                pts[ceil(amt / cunit)],
                amt % cunit / cunit)

py5.run_sketch(block=False)
