def setup():
    size(400, 400)
    background(0)
    noFill()
    stroke(255)
    grade(0, 0, width - 1, 4)
    

def grade(xg, yg, wg, n=None):
    n = n or int(random(1, 5))  # n if n is not None else int(random(1, 5))
    w = wg / float(n)
    for i in range(n):
        x = xg + i * w
        for j in range(n):
            y = yg + j * w
            if n == 1:
                rect(x, y, w, w)
            else:
                if w < 20:
                    ellipse(w/2+x, w/2+y, w, w)
                else:
                    grade(x, y, w)
