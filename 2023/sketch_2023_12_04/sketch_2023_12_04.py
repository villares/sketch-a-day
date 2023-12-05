def setup():
    size(600, 600)

def draw():
    background(200)
    no_fill()
    xa, ya = 200, 200
    xb, yb = 400, 200
    xc, yc = mouse_x, mouse_y
    ra, rb, rc = raios_tangentes(xa, ya, xb, yb, xc, yc)
    circle(xa, ya, ra * 2)
    circle(xb, yb, rb * 2)
    circle(xc, yc, rc * 2)

    
def raios_tangentes(xa, ya, xb, yb, xc, yc):
    # lados
    a = sqrt(((xb - xc) ** 2) + ((yb - yc) ** 2))
    b = sqrt(((xc - xa) ** 2) + ((yc - ya) ** 2))
    c = sqrt(((xa - xb) ** 2) + ((ya - yb) ** 2))
    # semiperĩmetro
    s = (a + b + c) / 2
    try:
        ra = min(s - a, sqrt(s * (s - a)))
        rb = min(s - b, sqrt(s * (s - b)))
        rc = min(s - c, sqrt(s * (s - c)))
    except ValueError:
        print('problema')
        return(1, 1, 1)
    return (ra, rb, rc)

