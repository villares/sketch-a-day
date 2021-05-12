from itertools import combinations

def setup():
    size(500, 500)
    pts = [(sin(i * TWO_PI / 8) * 240,
            cos(i * TWO_PI / 8) * 240)
           for i in range(8)]
    n = 1
    for k in range(3, 9):
        combos = list(combinations(pts, k))
        for s in combos:
            out = createGraphics(500, 500)
            beginRecord(out)
            colorMode(HSB)
            background(255)
            strokeWeight(3)
            translate(250, 250)
            fill(len(s) * 28, 255, 255)
            beginShape()
            for x, y in s:
                vertex(x, y)
            endShape(CLOSE)
            resetMatrix()
            endRecord()
            out.save("{:03}.png".format(n))
            n += 1
