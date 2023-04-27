import numpy as np
import cv2

a = 100
b = 80

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

def key_pressed():
    global camera_on, a, b
    k = str(key)
    if k == TAB:
        camera_on = not camera_on
    elif key_code == UP:
        a += 5
    elif key_code == DOWN:
        a -= 5
    elif key_code == LEFT:
        b += 5
    elif key_code == RIGHT:
        b -= 5
    print(a, b)
     
     
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
        edges_rgb_npa = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGRA)
        mask = np.zeros_like(gray)
        mask[edges < 150] = 255
        rgba_np = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGBA)
        edges_rgb_npa[:, :, 3] = mask
#         py5_img = create_image_from_numpy(edges_rgb_npa, 'RGBA', dst=py5_img)
#         image(py5_img, 0, 0)
        edged = cv2.Canny(gray, a, b)
        contours, hierarchy = cv2.findContours(edged.copy(), 
            cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        py5_img = create_image_from_numpy(edges, 'L', dst=py5_img)
        image(py5_img, 0, 0)
        fill(255, 0, 0)
        for c in contours:
            with begin_closed_shape():
                for p in c:
                    #print(*p[0], type(p))
                    vertex(*p[0])
#         if is_key_pressed:
#             print(contours, hierarchy)
