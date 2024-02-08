def setup():
    size (600,600)
    background (159, 112, 153)
    fill(255)
    for x in range(100, 600, 100):
        for y in range(100, 600, 100):      
            azulejo(x, y, 50)
    fill(0)
    for x in range(150, 600, 100):
        for y in range(150, 600, 100):      
            azulejo(x, y, 50)

def azulejo (x, y, d):
    pts = [(x, y - d),
           (x + d, y),
           (x, y + d),
           (x - d, y)]
    begin_shape()
    for vx, vy in pts:
        vertex(vx, vy)
    end_shape(CLOSE)
    