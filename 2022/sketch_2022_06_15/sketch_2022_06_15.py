# unnecessary when importing from villares.arc.py module
beginShape = begin_shape
endShape = end_shape
bezierVertex = bezier_vertex
textSize = text_size
DEBUG, TEXT_HEIGHT = False, 12

from villares.arcs import arc_augmented_poly

def setup():
    size(900, 900, P3D)
    cursor(CROSS)

def draw():
    background(0, 0, 100)
    translate(width / 2, height / 2 + 100)
    rotate_x(QUARTER_PI)
    input_pts = (
        (-250, -250),
        (200, -300),
        (150, 125),
        (mouse_x - width / 2, mouse_y - height / 2),
    )

    for i in range(10):
        output_pts = arc_augmented_points(
            input_pts,
            radius=10 + i * 10,
            auto_flip=True,
            gradual_flip=True,
            min_dist=5,
        )
        no_fill()
        stroke(200)
        stroke_weight(2)
        with begin_closed_shape():
            vertices(output_pts)
        translate(0, 0, 20)
        stroke_weight(5)
        stroke(250, 100, 0)
        points(output_pts)


def arc_augmented_points(op_list, or_list=None, **kwargs):
    """
    A version of arc_augmented_poly that returns the points
    of a poly-approximation with arc_pts
    """

    def mid(p0, p1):
        return (p0[0] + p1[0]) * 0.5, (p0[1] + p1[1]) * 0.5

    assert op_list, 'No points were provided.'
    assert not (
        'radius' in kwargs and or_list
    ), "You can't use a radii list and a radius kwarg together."
    if 'radius' in kwargs and or_list == None:
        or_list = [kwargs.pop('radius')] * len(op_list)
    r2_list = list(or_list)
    assert len(op_list) == len(
        r2_list
    ), 'Number of points and radii provided not the same.'
    auto_flip = kwargs.pop('auto_flip', True)
    gradual_flip = kwargs.pop('gradual_flip', False)  # experimentas
    pts_list = []
    # remove overlapping adjacent points
    p_list, r_list = [], []
    p2_list = list(op_list)
    for i1, p1 in reversed(list(enumerate(p2_list))):
        i2 = (i1 + 1) % len(p2_list)
        p2, r2, r1 = p2_list[i2], r2_list[i2], r2_list[i1]
        d = dist(p1[0], p1[1], p2[0], p2[1])
        if d > abs(r1 - r2):
            p_list.append(p1)
            r_list.append(r1)
        else:
            p2_list[i2] = mid(p1, p2)
            r2_list[i2] = max(r1, r2)
    # invert radius
    for i1, p1 in enumerate(p_list):
        i0 = i1 - 1
        p0 = p_list[i0]
        i2 = (i1 + 1) % len(p_list)
        p2, r2, r1, r0 = p_list[i2], r_list[i2], r_list[i1], r_list[i0]

        cct0 = circ_circ_tangent(p0, p1, r0, r1)
        cct1 = circ_circ_tangent(p1, p2, r1, r2)
        ang0, a0, b0 = cct0
        ang1, a1, b1 = cct1
        a = triangle_area(a0, b0, b1) / 1000

        if auto_flip and simple_intersect(a0, b0, a1, b1):
            r_list[i1] = -r_list[i1]
            #         if auto_flip and a < 0:
            #              r_list[i1] = -r_list[i1]
            if gradual_flip:
                r_list[i1] = r_list[i1] * min(1, abs(a))
    # reduce radius that won't fit
    for i1, p1 in enumerate(p_list):
        i2 = (i1 + 1) % len(p_list)
        p2, r2, r1 = p_list[i2], r_list[i2], r_list[i1]
        r_list[i1], r_list[i2] = reduce_radius(p1, p2, r1, r2)
    # calculate the tangents
    a_list = []
    for i1, p1 in enumerate(p_list):
        i2 = (i1 + 1) % len(p_list)
        p2, r2, r1 = p_list[i2], r_list[i2], r_list[i1]
        cct = circ_circ_tangent(p1, p2, r1, r2)
        a_list.append(cct)
        if DEBUG:
            push()
            ang, (xa, ya), (xb, yb) = cct
            stroke(255, 0, 0)
            stroke_weight(5)
            line(xa, ya, xb, yb)
            pop()
    # now draw it!
    for i1, ia in enumerate(a_list):
        i2 = (i1 + 1) % len(a_list)
        p1, p2, r1, r2 = p_list[i1], p_list[i2], r_list[i1], r_list[i2]
        a1, p11, p12 = ia
        a2, p21, p22 = a_list[i2]
        if DEBUG:
            circle(p1[0], p1[1], r1 * 2)
        if a1 != None and a2 != None:
            start = a1 if a1 < a2 else a1 - TWO_PI   # was <
            if r2 < 0:  # was <=
                a2 = a2 - TWO_PI
            abs_angle = abs(a2 - start)
            if abs_angle > TWO_PI:
                if a2 < 0:
                    a2 += TWO_PI
                else:
                    a2 -= TWO_PI
            if abs(a2 - start) != TWO_PI:
                pts_list.extend(
                    arc_pts(p2[0], p2[1], r2 * 2, r2 * 2, start, a2, **kwargs)
                )
            if DEBUG:
                textSize(TEXT_HEIGHT)
                text(
                    ' {:0.2f} {:0.2f}'.format(r2, degrees(abs_angle)),
                    p2[0],
                    p2[1],
                )
        else:
            # when the the segment is smaller than the diference between
            # radius, circ_circ_tangent won't renturn the angle
            if DEBUG:
                ellipse(p2[0], p2[1], r1, r1)
            if a1:
                pts_list.append((p12[0], p12[1]))
            if a2:
                pts_list.append((p21[0], p21[1]))
    return pts_list


