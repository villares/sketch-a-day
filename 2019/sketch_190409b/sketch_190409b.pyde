# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME, OUTPUT = "sketch_190409b", ".gif"
"""
Subdivided top! (not quite there yet...)
"""
add_library('GifAnimation')
from gif_exporter import gif_export
add_library('peasycam')
from third_point import third_point

CUT_COLOR = color(200, 0, 0)  # Color to mark outline cut
ENG_COLOR = color(0, 0, 200)  # Color to mark folding/engraving
TAB_W = 10  # tab width
TAB_A = radians(30)  # tab angle
DEBUG = True

box_d, box_w, box_h = 100, 100, 100  # initial box dimensions
ah = bh = ch = dh = box_h  # initial height of points a, b, c and d
# height of points between d and c
cd_i = [box_h, box_h + 15, box_h + 18, box_h + 15, box_h]
# height of points between a and b
ab_i = [box_h, box_h - 15, box_h - 18, box_h - 15, box_h]

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
    # update top face point lists
    cd_i[0] = ch
    cd_i[-1] = dh
    ab_i[0] = ah
    ab_i[-1] = bh
    # cam.beginHUD() # for use with PeasyCam
    with pushMatrix():
        translate(100, 350)
        draw_unfolded()
    # cam.endHUD()

    with pushMatrix():
        translate(width / 2, height / 2)  # Comment out if using with PeasyCam
        rotateX(QUARTER_PI)
        rotateZ(0)
        translate(200, -50, -100)
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
    # debug_text("BbCcDdAa", (bh_2d, b0_2d, ch_2d, c0_2d, dh_2d, d0_2d, ah_2d, a0_2d))

    noFill()
    # stroke(ENG_COLOR)  # Marked for folding

    # verticals
    line_draw(b0_2d, bh_2d)
    line_draw(c0_2d, ch_2d)
    line_draw(d0_2d, dh_2d)
    line_draw(a0_2d, ah_2d)
    # lower triangle
    b_c1 = dist(0, 0, bh, box_w, box_d / len(cd_i)-1, cd_i[1])
    c_c1 = dist(box_w, 0, ch, box_w, box_d / len(cd_i)-1, cd_i[1])
    d2_2d = third_point(bh_2d, ch_2d, b_c1, c_c1)[0]  # gets the first solution
    line_draw(bh_2d, ch_2d)
    line_draw(bh_2d, d2_2d)
    line_draw(ch_2d, d2_2d)
    debug_text("BCDA", (bh_2d, ch_2d, dh_2d, ah_2d))
    # upper triangle

    ab = dist(0, ab_i[::-1][1], box_w, bh)
    ad = dist(0, ab_i[::-1][1], box_d / 3, ab_i[::-1][1])
    a2_2d = third_point(d2_2d, bh_2d, ab, ad)[1]  # gets the second solution
    line_draw(bh_2d, a2_2d)
    line_draw(d2_2d, a2_2d)
    # floor face
    rect(0, 0, box_w, box_d)

    # stroke(CUT_COLOR)  # Marked for cutting
    # top tabs
    # glue_tab(d2_2d, ch_2d, TAB_W, TAB_A)
    # glue_tab(bh_2d, a2_2d, TAB_W, TAB_A)
    # glue_tab(a2_2d, d2_2d, TAB_W, TAB_A)
    # middle tab
    # glue_tab(b0_2d, bh_2d, TAB_W, TAB_A)
    # floor tabs
    # glue_tab((0, box_d), b0_2d, TAB_W, TAB_A)
    # glue_tab((box_w, box_d), (0, box_d), TAB_W, TAB_A)
    # glue_tab((box_w, 0), (box_w, box_d), TAB_W, TAB_A)

    # main outline cut
    num_i = len(cd_i)
    cd_pts = [(box_w + box_d * i / (num_i - 1), -cd_i[i])
              for i in range(num_i)]
    ab_pts = [(box_w * 2 + box_d + box_d * i / (num_i - 1), -ab_i[i])
              for i in range(num_i)]
    main_outline = tuple(cd_pts + ab_pts) + ((box_w * 2 + box_d * 2, 0), c0_2d)
    poly_draw(main_outline, closed=False)

