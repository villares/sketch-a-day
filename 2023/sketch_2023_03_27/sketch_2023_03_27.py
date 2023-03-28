# More ideas at: https://vuamitom.github.io/2019/12/13/fast-iterate-through-video-frames.html

import py5
import cv2
import numpy as np
from py5 import create_image_from_numpy

movie = cv2.VideoCapture('launch2.mp4')
movie_width = int(movie.get(cv2.CAP_PROP_FRAME_WIDTH))
movie_height = int(movie.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = movie.get(cv2.CAP_PROP_FPS)

py5_img = None

def setup():
    py5.size(movie_width, movie_height)
    py5.frame_rate(fps)

def draw():
    global py5_img
    a = py5.remap(py5.mouse_x, 0, py5.width, 0, 100)
    b = py5.remap(py5.mouse_y, 0, py5.height, 0, 100)
    success, frame = movie.read()  # frame is a numpy array
    if success:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = 255 - cv2.Canny(gray, a, b) 
        edges_rgb_npa = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        blended_rgb_npa = cv2.addWeighted(frame, 0.6, edges_rgb_npa, 0.4, 0)
        py5_img = create_image_from_numpy(blended_rgb_npa, 'RGB', dst=py5_img)
#         py5_img = create_image_from_numpy(frame, 'RGB', dst=py5_img)
        # display image
        py5_img = create_image_from_numpy(edges, 'L', dst=py5_img)
        py5.image(py5_img, 0, 0)
    else:  # If it can't read frame, try starting again
        movie.set(cv2.CAP_PROP_POS_FRAMES, 0)

    if py5.frame_count % 30 == 0:
        py5.window_title(f'FR: {py5.get_frame_rate():.1f}')

def exiting():
    print('over and out')
    movie.release()

py5.run_sketch()
