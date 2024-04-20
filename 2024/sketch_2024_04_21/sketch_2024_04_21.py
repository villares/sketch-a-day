# Alexandre B A Villares - https://abav.lugaralgum.com/
# To run this you will need py5 https://abav.lugaralgum.com/como-instalar-py5/index-EN.html
from itertools import product

import py5

from shape import all_from_points

grid = product((-1, 0, 1), (-1, 0, 1))  # 3X3
pts = list(grid)
space, border = 100, 50

def setup():
    global shapes
    py5.size(850, 550)
    py5.background(200)
    py5.text_font(py5.create_font('Inconsolata Bold', 18))
    W = int(py5.width - border * 2) // space
    H = int(py5.height - border * 2) // space
    shapes = []
    tm = 0
    for i in [4]: # 3 to 7, as no non-intersecting shapes exist with 8 or 9 pts.
        m = py5.millis()
        shapes.extend(all_from_points(pts, i)) #, remove_flipped=True))
        dt = py5.millis() - m
        print(i, dt)
        tm += dt
    print(f'total: {tm} millisegundos')
    
    def min_angles(s):
        a = []
        for i, v2 in enumerate(s.points):
            v1 = s.points[i - 1]
            v0 = s.points[i - 2]
            ang = py5.degrees(corner_angle(v1, v0, v2))
            a.append(ang)
        print(a, s.area)
        return int(min(a)) + s.area
        
    shapes.sort(key=min_angles)
    
    print(f'shapes: {len(shapes)} Cols: {W} Rows: {H} Visible grid: {W*H}')

    py5.stroke_join(py5.ROUND)
    py5.no_stroke()
    i = 0
    scale_factor = space * 0.4
    for y, x in product(range(H), range(W)):
        if i < len(shapes):
            shp = shapes[i]
            a = poly_area(shp.points)
            shp_pts = shp.points 
            with py5.push_matrix():
                py5.translate(border + space * x + space / 2,
                              border + space * y + space / 2)
                py5.fill(0)
                shp.draw(scale_factor)
                py5.text_size(12)
                for vi, v2 in enumerate(shp_pts):
                    v1 = shp_pts[vi - 1]
                    v0 = shp_pts[vi - 2]
                    ang = int((180 - py5.degrees(corner_angle(v1, v0, v2))) * 10) / 10
                    py5.fill(255)
                    py5.text(f'{ang}', v1[0] * scale_factor, v1[1] * scale_factor)

                if a < 0:
                    py5.fill(255, 0, 0)
                else:
                    py5.fill(0, 0, 255)
                cx, cy = shp.poly.centroid.coords[0]
                py5.text(f'{min_angles(shp)}', cx * scale_factor, cy * scale_factor)
        i += 1


def corner_angle(c, a, b):
    import numpy as np
    c = np.array(c)
    a = np.array(a) - c
    b = np.array(b) - c
    ang = np.arctan2(np.cross(a, b), np.dot(a, b))
    if ang < 0: ang += np.pi
    return ang

def cross_sign(x1, y1, x2, y2):
    return x1 * y2 > x2 * y1

# for i in range(len(points)):
#     p1 = points[i]
#     ref = points[i - 1]
#     p2 = points[i - 2]
#     x1, y1 = p1[0] - ref[0], p1[1] - ref[1]
#     x2, y2 = p2[0] - ref[0], p2[1] - ref[1]
# 
#     print('Points', p1, ref, p2)
#     print('Angle', angle(x1, y1, x2, y2))
#     if cross_sign(x1, y1, x2, y2):
#         print('Inner Angle')
#     else:
#         print('Outer Angle')
#     print('')


def poly_area(points):
    points = list(points)
    area = 0.0
    for (ax, ay), (bx, by) in zip(points, points[1:] + [points[0]]):
        area += ax * by
        area -= bx * ay
    return area / 2.0

def key_pressed():
    py5.save_frame('###.png')



py5.run_sketch(block=False)
