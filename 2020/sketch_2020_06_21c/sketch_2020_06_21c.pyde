def setup():
    size(400, 400)
    f = createFont('FreeMono Bold', 14)
    textFont(f)

def draw():
    background(0)
    xa, ya = mouseX, mouseY
    xb, yb = 300, 300

    strokeWeight(2)
    stroke(200, 0, 200)
    line(xa, ya, xb, yb)

    stroke(255)
    strokeWeight(1)
    line(xa, ya, xa, yb)
    line(xb, yb, xa, yb)

    dx = xb - xa
    dy = yb - ya
    a = atan2(dy, dx)

    if mousePressed:
        txa, tya = xa, ya
        txb, tyb = xb, yb
        ta = u"ângulo: {:.2f} ({:.2f}°)".format(a, degrees(a))
    else:
        ta = u"ângulo: atan2(yb - ya, xb - xa)"
        txa, tya = 'xa', 'ya'
        txb, tyb = 'xb', 'yb'
    tdx, tdy = 'xb - xa', 'yb - ya'
    
    textAlign(LEFT)
    textSize(16)
    fill(0, 200, 0)
    text(ta, 20, 20)
    textSize(14)
    fill(255)
    text(" {}, {}".format(txa, tya), xa, ya)
    text(" {}, {}".format(txb, tyb), xb, yb)
    textAlign(CENTER)
    text(tdx, (xb + xa) / 2, yb + 20)
    textAlign(RIGHT)
    text(tdy, xa, (yb + ya) / 2)
