import numpy as np
import cv2

cap = None
py5_img = None
camera_on = True

def setup():
    size(800, 600)
    launch_thread(open_capture)
    
def draw():
    background(255)
    if camera_on:
        camera()

def open_capture():
    global cap
    cap = cv2.VideoCapture(0)
    #brightness = cap.get(cv2.cv.CV_CAP_PROP_BRIGHTNESS)
    #cap.set(cv2.CAP_PROP_BRIGHTNESS, 0.5)
    print('Capture started')
    
def camera():
    global py5_img
    ret = False
    if cap:
        ret, frame = cap.read()  # frame is a numpy array
    if ret:
        resized_frame = cv2.resize(frame, (width, height))
        rgb_np = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
        edges = 255 - cv2.Canny(gray, 100, 80, 5)
#         edges_rgb_npa = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGRA)
#         mask = np.zeros_like(gray)
#         mask[edges < 150] = 255
#         edges_rgb_npa[:, :, 3] = mask
        ret, img_bw_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        contours, hierarchy = cv2.findContours(img_bw_otsu, 
            cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        
        contours2, hierarchy2 = cv2.findContours(255 - img_bw_otsu, 
            cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        py5_img = create_image_from_numpy(edges, 'L', dst=py5_img)
        image(py5_img, 0, 0)
        fill(0, 100, 0, 150)
        draw_contours(contours)
        fill(0, 0, 100, 150)
        draw_contours(contours2)
        
def draw_contours(contours):
        for c in contours:
            with begin_closed_shape():
                for p in c:
                    vertex(*p[0])
