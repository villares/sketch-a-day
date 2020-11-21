from villares.line_geometry import hatch_poly, draw_poly, poly_edges
def setup():
    size(400, 400)

def draw():
    background(100, 100, 230)
    stroke(0)
    fill(255)
    r = [(75, 150), (325, 150), (325, 350), (75, 350)]
    r.insert(1, (mouseX, mouseY))

    draw_poly(r)
    angs = [int(degrees(atan2(e[0][1] - e[1][1], e[0][0] - e[1][0]) + PI + HALF_PI))
            for e in poly_edges(r)]
    angs = {ang if ang < 180 else
            ang - 180 if ang < 360 else
            ang - 360
            for ang in angs}
    text(str(angs), 30, 30)
    for ang in angs:
        hatch_poly(r, radians(ang), spacing=10)


# older attempts
# from villares.line_geometry import hatch_poly, draw_poly, rect_points, edges, rotate_point

# def setup():
#     size(400, 400)

# def draw():
#     background(100, 100, 230)
#     stroke(0)
#     fill(255)
#     r = [rotate_point(p[0], p[1], 0, 200, 200)
#          for p in rect_points(75, 150, 250, 200)]
#     r.insert(1, (mouseX, mouseY))
#     r.extend(rect_points(150, 120, 50, 50))
#     draw_poly(r)
#     es = edges(r)[:-1]
#     angs = [int(degrees(atan2(e[0][1] - e[1][1], e[0][0] - e[1][0]) + PI + HALF_PI))
#             for e in es]
#     angs = {ang if ang < 180 else
#             ang - 180 if ang < 360 else
#             ang - 360
#             for ang in angs}
#     text(str(angs), 30, 30)
#     for ang in angs:
#         hatch_poly(r, radians(ang), spacing=10)
