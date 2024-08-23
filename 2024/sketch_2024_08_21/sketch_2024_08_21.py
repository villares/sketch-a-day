def setup():
    size(500, 500)
    fill('red')
    stroke('red')
    ponta(100, 500, 200, 100, 50)
    ponta2(200, 500, 300, 100, 50)
    save_frame('out.png')

def ponta(xa, ya, xb, yb, tam):
    stroke_weight(tam)
    line(xa, ya, xb, yb)  # corpo com tamanho fixo
    ang = atan2(yb - ya, xb - xa)
    push() # combines push_matrix() and push_style()
    translate(xb, yb)
    rotate(ang)
    no_stroke()
    rect(-tam/2, -tam, tam, 3 * tam / 2,
         tam / 2, 0, tam / 2, 0)  # corner radius
    fill(255)
    circle(tam / 4, -tam * 2 / 3, tam / 4)
    pop()  # combines pop_matrix() and pop_style()

def ponta2(xa, ya, xb, yb, tam):
    stroke_weight(tam)
    line(xa, ya, xb, yb)  # corpo com tamanho fixo
    ang = atan2(yb - ya, xb - xa)
    push()
    translate(xb, yb)
    rotate(ang)
    no_stroke()
    fill('red')
    rect(-tam/2 + tam / 3, -tam, 3 * tam / 4 , 3 * tam / 2,
         0, tam / 2, tam / 2, 0)
    fill(255)
    circle(tam / 4, -tam * 2 / 3, tam / 4)
    pop()



