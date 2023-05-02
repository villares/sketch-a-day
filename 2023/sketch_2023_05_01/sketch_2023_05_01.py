import py5

import numpy as np
import cv2
from shapely.geometry import Polygon, MultiPolygon
from shapely.ops import unary_union

cap = None
reduced_size = 800, 600


def setup():
    py5.size(800, 600)
    py5.launch_thread(open_capture)
    py5.no_stroke()

def open_capture():
    global cap
    cap = cv2.VideoCapture(0)
    print('Capture started')

def draw():
    py5.background(100, 100, 200)
    global py5_img1, py5_img2, py5_img3
    ret = False
    if cap:
        ret, frame = cap.read()  # frame is a numpy array
    if ret:
        resized_frame = cv2.resize(frame, reduced_size)
        rgb_np = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (7, 7), 1)
        tresholds = [
            cv2.threshold(blurred, 25 + i * 25, 255, cv2.THRESH_BINARY)[1]  # ret, img
            for i in range(8)
        ]
        contours = [
            cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0]
            for threshold in tresholds
        ]
        for i, contour in enumerate(contours):
            py5.fill(i * 50)
            mp = merge_polygons(contour)
            draw_shapely_objs(mp)

def merge_polygons(contours):
    polys = []
    for contour in contours:
        if len(contour) > 4:
            new_poly = Polygon(v[0] for v in contour)
            # Not all polygons are shapely-valid (self intersection, etc.)
            if not new_poly.is_valid:
                # Convert invalid polygon to valid
                new_poly = new_poly.buffer(1)
            if isinstance(new_poly, MultiPolygon):
                polys.extend(new_poly.geoms)
            else:
                polys.append(new_poly)    
    if polys:
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
    else:
        return []

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