def draw_3d():
    stroke(0)
    fill(255, 200)
    # floor face
    poly_draw(((0, 0, 0),
               (box_w, 0, 0),
               (box_w, box_d, 0),
               (0, box_d, 0)))

    num_i = len(cd_i)
    cd_pts = tuple([(box_w, box_d - box_d * i / (num_i - 1), cd_i[::-1][i])
                    for i in range(num_i)])
    ab_pts = tuple([(0, box_d * i / (num_i - 1), ab_i[::-1][i])
                    for i in range(num_i)])
    # face 0
    poly_draw(((0, 0, bh),
               (box_w, 0, ch),
               (box_w, 0, 0),
               (0, 0, 0)))
    # face 1
    poly_draw(cd_pts + (
        (box_w, 0, 0),
        (box_w, box_d, 0)))
    # face 2
    poly_draw(((box_w, box_d, dh),
               (0, box_d, ah),
               (0, box_d, 0),
               (box_w, box_d, 0)))
    # face 3
    poly_draw(ab_pts + (
        (0, box_d, 0),
        (0, 0, 0)))
    # top faces

    for i in range(1, len(ab_pts)):
        p = i - 1
        x = screenX(*cd_pts[::-1][p])
        y = screenY(*cd_pts[::-1][p])

        triangulated_face(
            cd_pts[::-1][p], ab_pts[p], ab_pts[i], cd_pts[::-1][i])

        debug_text("cd", cd_pts, enum=True)
        debug_text("ab", ab_pts, enum=True)
        debug_text("DAad", ((box_w, box_d, dh),
                            (0, box_d, ah),
                            (0, box_d, 0),
                            (box_w, box_d, 0)))

def debug_text(name, points, enum=False):
    if DEBUG:
        for i, p in enumerate(points):
            with push():
                
                fill(255, 0, 0)
                if enum:
                    translate(0, -5, 10)
                    text(name + "-" + str(i), *p)
                else:
                    translate(10, 10, 10)
                    text(name[i], *p)

    # diagonal
    # stroke(ENG_COLOR)
    # line(0, 0, bh, box_w, box_d, dh)

def poly_draw(points, closed=True):
    beginShape()
    for p in points:
        vertex(*p)
    if closed:
        endShape(CLOSE)
    else:
        endShape()

def triangulated_face(a, b, c, d):
    poly_draw((b, d, a))
    poly_draw((b, d, c))

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
    f1 = (p1[0] + cut_len * sin(a1),
          p1[1] + cut_len * cos(a1))
    f2 = (p2[0] + cut_len * sin(a2),
          p2[1] + cut_len * cos(a2))
    edge_len = dist(p1[0], p1[1], p2[0], p2[1])

    if edge_len > 2 * cut_len * cos(cut_ang):  # 'normal' trapezoidal tab
        beginShape()
        vertex(*p1)  # vertex(p1[0], p1[1])
        vertex(*f1)
        vertex(*f2)
        vertex(*p2)
        endShape()
    else:  # short triangular tab
        fm = ((f1[0] + f2[0]) / 2, (f1[1] + f2[1]) / 2)
        beginShape()
        vertex(*p1)
        vertex(*fm)  # middle way of f1 and f2
        vertex(*p2)
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
        saveFrame("####.png")

def slowly_reset_values():
    global box_w, box_d, box_h, ah, bh, ch, dh
    box_w += (100 - box_w) / 2
    box_d += (100 - box_d) / 2
    box_h += (100 - box_h) / 2
    ah += (box_h - ah) / 2
    bh += (box_h - bh) / 2
    ch += (box_h - ch) / 2
    dh += (box_h - dh) / 2
