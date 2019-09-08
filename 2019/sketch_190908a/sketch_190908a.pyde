def setup():
    size(500, 500)
    fill(200, 0, 0) # red fill
    stroke(0, 0, 200)  # blue stroke
    strokeWeight(15)
    star(250, 250, 7, 200, 100) # 7 pointed star

def star(x, y, np, re, ri):
    """
    draw a star with np tips
    external radius re, internal radius ri
    """ 
    pushMatrix()
    translate(x, y)
    n = np * 2
    ang = radians(360. / n)
    beginShape()
    for i in range(n):
        if i % 2 == 0: r = ri
        else: r = re
        x = sin(ang * i) * r
        y = cos(ang * i) * r
        vertex(x, y)
    endShape(CLOSE)
    popMatrix()
