from draw_3D import poly_draw
from debug import *

CUT_COLOR = color(200, 0, 0)  # Color to mark outline cut
ENG_COLOR = color(0, 0, 200)  # Color to mark folding/engraving
TAB_W = 10  # tab width
TAB_A = radians(30)  # tab angle

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
    stroke(ENG_COLOR)  # Marked for folding

    # verticals
    line_draw(b0_2d, bh_2d)
    line_draw(c0_2d, ch_2d)
    line_draw(d0_2d, dh_2d)
    line_draw(a0_2d, ah_2d)
    debug_text("BCDA", (bh_2d, ch_2d, dh_2d, ah_2d))
    # divided top face
    start_1, start_2 = bh_2d, ch_2d
    for a, b, c, d in face_data:
        start_1, start_2 = unfold_tri_face((start_1, start_2), (a, b, c, d))

    # floor face
    rect(0, 0, box_w, box_d)
    # Marked for cutting
    stroke(CUT_COLOR)
    # top tab
    glue_tab(start_1, start_2, TAB_W, TAB_A)
    # middle tab
    glue_tab(b0_2d, bh_2d, TAB_W, TAB_A)
    # floor tabs
    glue_tab((0, box_d), b0_2d, TAB_W, TAB_A)
    glue_tab((box_w, box_d), (0, box_d), TAB_W, TAB_A)
    glue_tab((box_w, 0), (box_w, box_d), TAB_W, TAB_A)

    # main outline cut
    num_i = len(cd_i)
    cd_pts = [(box_w + box_d * i / (num_i - 1), -cd_i[i])
              for i in range(num_i)]
    ab_pts = [(box_w * 2 + box_d + box_d * i / (num_i - 1), -ab_i[i])
              for i in range(num_i)]
    main_outline = tuple(cd_pts + ab_pts) + ((box_w * 2 + box_d * 2, 0), c0_2d)
    poly_draw(main_outline, closed=False)

def line_draw(p1, p2, tab=False):
    line(p1[0], p1[1], p2[0], p2[1])
    if tab:
        with pushStyle():
            stroke(CUT_COLOR)
            glue_tab(p1, p2, TAB_W, TAB_A)    

def glue_tab(p1, p2, tab_w=10, cut_ang=QUARTER_PI):
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

def unfold_tri_face(pts_2D, pts_3D):
    """
    gets a collection of 2 (B, D) starting 2D points (PVectors or tuples)
    Gets a collection of 4 (A, B, C, D) 3D points (PVectors or tuples)
    Draws the unfolded face a returns (A, C) 2D positions.
    """
    b2D, c2D = pts_2D
    a3D, b3D, c3D, d3D = pts_3D
    bd_len = dist(b3D[0], b3D[1], b3D[2], d3D[0], d3D[1], d3D[2])
    cd_len = dist(c3D[0], c3D[1], c3D[2], d3D[0], d3D[1], d3D[2])
    # lower triangle
    d2D = third_point(b2D, c2D, bd_len, cd_len)[0]  # gets the first solution
    line_draw(b2D, c2D)
    line_draw(b2D, d2D)
    line_draw(d2D, c2D, tab=True)
    # upper triangle (fixed from 190408a)
    ab_len = dist(b3D[0], b3D[1], b3D[2], a3D[0], a3D[1], a3D[2])
    ad_len = dist(a3D[0], a3D[1], a3D[2], d3D[0], d3D[1], d3D[2])
    a2D = third_point(b2D, d2D, ab_len, ad_len)[0]  # gets the 1st solution too! 
    line_draw(b2D, a2D, tab=True)
    line_draw(d2D, a2D)
    return (a2D, d2D)

"""
Code adapted from code by Monkut https://stackoverflow.com/users/24718/monkut
found at https://stackoverflow.com/questions/4001948/drawing-a-triangle-in-a-coordinate-plane-given-its-three-sides
"""

class NoTrianglePossible(BaseException):
    pass

def third_point(a, b, ac_len, bc_len):
    """
    Returns two point c options given:
    point a, point b, ac length, bc length    
    """
    # To allow use of tuples, creates or recreates PVectors
    a, b = PVector(*a), PVector(*b)

    # check if a triangle is possible
    ab_len = a.dist(b)
    if ab_len > (ac_len + bc_len) or ab_len < abs(ac_len - bc_len):
        raise NoTrianglePossible("The sides do not form a triangle")

    # get the length to the vertex of the right triangle formed,
    # by the intersection formed by circles a and b
    ad_len = (ab_len ** 2 + ac_len ** 2 - bc_len ** 2) / (2.0 * ab_len)

    # get the height of the line at a right angle from a_len
    h = sqrt(abs(ac_len ** 2 - ad_len ** 2))

    # Calculate the mid PVector (point d), needed to calculate point c(1|2)
    d_x = a.x + ad_len * (b.x - a.x) / ab_len
    d_y = a.y + ad_len * (b.y - a.y) / ab_len
    d = PVector(d_x, d_y)

    # get point_c locations
    c_x1 = d.x + h * (b.y - a.y) / ab_len
    c_x2 = d.x - h * (b.y - a.y) / ab_len
    c_y1 = d.y - h * (b.x - a.x) / ab_len
    c_y2 = d.y + h * (b.x - a.x) / ab_len

    return PVector(c_x1, c_y1), PVector(c_x2, c_y2)
