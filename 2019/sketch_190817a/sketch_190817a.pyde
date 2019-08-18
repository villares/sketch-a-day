add_library('geomerative')

def setup():
    size(400, 400)
    strokeWeight(3)
    RG.init(this)

def draw():
    background(100)
    mw, mh = width / 2, height / 2
    translate(mw, mh)

    r0 = RShape.createStar(mouseX - mw, mouseY - mh, 200.0, 80.0, 20)
    r1 = rg_ellipse(mouseX, mouseY, 200, 200, 0)
    r2 = rg_ellipse(mouseX - mw, height -mouseY - mh, 200, 200, QUARTER_PI / 2)
    r3 = rg_rect(mouseX - mw, mouseY - mh, 200, 200)

    resultado = RG.union(r0, r1)
    resultado = RG.diff( resultado, r2 )
    resultado = RG.intersection(resultado, r3)
    RG.shape(resultado)


def rg_rect(x, y, w, h, rot=0):
    r = RShape.createRectangle(0, 0, w, h)
    r.translate(x - w / 2, y - h / 2)
    r.rotate(rot, RPoint(x, y))
    return r

def rg_ellipse(x, y, w, h, rot=0):
    r = RShape.createEllipse(0, 0, w, h)
    r.translate(x - w / 2, y - h / 2)
    r.rotate(rot, RPoint(x, y))
    return r
