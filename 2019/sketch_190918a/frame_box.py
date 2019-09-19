CUT_STROKE, FOLD_STROKE = color(255, 0, 0), color(0, 0, 255)

def frame_box(w, h, d, thick=0):
    """ draw the 3D version of the box with rectangular holes """
    mw, mh, md = w / 2., h / 2., d / 2.
    translate(0, 0, -md)  # base
    face(0, 0, w, h, thick)
    translate(0, 0, d)  # top
    face(0, 0, w, h, thick)
    translate(0, 0, -md)  # back to 0
    rotateY(HALF_PI)
    translate(0, 0, -mw)  # left side
    face(0, 0, d, h, thick)
    translate(0, 0, w)  # right side
    face(0, 0, d, h, thick)
    translate(0, 0, -mw)  # back to middle
    rotateY(-HALF_PI)  # back to 0 rotation
    rotateX(HALF_PI)
    translate(0, 0, -mh)  # lateral e
    face(0, 0, w, d, thick)
    translate(0, 0, h)  # lateral d
    face(0, 0, w, d, thick)
    translate(0, 0, -mw)  # reset translate
    rotateX(-HALF_PI)  # reset rotate

def face(x, y, w, h, e):
    mw, mh = w / 2., h / 2.
    pushMatrix()
    translate(x, y)
    beginShape()
    vertex(-mw, -mh)
    vertex(+mw, -mh)
    vertex(+mw, +mh)
    vertex(-mw, +mh)
    hole(mw, mh, e)
    endShape(CLOSE)
    popMatrix()

def hole(mw, mh, e):
        if e > 0 and mw - e > 0 and mh - e > 0:
            beginContour()
            np = 24
            for i in range(np):
                ang = TWO_PI / np * i
                x = sin(ang) * e
                y = cos(ang) * e
                vertex(x, y)
            endContour()
    


def unfolded_frame_box(w, h, d, thick=0, draw_main=True):
    mw, mh, md = w / 2., h / 2., d / 2.
    unfolded_face(0, -h - md, w, d, "aaan", thick, draw_main)
    unfolded_face(0, -mh, w, h, "vvvv", thick, draw_main)
    unfolded_face(0, -mh + mh + md, w, d, "cncv", thick, draw_main)
    unfolded_face(0, +mh + d, w, h, "cncc", thick, draw_main)
    unfolded_face(-mw - md, -mh, d, h, "acna", thick, draw_main)
    unfolded_face(mw + md, -mh, d, h, "ncaa", thick, draw_main)

def unfolded_face(x, y, w, h, edge_types, thick=0, draw_main=True):
    e0, e1, e2, e3 = edge_types
    mw, mh = w / 2., h / 2.
    pushMatrix()
    translate(x, y)
    if draw_main:
        edge(-mw, +mh, -mw, -mh, e0)
        edge(-mw, -mh, +mw, -mh, e1)
        edge(+mw, -mh, +mw, +mh, e2)
        edge(+mw, +mh, -mw, +mh, e3)
    if thick > 0 and mw - thick > 0 and mh - thick > 0:
        stroke(CUT_STROKE)
        circle(0, 0, thick * 2)
    popMatrix()

def edge(x0, y0, x1, y1, edge_type):
    if edge_type == "n":  # no edge is drawn
        return
    elif edge_type == "c":  # cut stroke selected
        stroke(CUT_STROKE)
    else:
        stroke(FOLD_STROKE)  # fold stroke selected for "v" and "a"
    line(x0, y0, x1, y1)    # line drawn here
    if edge_type == "a":    # tab (note a fold-stroke line was already drawn)
        stroke(CUT_STROKE)
        noFill()
        glue_tab((x0, y0), (x1, y1), 10)

def glue_tab(p1, p2, tab_w, cut_ang=QUARTER_PI / 3):
    """
    draws a trapezoidal or triangular glue tab along edge defined by p1 and p2,
    with width tab_w and cut angle a
    """
    al = atan2(p1[0] - p2[0], p1[1] - p2[1])
    a1 = al + cut_ang + PI
    a2 = al - cut_ang
    # calculate cut_len to get the right tab width
    cut_len = tab_w / sin(cut_ang)
    f1 = (p1[0] + cut_len * sin(a1),
          p1[1] + cut_len * cos(a1))
    f2 = (p2[0] + cut_len * sin(a2),
          p2[1] + cut_len * cos(a2))
    edge_len = dist(p1[0], p1[1], p2[0], p2[1])

    if edge_len > 2 * cut_len * cos(cut_ang):    # 'normal' trapezoidal tab
        beginShape()
        vertex(*p1)    # vertex(p1[0], p1[1])
        vertex(*f1)
        vertex(*f2)
        vertex(*p2)
        endShape()
    else:    # short triangular tab
        fm = ((f1[0] + f2[0]) / 2, (f1[1] + f2[1]) / 2)
        beginShape()
        vertex(*p1)
        vertex(*fm)    # middle way of f1 and f2
        vertex(*p2)
        endShape()
