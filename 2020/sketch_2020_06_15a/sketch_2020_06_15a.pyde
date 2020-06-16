ga = {'s':[], 'c':[]}
gb = {'s':[], 'c':[]}

def setup():
    global ga, gb
    size(400, 400)
    noFill()
    stroke(255)
    ellipseMode(CORNER)
    grade(ga, 0, 0, width - 1, 4)
    grade(gb, 0, 0, width - 1, 4)

    lga = len(ga)
    lgb = len(gb)
    print(len(ga), len(gb))
    if lga > lgb:
        d = lga - lgb
        # gb += [(' ', random(width), random(height), 0)
        #        for _ in range(d)]
        gb += gb[:d]
    else:
        d = lgb - lga
        # gb += [(' ', random(width), random(height), 0)
        #        for _ in range(d)]
        ga += ga[:d]

    print(len(ga), len(gb))

def draw():
    background(0)
    m = map(mouseX, 0, width, 0, 1)
    for fa, fb in zip(ga['s'], gb['s']):
        x, y, w = lerp_g(fa, fb, m)
        square(x, y, w)
        
    for fa, fb in zip(ga['c'], gb['c']):
        x, y, w = lerp_g(fa, fb, m)
        square(x, y, w)

def lerp_g(fa, fb, t):
    ta = fa[0]
    tb = fb[0]
    tc = ta if t < .5 else tb
    return tuple([tc] + [lerp(ea, eb, t)
                         for ea, eb
                         in zip(fa[1:], fb[1:])
                         ])


def grade(gg, xg, yg, wg, n=None):
    n = n or int(random(1, 5))  # n if n is not None else int(random(1, 5))
    w = wg / float(n)
    for i in range(n):
        x = xg + i * w
        for j in range(n):
            y = yg + j * w
            if n == 1:
                gg['s'].append((x, y, w))
            else:
                if w < 20:
                    gg['c'].append((x, y, w))
                else:
                    grade(gg, x, y, w)
