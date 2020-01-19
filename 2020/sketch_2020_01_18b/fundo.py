from __future__ import division

def fundo(nome, img):
    seed = 0
    for c in nome:
        seed += ord(c)
    print(seed) 
    randomSeed(seed)
    noStroke()
    grade(width / 2, height / 2, 40, height, img)
    rectMode(CORNER)
    fill(255)
    noStroke()

def grade(xo, yo, n, tw, img):
    paleta = (color(241, 120, 175),
              color(0, 164, 207),
              color(253, 208, 115),
              color(255)
              )
    cw = tw / n
    offset = (cw - tw) / 2.
    for i in range(n):
        x = xo + offset + cw * i
        for j in range(n):
            y = yo + offset + cw * j
            s = .01
            no = noise(x * s, y * s, mouseX * s)
            if cw > 2  and no < .5:
                grade(x, y, 2, cw, img)
            else:
                c = (i + j) % 3

                if img.get(int(x),
                    int(y)) != color(255): 
                    fill(paleta[c])
                    rectMode(CENTER)
                    noStroke()        
                    square(x, y, cw)
                    c2 = (i - j) % 3
                    if c2 == c:
                        c2 = c - 1 
                    fill(paleta[c2])
                    circle(x, y, cw)
                else:
                    stroke(0)
                    strokeWeight(2)
                    line(x, y, x + 10 * no, y + 10 * no)
