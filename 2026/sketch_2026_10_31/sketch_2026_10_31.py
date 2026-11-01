from itertools import product
import numpy as np
import py5
import shapely


def setup():
    py5.size(500, 500)
    
def draw():
    py5.background(0)
    py5.no_fill()
    py5.stroke(255)
    a = estrela(150, 250, 6, 125, 50, hole=10)
    #py5.shape(a)
    b = estrela(350, 250, 6, 100, 175, hole=10)
    #py5.shape(b)
    for n in range(10):
        t = n / 10
        c = lerp_poly(a, b, t)
        py5.shape(c)
    
def estrela(x, y, n, ra, rb, buffer=0, hole=1, rot=0):    
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
    e  = shapely.Polygon(vs).buffer(buffer)
    if hole:
        return e - e.buffer(-hole) #.buffer(-1)
    else:
        return e
    
def lerp_poly(poly_a, poly_b, t):
    ext_a = np.array(poly_a.exterior.coords[:-1])
    ext_b = np.array(poly_b.exterior.coords[:-1])
    
    if len(ext_a) != len(ext_b):
        target_count = max(len(ext_a), len(ext_b))
        ext_a = resample_points(ext_a, target_count * 10)
        ext_b = resample_points(ext_b, target_count * 10)
    
    inter_ext = ext_a + t * (ext_b - ext_a)
    holes_a = list(poly_a.interiors)
    holes_b = list(poly_b.interiors)
    inter_holes = []
    num_holes = max(len(holes_a), len(holes_b))
    for i in range(num_holes):
        if i < len(holes_a) and i < len(holes_b):
            exterior_centroid = ext_a.mean(axis=0)
            hole_a = np.array(holes_a[i].coords[:-1])
            hole_b = np.array(holes_b[i].coords[:-1])
            if len(hole_a) != len(hole_b):
                target_count = max(len(hole_a), len(hole_b))
                hole_a = resample_points(hole_a, target_count)
                hole_b = resample_points(hole_b, target_count)
            interpolated_interior = hole_a + t * (hole_b - hole_a)
            inter_holes.append(interpolated_interior)
        elif i < len(holes_a):
            exterior_centroid = ext_b.mean(axis=0)
            hole_a = np.array(holes_a[i].coords[:-1])
            interpolated_interior = hole_a + t * (exterior_centroid - hole_a)
            inter_holes.append(interpolated_interior)        
        else:
            exterior_centroid = inter_ext.mean(axis=0)
            hole_b = np.array(holes_b[i].coords[:-1])
            interpolated_interior = exterior_centroid + t * (hole_b - exterior_centroid)
            inter_holes.append(interpolated_interior)

    return shapely.Polygon(inter_ext, holes=inter_holes)


def resample_points(ring_coords, num_points):
    line = shapely.LineString(ring_coords)
    distances = np.linspace(0, line.length, num_points, endpoint=False)
    points = [line.interpolate(distance).coords[0] for distance in distances]
    return np.array(points)

def key_pressed():
    py5.save_frame('out.png')

py5.run_sketch()