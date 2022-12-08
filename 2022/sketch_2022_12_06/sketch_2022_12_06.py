import cv2
import numpy as np
#from PIL import Image
from py5 import create_image_from_numpy

cap = cv2.VideoCapture(0)

def setup():
    size(640, 480)

def draw():
    ret, frame = cap.read()
    #pil_img = Image.fromarray(frame)     # from npa to PIL.Image
    ## if you want to use PIL manipulation here
    #img_as_np_array = np.array(pil_img)  # back to npa
    img_as_np_array = frame
    gray = cv2.cvtColor(img_as_np_array, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 80)
    # blended_gray = cv2.addWeighted(gray, 0.6, edges, 0.4, 0)
    edges_rgb_npa = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    blended_rgb_npa = cv2.addWeighted(img_as_np_array, 0.6,
                                      edges_rgb_npa, 0.4, 0)
    py5_img = create_image_from_numpy(blended_rgb_npa, 'RGB')
    image(py5_img, 0, 0)
     
def exiting():
    print('over and out')
    cap.release()