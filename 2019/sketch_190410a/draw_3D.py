from debug import *

def draw_3d(box_w, box_d, ab_i, cd_i):
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
    poly_draw(((0, 0, ab_i[-1]),
               (box_w, 0, cd_i[0]),
               (box_w, 0, 0),
               (0, 0, 0)))
    # face 1
    poly_draw(cd_pts + (
        (box_w, 0, 0),
        (box_w, box_d, 0)))
    # face 2
    poly_draw(((box_w, box_d, cd_i[-1]),
               (0, box_d, ab_i[0]),
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

        debug_text("cd", cd_pts[::-1], enum=True)
        debug_text("ab", ab_pts[::-1], enum=True)
        debug_text("DAad", ((box_w, box_d, cd_i[-1]),
                            (0, box_d, ab_i[0]),
                            (0, box_d, 0),
                            (box_w, box_d, 0)))

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