def reduce_radius(p1, p2, r1, r2, reduce_both=True):
    d = dist(p1[0], p1[1], p2[0], p2[1])
    ri = abs(r1 - r2)
    if d - ri <= 0:
        if reduce_both:
            r1, r2 = (
                remap(d, ri + 1, 0, r1, (r1 + r2) / 2),
                remap(d, ri + 1, 0, r2, (r1 + r2) / 2),
            )
        elif abs(r1) > abs(r2):
            r1 = remap(d, ri + 1, 0, r1, r2)
        else:
            r2 = remap(d, ri + 1, 0, r2, r1)
    return r1, r2


def circ_circ_tangent(p1, p2, r1, r2):
    d = dist(p1[0], p1[1], p2[0], p2[1])
    ri = r1 - r2
    line_angle = atan2(p1[0] - p2[0], p2[1] - p1[1])
    if d - abs(ri) >= 0:
        theta = asin(ri / float(d))
        x1 = -cos(line_angle + theta) * r1
        y1 = -sin(line_angle + theta) * r1
        x2 = -cos(line_angle + theta) * r2
        y2 = -sin(line_angle + theta) * r2
        return (
            line_angle + theta,
            (p1[0] - x1, p1[1] - y1),
            (p2[0] - x2, p2[1] - y2),
        )
    else:
        return (None, (p1[0], p1[1]), (p2[0], p2[1]))


def triangle_area(a, b, c):
    area = a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])
    return area


def arc_pts(cx, cy, w, h, start_angle, end_angle, num_points=24, min_dist=0):
    """
    Returns points approximating an arc using the same
    signature as the original Processing arc().
    """
    sweep_angle = end_angle - start_angle
    if abs(sweep_angle) < 0.0001:
        vx = cx + cos(start_angle) * w / 2.0
        vy = cy + sin(start_angle) * h / 2.0
        return [(vx, vy)]
    pts_list = []
    step_angle = float(sweep_angle) / num_points
    va = start_angle
    side = 1 if sweep_angle > 0 else -1
    while va * side < end_angle * side or abs(va - end_angle) < 0.0001:
        vx = cx + cos(va) * w / 2.0
        vy = cy + sin(va) * h / 2.0
        pts_list.append((vx, vy))
        va += step_angle
    if not min_dist or len(pts_list) < 3:
        return pts_list
    else:
        #    def simplify_pts(pts_list, min_dist):
        previous_x, previous_y = pts_list[0]
        pts_simplified = [pts_list[0]]
        for x, y in pts_list[1:]:
            if dist(x, y, previous_x, previous_y) >= min_dist:
                pts_simplified.append((x, y))
                previous_x, previous_y = x, y
        return pts_simplified


def ccw(a, b, c):
    """Returns True if the points are arranged counter-clockwise in the plane"""
    return (b[0] - a[0]) * (c[1] - a[1]) > (b[1] - a[1]) * (c[0] - a[0])


def simple_intersect(a1, b1, a2, b2):
    """Returns True if line segments intersect."""
    return ccw(a1, b1, a2) != ccw(a1, b1, b2) and ccw(a2, b2, a1) != ccw(
        a2, b2, b1
    )
