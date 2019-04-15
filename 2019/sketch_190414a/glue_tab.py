def glue_tab(p1, p2, tab_w=10, cut_ang=QUARTER_PI/2):
    """
    draws a trapezoidal or triangular glue tab
    along edge defined by p1 and p2, with provided
    width (tab_w) and cut angle (cut_ang)
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
