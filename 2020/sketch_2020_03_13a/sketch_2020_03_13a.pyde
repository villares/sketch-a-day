"""
MandelbrotSet
https://rosettacode.org/wiki/Mandelbrot_set#Processing
Processing 3.4
2017-09-23 Noel
2020-03-13 Alexandre (Python Mode)
Task: Generate and draw the Mandelbrot set.
Note that there are many algorithms to draw Mandelbrot set
and there are many functions which generate it .
"""

# Click on an area to zoom in.
# Choose areas with multiple colors for interesting zooming.

def setup():
    global x, y, zr, zi, zr2, zi2, cr, ci, n
    global zmx1, zmx2, zmy1, zmy2, f, di, dj
    global fn1, fn2, fn3, re, gr, bl, xt, yt, i, j
    size(500, 500)
    i = di = dj = 0
    f = 10
    fn1 = random(20)
    fn2 = random(20)
    fn3 = random(20)
    zmx1 = int(width / 4)
    zmx2 = 2
    zmy1 = int(height / 4)
    zmy2 = 2


def draw():
    global x, y, zr, zi, zr2, zi2, cr, ci, n
    global zmx1, zmx2, zmy1, zmy2, f, di, dj
    global fn1, fn2, fn3, re, gr, bl, xt, yt, i, j

    if i <= width:
        i += 1
    x = float(i + di) / zmx1 - zmx2
    for j in range(height + 1):
        y = zmy2 - float(j + dj) / zmy1
        zr = zi = zr2 = zi2 = 0
        cr, ci = x, y
        n = 1
        while n < 200 and (zr2 + zi2) < 4:
            zi2 = zi * zi
            zr2 = zr * zr
            zi = 2 * zi * zr + ci
            zr = zr2 - zi2 + cr
            n += 1

        re = (n * fn1) % 255
        gr = (n * fn2) % 255
        bl = (n * fn3) % 255
        stroke(re, gr, bl)
        point(i, j)


def mousePressed():
    global x, y, zr, zi, zr2, zi2, cr, ci, n
    global zmx1, zmx2, zmy1, zmy2, f, di, dj
    global fn1, fn2, fn3, re, gr, bl, xt, yt, i, j
    background(200)
    xt, yt = mouseX, mouseY
    di = di + xt - width / 2.
    dj = dj + yt - height / 2.
    zmx1 = zmx1 * f
    zmx2 = zmx2 * (1. / f)
    zmy1 = zmy1 * f
    zmy2 = zmy2 * (1. / f)
    di, dj = di * f, dj * f
    i = j = 0
