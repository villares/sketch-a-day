from __future__ import division

def fundo(nome, img):
    background(255)
    seed = 0
    for c in nome:
        seed += ord(c)
    print(seed) 
    randomSeed(seed)
    noStroke()
    grade(width / 2, height / 2, 8, height, img)
    rectMode(CORNER)
    fill(255)
    noStroke()

def grade(xo, yo, n, tw, img):
    paleta = (color(241, 120, 175),
              color(0, 164, 207),
              color(253, 208, 115),
              color(128)
              )
    cw = tw / n
    offset = (cw - tw) / 2.
    for i in range(n):
        x = xo + offset + cw * i
        for j in range(n):
            y = yo + offset + cw * j
            if cw > 5 and random(10) < 7 or cw > 50:
                grade(x, y, 3, cw, img)
            else:
                c = (i + j) % 3
                fill(paleta[c])
                # fill(127 + i*32 - j*64)
                # t = "i{} j{} t{}".format(i, j, (127 + i*32 - j*64))
                rectMode(CENTER)
                # square(x, y, cw)
                c2 = (i - j) % 3
                if c2 == c:
                    c2 = c - 1 
                if img.get(int(x),
                           int(y)) != color(255):         
                    fill(paleta[c2])
                else:
                    fill(0)
                square(x, y, cw)
