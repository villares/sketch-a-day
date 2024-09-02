#! /home/villares/thonny-env/bin/python3
# You'll need py5. Learn more at py5coding.org
from functools import cached_property

import py5

palete = []


from shapely import Polygon

def draw_shapely(self):
    shp = py5.convert_cached_shape(self)
    shp.disable_style()
    py5.shape(shp)

Polygon.draw = draw_shapely

# class Polygon(shapely.Polygon):
#     def draw(self):
#         shp = py5.convert_shape(self)
#         shp.disable_style()
#         py5.shape(shp)



def setup():
    py5.size(600, 600)
    py5.no_loop()
    
def draw():
    py5.background(100)
    py5.no_stroke()
    r = 100
    w = r * py5.sqrt(3)
    palete[:] = [
        py5.color(py5.random_int(255),
                  py5.random_int(255),
                  py5.random_int(255))
             for _ in range(4)]
    for j in range(-2, 3):
        y = 300 + j * r * 3 / 2
        for i in range(-2, 3):
            x = 300 + i * w + (w / 2) * (j % 2)
            unit(x, y, r)
#    tri(300, 300, 100)


def unit(xu, yu, ru, ang=0): 
    vs = regular_poly_points(xu, yu, ru / py5.sqrt(3), 6, ang)
    for i, (x, y) in enumerate(vs):
        tri(x, y, ru /  py5.sqrt(3), ang + py5.radians(60) * (i + 1), i)


def tri(x, y, r, angle=0, n=0):
    evs = regular_poly_points(x, y, r, 3, angle)
    ivs = regular_poly_points(x, y, r / 4, 3, angle)
    py5.fill(palete[3])
    central_triangle = Polygon(ivs).buffer(-3)
    central_triangle.draw()
    trapezoids = []
    for i in range(3):
        sax, say = evs[i]
        sbx, sby = evs[i - 1]
        a = py5.lerp(sax, sbx, 1/4), py5.lerp(say, sby, 1/4)
        b = py5.lerp(sax, sbx, 3/4), py5.lerp(say, sby, 3/4)
        c = ivs[i - 1]
        d = ivs[i]
        py5.fill(palete[(i + n) % 3])
        Polygon((a, b, c, d)).buffer(-3).draw()
        trapezoids.append((a, b, c, d))
    for i in range(3):
        a = evs[i-1]
        b = trapezoids[i-1][0]
        c = ivs[i-1]
        d = trapezoids[i][1]
        Polygon((a, b, c, d)).buffer(-3).draw()
#         Polygon(d).buffer(-3).draw()
#         py5.fill(255)
#         py5.circle(*b, 5)
#         py5.circle(*d, 5)
#         py5.circle(*a, 5)

#     py5.fill(palete[-1])
#     #ivs = regular_poly_points(x, y, r / 4, 3, angle)
#     for j, major in enumerate(triangulate(evs)):
#         tris = triangulate(major)
#         for i, tri in enumerate(tris):
#             py5.fill(palete[int((j + i // 2) % 3)])
#             with py5.begin_closed_shape():
#                 py5.vertices(tri)
#     
def regular_poly_points(x, y, cr, N, rot=0):
    # cr is the circumradius
    ang = py5.TAU / N
    return [(x + py5.cos(i * ang + rot) * cr,
             y + py5.sin(i * ang + rot) * cr)
           for i in range(N)]

def triangulate(pts):
    xs, ys = tuple(zip(*pts))
    xc, yc = sum(xs) / len(xs), sum(ys) / len(ys)
    triangles = []
    for i, (x, y) in enumerate(pts):
        x0, y0 = pts[i-1]
        triangles.append(((x, y), (x0, y0), (xc, yc)))
    return triangles

def key_pressed():
    if py5.key == ' ':
        py5.redraw()
    elif py5.key == 'S':
        save_snapshot_and_code()
    elif py5.key == 's':
        py5.save(__file__[:-3]+'.png')
    
def save_snapshot_and_code():
    from py5 import sketch_path, save
    import shutil
    p = sketch_path()
    N = f'{len(list(p.iterdir())):03d}'
    save(p / N / (N + '.png')) 
    shutil.copyfile(__file__, p / N / (N + '.py'))

py5.run_sketch(block=False)