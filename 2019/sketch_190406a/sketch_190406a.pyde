"""
Terrain Box
"""

add_library('peasycam')
from third_point import third_point
from face_draw import face_draw

L, H = 100, 100
A, B, C, D = H + 10, H + 0, H + 50, H + 20

def setup():
    global cam
    size(800, 500, P3D)
    cam = PeasyCam(this, 660)
    hint(ENABLE_DEPTH_SORT)

def draw():
    # lights()
    background(200)
    # ortho()
    strokeWeight(2)
    stroke(0)
    fill(255, 200)
    translate(100, 0, -100)
    faces_3D()
    cam.beginHUD()
    translate(100, 300)
    faces_2D()
    cam.endHUD()

def faces_2D():
    noFill()
    stroke(0)
    b_2d = PVector(0, -B)
    c_2d = PVector(L, -C)

    face_draw((b_2d, c_2d, (L, 0), (0, 0)))  # face 0
    face_draw((c_2d, (L * 2, -D), (L * 2, 0), (L, 0)))  # face 1
    face_draw(((L * 2, -D), (L * 3, -A), (L * 3, 0), (L * 2, 0)))  # face 2
    face_draw(((L * 3, -A), (L * 4, -B), (L * 4, 0), (L * 3, 0)))  # face 3

    bc = PVector.dist(b_2d, c_2d)  # (0, 0, -B, L, 0, -C)
    bd = dist(0, 0, B, L, L, D)
    cd = dist(L, 0, C, L, L, D)
    d_2d = third_point(b_2d, c_2d, bd, cd)
    stroke(200, 200, 0)
    line(b_2d.x, b_2d.y, d_2d.x, d_2d.y)
    stroke(0)
    line(c_2d.x, c_2d.y, d_2d.x, d_2d.y)

    ab = dist(0, A, L, B)
    ad = dist(0, A, L, D)
    a_2d = third_point(b_2d, d_2d, ab, ad)
    stroke(0)
    line(b_2d.x, b_2d.y, a_2d.x, a_2d.y)
    line(d_2d.x, d_2d.y, a_2d.x, a_2d.y)
    rect(0, 0, L, L)

def keyPressed():
    global A, B, C, D
    if key == "q":
        A += 5
    if key == "a":
        A -= 5
    if key == "w":
        B += 5
    if key == "s":
        B -= 5
    if key == "e":
        C += 5
    if key == "d":
        C -= 5
    if key == "r":
        D += 5
    if key == "f":
        D -= 5

def faces_3D():
    face_draw(((0, 0, 0),  # floor f
               (L, 0, 0),
               (L, L, 0),
               (0, L, 0)))

    face_draw(((0, 0, B),  # face 0
               (L, 0, C),
               (L, 0, 0),
               (0, 0, 0)))

    face_draw(((L, L, D),  # face 1
               (L, 0, C),
               (L, 0, 0),
               (L, L, 0)))

    face_draw(((L, L, D),  # face 2
               (0, L, A),
               (0, L, 0),
               (L, L, 0)))

    face_draw(((0, 0, B),  # face 3
               (0, L, A),
               (0, L, 0),
               (0, 0, 0)))

    face_draw(((0, 0, B),
               (L, L, D),
               (0, L, A)))

    face_draw(((0, 0, B),
               (L, L, D),
               (L, 0, C)))

    stroke(200, 200, 0)
    line(0, 0, B, L, L, D)
