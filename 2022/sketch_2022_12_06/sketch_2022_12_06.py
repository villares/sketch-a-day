# Update using hx2A's tip from:
# https://github.com/py5coding/py5generator/discussions/206#discussioncomment-4329841

import cv2
import numpy as np
from py5 import create_image_from_numpy

cap = cv2.VideoCapture(0)
py5_img = None

def setup():
    size(640, 480)

def draw():
    global py5_img
    if frame_count % 30 == 0:
        window_title(f'FR: {get_frame_rate()}')
    ret, frame = cap.read()  # frame is a numpy array
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 80)
    #blended_gray = cv2.addWeighted(gray, 0.6, edges, 0.4, 0)
    edges_rgb_npa = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    blended_rgb_npa = cv2.addWeighted(frame, 0.6,
                                      edges_rgb_npa, 0.4, 0)
    #py5_img = create_image_from_numpy(blended_gray, 'L', dst=py5_img)    
    py5_img = create_image_from_numpy(blended_rgb_npa, 'RGB', dst=py5_img)
    # display image
    image(py5_img, 0, 0)
     
def exiting():
    print('over and out')
    cap.release()