import py5


import numpy as np
import cv2
from shapely.geometry import Polygon, MultiPolygon
from shapely.ops import unary_union

cap = None
py5_imgs = [None] * 3

reduced_size = 600, 600


def setup():
    py5.size(800, 600)
    py5.launch_thread(open_capture)

def open_capture():
    global cap
    cap = cv2.VideoCapture(0)
    print('Capture started')

def draw():
    py5.background(255, 255, 0)
    global py5_img1, py5_img2, py5_img3
    ret = False
    if cap:
        ret, frame = cap.read()  # frame is a numpy array
    if ret:
        resized_frame = cv2.resize(frame, reduced_size)
        rgb_np = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)

        tresholds = (
            cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)[1],  # ret, img
            cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)[1],
            cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1],
            # cv2.threshold(255 - gray, 100, 255, cv2.THRESH_BINARY)[1],
        )
        contours = [
            cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0]
            for threshold in tresholds
        ]
#         x = 0
#         for i, img in enumerate(py5_imgs):
#             py5_imgs[i] = py5.create_image_from_numpy(tresholds[i], 'L', dst=img)
#             py5.image(py5_imgs[i], x + 400, 0)
#             x += 400
        py5.fill(255, 0, 0)
        py5.rect(0, 0, 400, 400)
        colors = ('gray', 'blue', 'black')
        for i, contour in enumerate(contours):
            py5.fill(colors[i])
            mp = merge_polygons(contour)
            py5.translate(20, 0)
            draw_shapely_objs(mp)


def merge_polygons(contours):
    polys = []
    for contour in contours:
        if len(contour) > 4:
            new_poly = Polygon(v[0] for v in contour)
            # Not all polygons are shapely-valid (self intersection, etc.)
            if not new_poly.is_valid:
                # Convert invalid polygon to valid
                new_poly = new_poly.buffer(0)
            polys.append(new_poly)
    #polys = sorted(polys, key=lambda p: p.area, reverse=True)
    results = [polys[0]]
    for p in polys[1:]:
        # works on edge cases like â and ®
        for i, earlier in enumerate(results):
            if earlier.contains(p):
                results[i] = results[i].difference(p)
                break
        else:   # the for-loop's else only executes after unbroken loops
            results.append(p)
    return results


def draw_shapely_objs(element):
    """
    With py5, draw some shapely object (or a list of objects).
    """
    from shapely.geometry import (
        Polygon, MultiPolygon, GeometryCollection, LineString, Point
    )
    if isinstance(element, (MultiPolygon, GeometryCollection)):
        for p in element.geoms:
            draw_shapely_objs(p)
    elif isinstance(element, Polygon):
        with py5.begin_closed_shape():
            if element.exterior.coords:
                py5.vertices(element.exterior.coords)
            for hole in element.interiors:
                with py5.begin_contour():
                    py5.vertices(hole.coords)
    elif isinstance(element, list):
        for i, p in enumerate(element):
            draw_shapely_objs(p)
    elif isinstance(element, LineString):
        (xa, ya), (xb, yb) = element.coords
        py5.line(xa, ya, xb, yb)
    elif isinstance(element, Point):
        with py5.push_style():
            x, y = element.coords[0]
            py5.point(x, y)
    else:
        print(f"I can't draw {element}.")


py5.run_sketch()
