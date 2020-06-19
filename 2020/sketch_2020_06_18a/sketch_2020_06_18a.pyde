ga = {'s': [], 'c': []}
gb = {'s': [], 'c': []}

def setup():
    global ga, gb
    size(400, 400)
    noFill()
    strokeWeight(2)
    stroke(255)
    colorMode(HSB)
    ellipseMode(CORNER)
    grade(ga, 0, 0, width - 1, 4)
    grade(gb, 0, 0, width - 1, 4)
    fill_in('c')
    fill_in('s')

def fill_in(k):
    lga, lgb = len(ga[k]), len(gb[k])
    if lga > lgb:
        d = lga - lgb
        # gb[k] += [(random(width), random(height), 0)
        # for _ in range(d)]
        gb[k] += gb[k][:d]
    else:
        d = lgb - lga
        # gb[k]+= [(random(width), random(height), 0)
        # for _ in range(d)]
        ga[k] += ga[k][:d]
    print(len(ga[k]), len(gb[k]))


def draw():
    background(0)
    # m = map(mouseX, 0, width, 0, 1)
    m = (1 + cos(radians(frameCount))) / 2.0

    for fa, fb in zip(ga['c'], gb['c']):
        x, y, w = lerp_g(fa, fb, m)
        stroke((w * 8) % 256, 255, 255)
        circle(x, y, w)

    for fa, fb in zip(ga['s'], gb['s']):
        x, y, w = lerp_g(fa, fb, m)
        square(x, y, w)
        stroke((w * 8) % 256, 255, 255)

    if frameCount in (2, 181, 361):
        delay(2000)


def lerp_g(fa, fb, t):
    return tuple([lerp(ea, eb, t)
                  for ea, eb
                  in zip(fa, fb)
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
