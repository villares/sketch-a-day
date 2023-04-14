import py5
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
py5_img = None

def setup():
    py5.size(640, 480)


def draw():
    global py5_img
    py5.background(200, 0, 0)
    if py5.frame_count % 30 == 0:
        py5.window_title(f'FR: {py5.get_frame_rate()}')
    ret, frame = cap.read()  # frame is a numpy array
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 80)
    # create a binary mask for pixels with brightness > 250
    mask = np.zeros_like(gray)
    mask[gray < 128] = 255
    # add transparency to the blended image based on the mask
    blended_rgb_npa = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    blended_rgb_npa[:, :, 3] = mask
    # display image
    py5_img = py5.create_image_from_numpy(blended_rgb_npa, 'BGRA', dst=py5_img)
    py5.image(py5_img, 0, 0)


def exiting():
    print('over and out')
    cap.release()


py5.run_sketch()
