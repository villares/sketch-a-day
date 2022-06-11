
def setup():
    size(600, 600)
    
def draw():
    background(100, 150, 100)
    pts = var_bar_pts(mouse_x, mouse_y, 200, 300, 40, 100, num_points=16)
    stroke_weight(1)
    with begin_closed_shape():
        vertices(pts)
    stroke_weight(5)
    points(pts)

def arc_pts(cx, cy, w, h, start_angle, end_angle, num_points=24):
    """
    Returns points approximating an arc using the same
    signature as the original Processing arc().
    """
    result = []
    sweep_angle = end_angle - start_angle
    if sweep_angle == 0:
        vx = cx + cos(start_angle) * w / 2.0
        vy = cy + sin(start_angle) * h / 2.0
        return [(vx, vy)]
    step_angle = float(sweep_angle) / num_points    
    va = start_angle
    side = 1 if sweep_angle > 0 else -1
    while va * side < end_angle * side:
        vx = cx + cos(va) * w / 2.0
        vy = cy + sin(va) * h / 2.0
        result.append((vx, vy))
        va += step_angle
    return result

def var_bar_pts(p1x, p1y, p2x, p2y, r1, r2=None, **kwargs):
    """
    Tangent/tangent shape on 2 circles of arbitrary radius
    """
    r2 = r2 if r2 is not None else r1
    shorter = kwargs.pop('shorter', 0)
    assert not (shorter and r1 != r2),\
        "Can't draw shorter var_bar with different radii"
    d = dist(p1x, p1y, p2x, p2y)
    ri = r1 - r2
    result = []
    if d > abs(ri):
        clipped_ri_over_d = min(1, max(-1, ri / d))
        beta = asin(clipped_ri_over_d) + HALF_PI
        angle = atan2(p1x - p2x, p2y - p1y) + HALF_PI
        offset = shorter / 2.0 if shorter < d else d / 2.0
        result.extend(arc_pts(offset, 0, r1 * 2, r1 * 2,
                     -beta - PI, beta - PI, **kwargs))
        result.extend(arc_pts(d - offset, 0, r2 * 2, r2 * 2,
                      beta - PI, PI - beta, **kwargs))
        return rotate_offset_points(result, angle, p1x, p1y)
    else:
        r = max(r1, r2)
        x, y = (p1x, p1y) if r1 > r2 else (p2x, p2y)
        return arc_pts(x, y, r * 2, r * 2, 0, TWO_PI, **kwargs)
                          
def rotate_offset_points(pts, angle, offx, offy, y0=0, x0=0):
    return [(((xp - x0) * cos(angle) - (yp - y0) * sin(angle)) + x0 + offx,
             ((yp - y0) * cos(angle) + (xp - x0) * sin(angle)) + y0 + offy)
            for xp, yp in pts]
    