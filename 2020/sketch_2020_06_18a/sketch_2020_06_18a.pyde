
# Dois dicionários pra guardar duas grades - não sei se isso foi uma boa ideia
ga = {'s': [], 'c': []}  # s para uma lista de quadrados (square)
gb = {'s': [], 'c': []}  # c para uma lista de círculos (circle)

def setup():
    global ga, gb
    size(400, 400)
    noFill()
    strokeWeight(2)
    stroke(255)
    colorMode(HSB)
    ellipseMode(CORNER)
    # Popula as duas grades
    grade(ga, 0, 0, width - 1, 4)
    grade(gb, 0, 0, width - 1, 4)
    fill_in('c')
    fill_in('s')

def fill_in(k):
    # como as grades podem ter numero de itens diferente uma da outra
    # duplica itens da grade com menos itens (eles ficam sobrepostos)
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
    # m = map(mouseX, 0, width, 0, 1)  # para debug com o mouse
    m = (1 + cos(radians(frameCount))) / 2.0

    # para cada dupla de círculos, um de cada grade
    for fa, fb in zip(ga['c'], gb['c']):
        x, y, w = lerp_g(fa, fb, m)   # interpola um círculo intermediário
        stroke((w * 8) % 256, 255, 255)
        circle(x, y, w)
    # para cada dupla de quadrados, um de cada grade
    for fa, fb in zip(ga['s'], gb['s']):
        x, y, w = lerp_g(fa, fb, m)  # interpola um quadrado intermediário
        square(x, y, w)
        stroke((w * 8) % 256, 255, 255)

    if frameCount in (2, 181, 361):
        delay(2000)


def lerp_g(fa, fb, t):
    """ lerp (interpolação linear) para tuplas """
    return tuple([lerp(ea, eb, t)
                  for ea, eb
                  in zip(fa, fb)
                  ])

def grade(gg, xg, yg, wg, n=None):
    """ A função recursiva que popula uma grade """
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
