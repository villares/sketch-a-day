from draw_3D import poly_draw
from third_point import third_point
from debug import *

def draw_unfolded(box_w, box_d, ab_i, cd_i, face_data):
    bh_2d = (0, -ab_i[-1])
    b0_2d = (0, 0)
    ch_2d = (box_w, -cd_i[0])
    c0_2d = (box_w, 0)
    dh_2d = (box_w + box_d, -cd_i[-1])
    d0_2d = (box_w + box_d, 0)
    ah_2d = (box_w * 2 + box_d, -ab_i[0])
    a0_2d = (box_w * 2 + box_d, 0)

    noFill()
    # stroke(ENG_COLOR)  # Marked for folding

    # verticals
    line_draw(b0_2d, bh_2d)
    line_draw(c0_2d, ch_2d)
    line_draw(d0_2d, dh_2d)
    line_draw(a0_2d, ah_2d)
    # lower triangle
    # b_c1 = dist(0, 0, ab_i[-1], box_w, box_d / len(cd_i)-1, cd_i[1])
    # c_d1 = dist(box_w, 0, cd_i[0], box_w, box_d / len(cd_i)-1, cd_i[1])
    debug_text("BCDA", (bh_2d, ch_2d, dh_2d, ah_2d))

    for bc, cd, da, ab in face_data:
        d2_2d = third_point(ch_2d, bh_2d, cd, bc)[1]  # gets the first solution
        line_draw(bh_2d, ch_2d)
        line_draw(bh_2d, d2_2d)
        line_draw(ch_2d, d2_2d)
        # upper triangle
        a2_2d = third_point(bh_2d, d2_2d, ab, bc)[0]  # gets the second solution
        line_draw(bh_2d, a2_2d)
        line_draw(d2_2d, a2_2d)
        bh_2d = d2_2d
        ch_2d = a2_2d
        
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
