"""
 ASCII video
 a, d, w, s to change sizes
"""
import py5
import cv2  # opencv-python
import numpy as np

cap = None
img = None
color_on = False
grid_size = 8  # tamanho da grade
font_size = 12  # tamanho dsa letras
gliphs = (
    " .`-_':,;^=+/\"|)\\<>)iv%xclrs{*}I?!][1taeo7zjLu" +
    "nT#JCwfy325Fp6mqSghVd4EgXPGZbYkOA&8U$@KHDBWNMR0Q"
    )#[::-1]   
# esse [::-1]  é um "reverse" do string em Python, para o primiro glifo ser o mais escuro e o último o mais claro
print(gliphs)    

def setup():
    py5.size(640, 480)
    py5.no_smooth()
    f = py5.create_font("Source Code Pro Bold",60)
    py5.text_font(f)
    py5.text_align(py5.CENTER, py5.CENTER)
    py5.launch_thread(open_capture)
    set_grid()

def set_grid():
    global sample_pos, n_rows, n_cols
    n_cols = int(py5.width / grid_size)
    n_rows = int(py5.height / grid_size)
    sample_pos = np.array([
        (r * grid_size, c * grid_size)
        for c in range (n_cols)
        for r in range(n_rows)
    ])
 
def draw():
    global img

    if cap:
        py5.background(0) 
        ret, frame = cap.read()
        img = py5.create_image_from_numpy(frame, 'RGB', dst=img)
#         for c in range(n_cols):
#             x = c * grid_size
#             for r in range(n_rows):
#                 y = r * grid_size
#                 px = img.get_pixels(x, y)
        sample = img.np_pixels[sample_pos[:, 0], sample_pos[:, 1]]
        for argb, (y, x) in zip(sample, sample_pos):
            px = py5.color(*argb[1:])
            bri = py5.brightness(px)
            g = int(py5.remap(bri, 0, 255, 0, len(gliphs)-1))
            if color_on:
                py5.fill(px)
            else:
                py5.fill(255)
            py5.text_size(font_size)
            py5.text(gliphs[g], x + grid_size / 2, y + grid_size / 2)

def open_capture():
    global cap
    cap = cv2.VideoCapture(0)
    #brightness = cap.get(cv2.cv.CV_CAP_PROP_BRIGHTNESS)
    #cap.set(cv2.CAP_PROP_BRIGHTNESS, 0.5)
    print('Capture started')
    

def key_pressed():
    global font_size, grid_size, color_on
    if py5.key == 'g':
        py5.save_frame("f####.png")
    if py5.key == 'w':
        font_size += 1
    if py5.key == 's' and font_size > 1:
        font_size -= 1
    if py5.key == 'a':
        grid_size += 1
    if py5.key == 'd' and grid_size > 1:
        grid_size -= 1
    if py5.key == 'c':
        color_on = not color_on
    set_grid()

def exiting():   # py5 will call this for clean up on exit
    cap.release()
    print('Capture released')
     
py5.run_sketch()