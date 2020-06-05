"""
via https://twitter.com/ntsutae/status/1267834176381702148?s=20
based on https://twitter.com/ntsutae/status/1267852301697343488?s=20
"""

rotx = PI / 4
roty = PI / 4
t = 0

def setup():
    size(400, 400, P3D)
    global halfWidth, halfHeight
    halfWidth = width / 2.0
    halfHeight = height / 2.0
    textureMode(NORMAL)

def draw():
    background(0)
    noStroke()
    translate(halfWidth, halfHeight, -100)
    rotateX(rotx)
    rotateY(roty)
    scale(120)
    global t
    t += 1
    g = 128
    G = createGraphics(g, g)
    G.beginDraw()
    G.clear()
    G.stroke(255)
    for x in range(g):
        for y in range(g):
            s = x - t
            if y % 32 < 2 or x % 32 < 2: G.point(x, y)
            if (s+y | s-y) + t % 256 < 4:
                G.stroke(t % 256, y % 256, s % 256)
                G.point(x, y)

            # print(s+y, s-y)
            # (((s + y) | (s - y)) ** 2 + t) % 2048 < 1024 and G.point(x, y)
    G.endDraw()
    texturedCube(G)


def texturedCube(tex):
    """
    From the Processing textureCube example by Dave Bollinger

    Given one texture and six faces, we can easily set up the uv coordinates
    such that four of the faces tile "perfectly" along either u or v, but
    the other two faces cannot be so aligned. This code tiles "along" u,
    "around" the X / Z faces and fudges the Y faces - the Y faces are
    arbitrarily aligned such that a rotation along the X axis will put the
    "top" of either texture at the "top" of the screen, but is not
    otherwised aligned with the X / Z faces. (This just affects what type of
    symmetry is required if you need seamless tiling all the way around the cube)
    """
    with beginShape(QUADS):
        texture(tex)
        # +Z "front" face.
        vertex(-1, -1, 1, 0, 0)
        vertex(1, -1, 1, 1, 0)
        vertex(1, 1, 1, 1, 1)
        vertex(-1, 1, 1, 0, 1)

        # -Z "back" face.
        vertex(1, -1, -1, 0, 0)
        vertex(-1, -1, -1, 1, 0)
        vertex(-1, 1, -1, 1, 1)
        vertex(1, 1, -1, 0, 1)

        # +Y "bottom" face.
        vertex(-1, 1, 1, 0, 0)
        vertex(1, 1, 1, 1, 0)
        vertex(1, 1, -1, 1, 1)
        vertex(-1, 1, -1, 0, 1)

        # -Y "top" face.
        vertex(-1, -1, -1, 0, 0)
        vertex(1, -1, -1, 1, 0)
        vertex(1, -1, 1, 1, 1)
        vertex(-1, -1, 1, 0, 1)

        # +X "right" face.
        vertex(1, -1, 1, 0, 0)
        vertex(1, -1, -1, 1, 0)
        vertex(1, 1, -1, 1, 1)
        vertex(1, 1, 1, 0, 1)

        # -X "left" face.
        vertex(-1, -1, -1, 0, 0)
        vertex(-1, -1, 1, 1, 0)
        vertex(-1, 1, 1, 1, 1)
        vertex(-1, 1, -1, 0, 1)

def mouseDragged():
    global rotx, roty
    rate = 0.01
    rotx += (pmouseY - mouseY) * rate
    roty += (mouseX - pmouseX) * rate
