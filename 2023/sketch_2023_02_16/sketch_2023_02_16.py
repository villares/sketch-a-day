phi = sqrt(5) / 2 - 0.5

def setup():
    size(600, 600)
    
    background(200)
    for x in range(0, width, 2):
        ya = 90 * number(1)# * random(1)
        line(x, height / 4 - ya, x, height / 4 + ya)
    for x in range(0, width, 2):
        yb = 90 * number(1) * number(1)
        if x % 3: number()
        line(x, height / 2 - yb, x, height / 2 + yb)
    for x in range(0, width, 2):
        yc = 90 * number(1)
        if x % 7: number()
        line(x, 3 * height / 4 - yc, x, 3 * height / 4 + yc)

def number(a=1, b=None, s=[PI/10]):
    if b is None:
        mi, ma = 0, a
    else:
        mi, ma = a, b
    d = ma - mi
    r = (s[0] + phi) % 1
    s[0] = r
    return mi + r * d
    
    
    
    
    