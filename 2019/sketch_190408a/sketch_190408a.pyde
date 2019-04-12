# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME, OUTPUT = "sketch_190408a", ".gif"
"""
With glue tabs!
"""
# add_library('GifAnimation')
# from gif_exporter import gif_export
# add_library('peasycam')
from third_point import third_point

CUT_COLOR = color(200, 0, 0)  # Color to mark outline cut
ENG_COLOR = color(0, 0, 200)  # Color to mark folding/engraving
TAB_W = 10  # tab width
TAB_A = radians(30)  # tab angle

box_d, box_w, box_h = 100, 100, 100  # initial values
ah = bh = ch = dh = box_h

def setup():
    size(850, 500, P3D)
    #global cam
    # cam = PeasyCam(this, 300)
    hint(ENABLE_DEPTH_SORT)
    smooth(16)
    strokeWeight(2)

def draw():
    background(200)
    # cam.beginHUD()
    with pushMatrix():
        translate(100, 350)
        draw_unfolded()
    # cam.endHUD()

    with pushMatrix():
        translate(width / 2, height / 2)  # comment out if with PeasyCam
        rotateX(QUARTER_PI)
        rotateZ(PI)
        translate(-300, -50, -100)
        draw_3d()

def draw_unfolded():
    bh_2d = (0, -bh)
    b0_2d = (0, 0)
    ch_2d = (box_w, -ch)
    c0_2d = (box_w, 0)
    dh_2d = (box_w + box_d, -dh)
    d0_2d = (box_w + box_d, 0)
    ah_2d = (box_w * 2 + box_d, -ah)
    a0_2d = (box_w * 2 + box_d, 0)

    noFill()
    stroke(ENG_COLOR)  # Marked for folding

    # verticals
    line_draw(b0_2d, bh_2d)
    line_draw(c0_2d, ch_2d)
    line_draw(d0_2d, dh_2d)
    line_draw(a0_2d, ah_2d)

    # lower triangle
    bd = dist(0, 0, bh, box_w, box_d, dh)
    cd = dist(box_w, 0, ch, box_w, box_d, dh)
    d2_2d = third_point(bh_2d, ch_2d, bd, cd)[0]  # gets the first solution
    line_draw(bh_2d, ch_2d)
    line_draw(bh_2d, d2_2d)
    line_draw(ch_2d, d2_2d)

    ab = dist(0, ah, box_w, bh)
    ad = dist(0, ah, box_d, dh)
    a2_2d = third_point(d2_2d, bh_2d, ab, ad)[1]  # gets the 1st solution too!
    line_draw(bh_2d, a2_2d)
    line_draw(d2_2d, a2_2d)

    # floor face
    rect(0, 0, box_w, box_d)

    stroke(CUT_COLOR)  # Marked for cutting

    # top tabs
    glue_tab(d2_2d, ch_2d, TAB_W, TAB_A)
    glue_tab(bh_2d, a2_2d, TAB_W, TAB_A)
    glue_tab(a2_2d, d2_2d, TAB_W, TAB_A)

    # middle tab
    glue_tab(b0_2d, bh_2d, TAB_W, TAB_A)

    # floor tabs
    glue_tab((0, box_d), b0_2d, TAB_W, TAB_A)
    glue_tab((box_w, box_d), (0, box_d), TAB_W, TAB_A)
    glue_tab((box_w, 0), (box_w, box_d), TAB_W, TAB_A)

    # main outline cut
    poly_draw((ch_2d, dh_2d, ah_2d,
               (box_w * 2 + box_d * 2, -bh),
               (box_w * 2 + box_d * 2, 0),
               c0_2d), closed=False)

def draw_3d():
    stroke(0)
    fill(255, 200)
    # floor face
    poly_draw(((0, 0, 0),
               (box_w, 0, 0),
               (box_w, box_d, 0),
               (0, box_d, 0)))
    # face 0
    poly_draw(((0, 0, bh),
               (box_w, 0, ch),
               (box_w, 0, 0),
               (0, 0, 0)))
    # face 1
    poly_draw(((box_w, box_d, dh),
               (box_w, 0, ch),
               (box_w, 0, 0),
               (box_w, box_d, 0)))
    # face 2
    poly_draw(((box_w, box_d, dh),
               (0, box_d, ah),
               (0, box_d, 0),
               (box_w, box_d, 0)))
    # face 3
    poly_draw(((0, 0, bh),
               (0, box_d, ah),
               (0, box_d, 0),
               (0, 0, 0)))
    # first triangle
    poly_draw(((0, 0, bh),
               (box_w, box_d, dh),
               (0, box_d, ah)))
    # second triangle
    poly_draw(((0, 0, bh),
               (box_w, box_d, dh),
               (box_w, 0, ch)))
    # diagonal
    stroke(ENG_COLOR)
    line(0, 0, bh, box_w, box_d, dh)

def poly_draw(points, closed=True):
    beginShape()
    for p in points:
        vertex(*p)
    if closed:
        endShape(CLOSE)
    else:
        endShape()

def line_draw(p1, p2):
    line(p1[0], p1[1], p2[0], p2[1])

def glue_tab(p1, p2, tab_w, cut_ang=QUARTER_PI):
    """
    draws a trapezoidal or triangular glue tab
    along edge defined by p1 and p2, 
    with width tab_w and cut angle a
    """
    a1 = atan2(p1[0] - p2[0], p1[1] - p2[1]) + cut_ang + PI
    a2 = atan2(p1[0] - p2[0], p1[1] - p2[1]) - cut_ang
    # calculate cut_len to get the right tab width
    cut_len = tab_w / sin(cut_ang)
    f1 = PVector(p1[0] + cut_len * sin(a1),
                 p1[1] + cut_len * cos(a1))
    f2 = PVector(p2[0] + cut_len * sin(a2),
                 p2[1] + cut_len * cos(a2))
    edge_len = dist(p1[0], p1[1], p2[0], p2[1])

    if edge_len > 2 * cut_len * cos(cut_ang):  # 'normal' trapezoidal tab
        beginShape()
        vertex(*p1)  # vertex(p1[0], p1[1])
        vertex(*f1)  # vertex(f1.x, f1.y)
        vertex(*f2)  # vertex(f2.x, f2.y)
        vertex(*p2)  # vertex(p2[0], p2[1])
        endShape()
    else:  # short triangular tab
        fm = (f1 + f2) / 2
        beginShape()
        vertex(*p1)  # (p1[0], p1[1])
        vertex(*fm)  # (fm.x, fm.y)
        vertex(*p2)  # (p2[0], p2[1])
        endShape()

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

def slowly_reset_values():
    global box_w, box_d, box_h, ah, bh, ch, dh
    box_w += (100 - box_w) / 2
    box_d += (100 - box_d) / 2
    box_h += (100 - box_h) / 2
    ah += (box_h - ah) / 2
    bh += (box_h - bh) / 2
    ch += (box_h - ch) / 2
    dh += (box_h - dh) / 2
