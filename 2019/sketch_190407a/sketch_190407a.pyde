# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME, OUTPUT = "sketch_190407a", ".gif"

"""
Terrain Box
"""
add_library('GifAnimation')
from gif_exporter import gif_export
add_library('peasycam')
from third_point import third_point
from face_draw import face_draw

diagonal_color = color(0, 100, 200)
Z = 100

def setup():
    global cam
    size(850, 500, P3D)
    cam = PeasyCam(this, 200)
    hint(ENABLE_DEPTH_SORT)
    init_values()

def init_values():
    global L, W, A, B, C, D
    L, W = 100, 100
    A = B = C = D = Z

def draw():
    # lights()
    background(200)
    # ortho()
    strokeWeight(2)
    stroke(0)
    fill(255, 200)
    rotateX(HALF_PI)
    rotateZ(-QUARTER_PI)
    translate(100, 0, -75)
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
    face_draw((c_2d, (L + W, -D), (L + W, 0), (L, 0)))  # face 1
    # face 2
    face_draw(((L + W, -D), (L * 2 + W, -A), (L * 2 + W, 0), (L + W, 0)))
    face_draw(((L * 2 + W, -A), (L * 2 + W * 2, -B),
               (L * 2 + W * 2, 0), (L * 2 + W, 0)))  # face 3

    bc = PVector.dist(b_2d, c_2d)  # (0, 0, -B, L, 0, -C)
    bd = dist(0, 0, B, L, W, D)
    cd = dist(L, 0, C, L, W, D)
    d_2d = third_point(b_2d, c_2d, bd, cd)[0]
    stroke(diagonal_color)
    line(b_2d.x, b_2d.y, d_2d.x, d_2d.y)
    stroke(0)
    line(c_2d.x, c_2d.y, d_2d.x, d_2d.y)

    ab = dist(0, A, L, B)
    ad = dist(0, A, W, D)
    a_2d = third_point(d_2d, b_2d, ab, ad)[1]
    stroke(0)
    line(b_2d.x, b_2d.y, a_2d.x, a_2d.y)
    line(d_2d.x, d_2d.y, a_2d.x, a_2d.y)
    rect(0, 0, L, W)

def keyPressed():
    gif_export(GifMaker, filename=SKETCH_NAME)
    global A, B, C, D, L, W, Z
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
    if key in ("+", "="):
        Z += 5
    if key == "-":
        Z -= 5        
    if keyCode == UP:
        L += 5
    if keyCode == DOWN:
        L -= 5
    if keyCode == RIGHT:
        W += 5
    if keyCode == LEFT:
        W -= 5
    if key == " ": init_values()

def faces_3D():
    face_draw(((0, 0, 0),  # floor f
               (L, 0, 0),
               (L, W, 0),
               (0, W, 0)))

    face_draw(((0, 0, B),  # face 0
               (L, 0, C),
               (L, 0, 0),
               (0, 0, 0)))

    face_draw(((L, W, D),  # face 1
               (L, 0, C),
               (L, 0, 0),
               (L, W, 0)))

    face_draw(((L, W, D),  # face 2
               (0, W, A),
               (0, W, 0),
               (L, W, 0)))

    face_draw(((0, 0, B),  # face 3
               (0, W, A),
               (0, W, 0),
               (0, 0, 0)))

    face_draw(((0, 0, B),
               (L, W, D),
               (0, W, A)))

    face_draw(((0, 0, B),
               (L, W, D),
               (L, 0, C)))

    stroke(diagonal_color)
    line(0, 0, B, L, W, D)
