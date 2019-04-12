# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME, OUTPUT = "sketch_190411a", ".gif"
"""
Now we are talking! 
I've got the divided top right and brought back the tabs
"""
add_library('GifAnimation')
from gif_exporter import gif_export
add_library('peasycam')
from draw_3D import draw_3D
from draw_2D import draw_unfolded

box_d, box_w, box_h = 100, 100, 100  # initial box dimensions
# height of points between d and c
edge_num = 4 # number of points on top lateral edges
cd_l = [box_h - 5 * i for i in range(edge_num)] 
# height of points between a and b
ab_l = [box_h + 5 * i for i in range(edge_num)] 
assert len(cd_l) == len(ab_l)  # equal number of points only

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
        face_3D_data = draw_3D(box_w, box_d, ab_l, cd_l)
    # Draw 2D unfolded
    # cam.beginHUD() # for use with PeasyCam
    with pushMatrix():
        translate(100, 350)
        draw_unfolded(box_w, box_d, ab_l, cd_l, face_3D_data)
    # cam.endHUD()

def keyPressed():
    global box_w, box_d, box_h
    # save frame on GIF
    # gif_export(GifMaker, filename=SKETCH_NAME)
    
    ah, bh, ch, dh = ab_l[0], ab_l[-1], cd_l[0], cd_l[-1]
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
    if keyCode == UP and box_d + box_w < 220:
        box_d += 5
    if keyCode == DOWN and box_d > 5:
        box_d -= 5
    if keyCode == RIGHT and box_w + box_d < 220:
        box_w += 5
    if keyCode == LEFT and box_w > 5:
        box_w -= 5
        
    ab_l[0], ab_l[-1], cd_l[0], cd_l[-1] = ah, bh, ch, dh    

    if key == "p":
        saveFrame("####.png")
    elif key in ("+", "="):
        box_h += 5
        cd_l[:] = [cd_l[i] + 5 for i in range(edge_num)] 
        ab_l[:] = [ab_l[i] + 5 for i in range(edge_num)] 
    elif (key == "-" and box_h > 5 and ah > 5 and bh > 5 and ch > 5 and dh > 5):
        box_h -= 5
        cd_l[:] = [cd_l[i] - 5 for i in range(edge_num)] 
        ab_l[:] = [ab_l[i] - 5 for i in range(edge_num)] 
    elif key == " ":
        slowly_reset_values()
        

def slowly_reset_values():
    global box_w, box_d, box_h, ah, bh, ch, dh

    box_w += (100 - box_w) / 2.
    box_d += (100 - box_d) / 2.
    delta_h = (100 - box_h) / 2.
    box_h += delta_h
    cd_l[:] = [cd_l[i] + delta_h for i in range(edge_num)] 
    ab_l[:] = [ab_l[i] + delta_h for i in range(edge_num)] 
