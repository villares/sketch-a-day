import py5
import numpy as np
import cv2
from shapely.geometry import Polygon, MultiPolygon
from shapely.ops import unary_union

py5_img = m = None

def setup():
    global img, img_rgb_pixels
    py5.size(800, 800)
    img_path = 'sample.png' # Sample from sketh 2023_07_22
    img = py5.load_image(img_path)
    img.load_np_pixels()
    img_rgb_pixels = img.np_pixels

def draw():
    py5.background(100, 100, 200)
    global py5_img, m
    rgb_np = cv2.cvtColor(img_rgb_pixels[:, :, 1:], cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(img_rgb_pixels, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 1)
    tresholds = [
        cv2.threshold(blurred, 25 + i * 25, 255, cv2.THRESH_BINARY)[1]  # ret, img
        for i in range(8)]
    #py5_img = py5.create_image_from_numpy(rgb_np, bands='BGR', dst=py5_img)
    py5_img = py5.create_image_from_numpy(tresholds[6], bands='L', dst=py5_img)
    m = py5.create_image_from_numpy(255 - tresholds[7],  bands='L', dst=m)
    py5_img.mask(m)
    py5.image(py5_img, 0, 0)
    
#     contours = [
#         cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0]
#         for threshold in tresholds]
#     for i, contour in enumerate(contours):
#         py5.fill(i * 50, 100)
#         mp = merge_polygons(contour)
#         draw_shapely_objs(mp)

def key_pressed():
    py5.save('out.png')

# def merge_polygons(contours):
#     polys = []
#     for contour in contours:
#         if len(contour) > 4:
#             new_poly = Polygon(v[0] for v in contour)
#             # Not all polygons are shapely-valid (self intersection, etc.)
#             if not new_poly.is_valid:
#                 # Convert invalid polygon to valid
#                 new_poly = new_poly.buffer(1)
#             if isinstance(new_poly, MultiPolygon):
#                 polys.extend(new_poly.geoms)
#             else:
#                 polys.append(new_poly)    
#     if polys:
#         results = [polys[0]]
#         for p in polys[1:]:
#             for i, earlier in enumerate(results):
#                 if earlier.contains(p):
#                     results[i] = results[i].difference(p)
#                     break
#             else:   # the for-loop's else only executes after unbroken loops
#                 results.append(p)
#         return results
#     else:
#         return []
# 
# def draw_shapely_objs(element):
#     """
#     With py5, draw some shapely object (or a list of objects).
#     """
#     from shapely.geometry import (
#         Polygon, MultiPolygon, GeometryCollection, LineString, Point
#     )
#     if isinstance(element, (MultiPolygon, GeometryCollection)):
#         for p in element.geoms:
#             draw_shapely_objs(p)
#     elif isinstance(element, Polygon):
#         with py5.begin_closed_shape():
#             if element.exterior.coords:
#                 py5.vertices(element.exterior.coords)
#             for hole in element.interiors:
#                 with py5.begin_contour():
#                     py5.vertices(hole.coords)
#     elif isinstance(element, list):
#         for i, p in enumerate(element):
#             draw_shapely_objs(p)
#     elif isinstance(element, LineString):
#         (xa, ya), (xb, yb) = element.coords
#         py5.line(xa, ya, xb, yb)
#     elif isinstance(element, Point):
#         with py5.push_style():
#             x, y = element.coords[0]
#             py5.point(x, y)
#     else:
#         print(f"I can't draw {element}.")

py5.run_sketch(block=False)