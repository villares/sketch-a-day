from __future__ import division

def fundo(nome, margem=20, borda=36):
    seed = 0
    for c in nome:
        seed += ord(c)
    print(seed) 
    randomSeed(seed)
    noStroke()
    grade(width / 2, height / 2, 3, height)
    rectMode(CORNER)
    fill(255)
    noStroke()
    rect(0, 0, width, margem)
    rect(0, 0, margem, height)
    rect(margem + borda, margem + borda,
         width - 2 * borda - 2 * margem,
         height - 2 * borda - 2 *margem)
    rect(width - margem, 0, margem, height)
    rect(0, height - margem, width, margem)


def grade(xo, yo, n, tw):
    paleta = (color(241, 120, 175),
              color(0, 164, 207),
              color(253, 208, 115),
              )
    cw = tw / n
    offset = (cw - tw) / 2.
    for i in range(n):
        x = xo + offset + cw * i
        for j in range(n):
            y = yo + offset + cw * j
            if cw > 10 and random(10) < 7:
                grade(x, y, 3, cw)
            else:
                fill(paleta[(i + j) % 3])
                # fill(127 + i*32 - j*64)
                # t = "i{} j{} t{}".format(i, j, (127 + i*32 - j*64))
                rectMode(CENTER)
                square(x, y, cw)
                fill(paleta[(i - j) % 3])
                circle(x, y, cw)
