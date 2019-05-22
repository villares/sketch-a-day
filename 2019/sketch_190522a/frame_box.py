CORTE, VINCO = color(255, 0, 0), color(0, 0, 255)

def face(x, y, w, h, e):
    mw, mh = w / 2., h / 2.
    pushMatrix()
    translate(x, y)
    beginShape()
    vertex(-mw, -mh)
    vertex(+mw, -mh)
    vertex(+mw, +mh)
    vertex(-mw, +mh)
    if e > 0 and mw - e > 0 and mh - e > 0:
        mw -= e
        mh -= e
        beginContour()
        vertex(-mw, -mh)
        vertex(-mw, +mh)        
        vertex(+mw, +mh)
        vertex(+mw, -mh)
        endContour()
    endShape(CLOSE)
    popMatrix()
    
def frame_box(w, h, d, e=0):
     mw, mh, md = w/2., h/2., d/2.
     translate(0, 0, -md) # base
     face(0, 0, w, h, e)
     translate(0, 0, d) # topo
     face(0, 0, w, h, e)
     translate(0, 0, -md) # volta
     rotateY(HALF_PI)
     translate(0, 0, -mw) # lateral e
     face(0, 0, d, h, e)
     translate(0, 0, w) # lateral d
     face(0, 0, d, h, e)
     translate(0, 0, -mw) # volta    
     rotateY(-HALF_PI)  # volta
     rotateX(HALF_PI)
     translate(0, 0, -mh) # lateral e
     face(0, 0, w, d, e)
     translate(0, 0, h) # lateral d
     face(0, 0, w, d, e)
     translate(0, 0, -mw) # volta         
     rotateX(-HALF_PI)

def unfolded_box(w, h, d, e=0, draw_main=True):
    mw, mh, md = w / 2., h / 2., d / 2.
    face_unfold(0, -h - md, w, d, "aaan", e, draw_main)
    face_unfold(0, -mh, w, h, "vvvv", e, draw_main)
    face_unfold(0, -mh + mh + md, w, d, "cncv", e, draw_main)
    face_unfold(0, +mh + d, w, h, "cncc", e, draw_main)
    face_unfold(-mw - md, -mh, d, h, "acna", e, draw_main)
    face_unfold(mw + md, -mh, d, h, "ncaa", e, draw_main)

def face_unfold(x, y, w, h, sides, e=0, draw_main=True):
    l0, l1, l2, l3 = sides
    mw, mh = w / 2., h / 2.
    pushMatrix()
    translate(x, y)
    if draw_main:
        edge(-mw, +mh, -mw, -mh, l0)
        edge(-mw, -mh, +mw, -mh, l1)
        edge(+mw, -mh, +mw, +mh, l2)
        edge(+mw, +mh, -mw, +mh, l3)
    if e > 0 and mw - e > 0 and mh - e > 0:
        face_unfold(0, 0, w - e * 2, h - e * 2, "cccc")
    popMatrix()

def edge(x0, y0, x1, y1, edge_type):
    if edge_type == "n":
        return
    elif edge_type == "c":
        stroke(CORTE)
    else:
        stroke(VINCO)
    line(x0, y0, x1, y1)
    if edge_type == "a":
        stroke(CORTE)
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
