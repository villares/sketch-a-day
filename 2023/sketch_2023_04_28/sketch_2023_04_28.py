import numpy as np
import cv2

cap = None
py5_imgs = [None] * 3

reduced_size = 400, 400

def setup():
    size(1600, 400)
    launch_thread(open_capture)
    
def draw():
    background(255)
    camera()

def open_capture():
    global cap
    cap = cv2.VideoCapture(0)
    #brightness = cap.get(cv2.cv.CV_CAP_PROP_BRIGHTNESS)
    #cap.set(cv2.CAP_PROP_BRIGHTNESS, 0.5)
    print('Capture started')
    
def camera():
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
#         ret, img_bw_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#         contours, hierarchy = cv2.findContours(img_bw_otsu, 
#             cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#         contours2, hierarchy2 = cv2.findContours(255 - img_bw_otsu, 
#             cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        x = 0
        for i, img in enumerate(py5_imgs):
            py5_imgs[i] = create_image_from_numpy(tresholds[i], 'L', dst=img)
            image(py5_imgs[i], x + 400, 0)
            x += 400
        fill(100, 0, 0)
        rect(0, 0, 400, 400)
        fill(0, 0, 200, 100)
        draw_contours(0, 0, contours[2])
        fill(0, 100, 0, 100)
        draw_contours(0, 0, contours[1])
        fill(255, 100)
        draw_contours(0, 0, contours[0])
        
        
def draw_contours(x, y, contours):
    with push_matrix():
        translate(x, y)
        for c in contours:
            with begin_closed_shape():
                for p in c:
                    vertex(*p[0])

