from itertools import product
import numpy as np
import py5
import shapely


def setup():
    py5.size(500, 500)
    
def draw():
    py5.background(0)
    a = estrela(130, 250, 10, 125, 50, hole=20)
    #py5.shape(a)
    b = estrela(320, 250, 20, 110, 160, hole=15)
    #py5.shape(b)
    m = 4
    for t in np.linspace(0, 1, 10):
        py5.stroke(0)
        py5.fill(255 * t, 128, 255 - 255 * t, 200)
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

def resample_points(pts, num_samples=1000):
    return np.array([
            shapely.LineString(pts).interpolate(t, normalized=True).coords[0] 
            for t in np.linspace(0, 1, num_samples, endpoint=False)
        ])


def lerp_poly(poly_a, poly_b, t):
    c_a = np.array(poly_a.centroid.coords)
    c_b = np.array(poly_b.centroid.coords)
    inter_centroid = (1 - t) * c_a + t * c_b
    # move each poly to its centroid (subtract the coords)
    ext_a_local = resample_points(poly_a.exterior.coords) - c_a
    ext_b_local = resample_points(poly_b.exterior.coords) - c_b    
    inter_ext_local = (1 - t) * ext_a_local + t * ext_b_local
    holes_a = list(poly_a.interiors)
    holes_b = list(poly_b.interiors)
    inter_holes_local = []    
    num_holes = max(len(holes_a), len(holes_b))
    for i in range(num_holes):
        if i < len(holes_a) and i < len(holes_b):
            # hole exists on both states
            h_a_local = resample_points(holes_a[i]) - c_a
            h_b_local = resample_points(holes_b[i]) - c_b
            inter_holes_local.append((1 - t) * h_a_local + t * h_b_local)
        elif i < len(holes_a):
            # hole in A only, should shrink
            h_a_local = resample_points(holes_a[i]) - c_a
            local_h_centroid = np.mean(h_a_local, axis=0)
            inter_holes_local.append((1 - t) * h_a_local + t * local_h_centroid)
        else:
            # hole only in B, should grow
            h_b_local = resample_points(holes_b[i]) - c_b
            local_h_centroid = np.mean(h_b_local, axis=0)
            inter_holes_local.append((1 - t) * local_h_centroid + t * h_b_local)
    # add back centroid coords
    inter_ext = inter_ext_local + inter_centroid
    inter_holes = [h + inter_centroid for h in inter_holes_local]
    result = shapely.Polygon(inter_ext, holes=inter_holes)
    return result.buffer(0)  # zero buffer clean up

def key_pressed():
    py5.save_frame('out.png')

py5.run_sketch()