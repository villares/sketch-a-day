import py5
import numpy as np
import cv2

cap = None
py5_img = None

def setup():
    py5.size(800, 600)
    py5.launch_thread(open_capture)
    
def draw():
    py5.background(255)
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
        resized_frame = cv2.resize(frame, (py5.width, py5.height))
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

        py5_img = py5.create_image_from_numpy(edges, 'L', dst=py5_img)
        py5.image(py5_img, 0, 0)
        py5.fill(0, 100, 0, 150)
        draw_contours(contours)
        py5.fill(0, 0, 100, 150)
        draw_contours(contours2)
        
def draw_contours(contours):
        for c in contours:
            with py5.begin_closed_shape():
                for p in c:
                    py5.vertex(*p[0])

py5.run_sketch()
