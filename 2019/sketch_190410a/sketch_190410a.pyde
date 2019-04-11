# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME, OUTPUT = "sketch_190410a", ".gif"
"""
"""
add_library('GifAnimation')
from gif_exporter import gif_export
add_library('peasycam')
from unfolded_2D import *
from draw_3D import *

CUT_COLOR = color(200, 0, 0)  # Color to mark outline cut
ENG_COLOR = color(0, 0, 200)  # Color to mark folding/engraving
TAB_W = 10  # tab width
TAB_A = radians(30)  # tab angle

box_d, box_w, box_h = 100, 100, 100  # initial box dimensions
ah = bh = ch = dh = box_h  # initial height of points a, b, c and d
# height of points between d and c
cd_i = [box_h, box_h, box_h]* 2 #[box_h, box_h + 15, box_h + 10, box_h]
# height of points between a and b
ab_i = [box_h, box_h, box_h]*2 #[box_h, box_h - 15, box_h - 10, box_h]

assert len(cd_i) == len(ab_i)  # has to mantain equal number of pts

def setup():
    size(850, 500, P3D)
    # global cam
    # cam = PeasyCam(this, 300)
    hint(ENABLE_DEPTH_SORT)
    smooth(16)
    strokeWeight(2)

def draw():
    background(200)    
    # Draw 3D
    with pushMatrix():
        translate(width / 2, height / 2)  # Comment out if using with PeasyCam
        rotateX(QUARTER_PI)
        rotateZ(0)
        translate(200, -50, -100)
        face_data = draw_3d(box_w, box_d, ab_i, cd_i)
        
    # Draw 2D unfolded
    # cam.beginHUD() # for use with PeasyCam
    with pushMatrix():
        translate(100, 350)
        draw_unfolded(box_w, box_d, ab_i, cd_i, face_data)
    # cam.endHUD()






def keyPressed():
    global ah, bh, ch, dh, box_w, box_d, box_h
    # save frame on GIF
    # gif_export(GifMaker, filename=SKETCH_NAME)

    if key == "q":
        ah += 5
    if key == "a" and ah > 5:
        ah -= 5
    if key == "w":
        bh += 5
    if key == "s" and bh > 5:
        bh -= 5
    if key == "e":
        ch += 5
    if key == "d" and ch > 5:
        ch -= 5
    if key == "r":
        dh += 5
    if key == "f" and dh > 5:
        dh -= 5
    if key in ("+", "="):
        box_h += 5
        ah += 5
        bh += 5
        ch += 5
        dh += 5
    if (key == "-" and box_h > 5 and ah > 5 and bh > 5 and ch > 5 and dh > 5):
        box_h -= 5
        ah -= 5
        bh -= 5
        ch -= 5
        dh -= 5
    if keyCode == UP and box_d + box_w < 220:
        box_d += 5
    if keyCode == DOWN and box_d > 5:
        box_d -= 5
    if keyCode == RIGHT and box_w + box_d < 220:
        box_w += 5
    if keyCode == LEFT and box_w > 5:
        box_w -= 5
    if key == " ":
        slowly_reset_values()
    if key == "p":
        saveFrame("####.png")
        
    # update top face point lists
    cd_i[0] = ch
    cd_i[-1] = dh
    ab_i[0] = ah
    ab_i[-1] = bh

def slowly_reset_values():
    global box_w, box_d, box_h, ah, bh, ch, dh
    box_w += (100 - box_w) / 2
    box_d += (100 - box_d) / 2
    box_h += (100 - box_h) / 2
    ah += (box_h - ah) / 2
    bh += (box_h - bh) / 2
    ch += (box_h - ch) / 2
    dh += (box_h - dh) / 2
    
    
    
