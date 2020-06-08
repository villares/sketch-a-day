# D'aprés @ntsutae つぶやきProcessing
# https://twitter.com/ntsutae/status/1268432505356513280?s=20

t = 0
a, b, c = 1, 256, 128
def setup():
    size(512, 512)
    noSmooth()
    colorMode(HSB)
def draw():
    global t
    t += 1
    background(0)
    s = 1
    scale(s)
    w = width // s
    for x in range(w):
        for y in range(w):
            p = (-t + abs((x + y) | (x - y + t * 2))
                 ** a) % b
            # delay(1)
            if p < c:
                px = color(p % 256, 255, 255)
                # for ix, iy in ((x * 2, y * 2),
                #                (x * 2 + 1, y * 2),
                #                (x * 2, y * 2 + 1),
                #                (x * 2 + 1, y * 2 + 1)):
                    # set(ix, iy, px)
                set(x, y, px)

def keyPressed():
    global a, b, c
    if key == 'a':
        a += .1
    if key == 'z' and a > 1:
        a -= .1
    if key == 's':
        b += 1
    if key == 'x' and b > 1:
        b -= 1
    if key == 'd':
        c += 1
    if key == 'c' and c > 1:
        c -= 1
    print(a, b, c)

# First ported from @ntsutae code for a single tweet
# t=0;w=720#つぶやきProcessing d'aprés @ntsutae
# def setup():size(w,w)
# def draw():
#  global t;t+=1;scale(3);background(-1)
#  for y in range(240):
#   for x in range(240):
#    (t+abs((x+y-t)^(x-y+t))**3)%1023<109 and point(x,y)
