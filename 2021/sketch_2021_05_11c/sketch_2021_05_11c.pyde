from itertools import permutations

def setup():
    size(500, 500)
    strokeJoin(ROUND)
    pts = [(sin(i * TWO_PI / 5) * 200,
            cos(i * TWO_PI / 5) * 200)
           for i in range(5)]
    n = 1
    for k in range(3, 6):
        combos = sorted(list(permutations(pts, k)))
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
            fill(0)
            for i, (x, y) in enumerate(s):
                circle(x, y, i * 5) 
            resetMatrix()
            endRecord()
            out.save("{:03}.png".format(n))
            n += 1
