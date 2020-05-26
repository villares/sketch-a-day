# Exploring https://easings.net/
# https://gist.github.com/zeffii/c1e14dd6620ad855d81ec2e89a859719
import inspect

i = 0
easing_func = []  # easing functions

def setup():
    global l1, l2, f1, f2
    size(500, 500)
    f1 = createFont("DejaVu Sans Mono Bold", 24)
    f2 = createFont("Inconsolata", 12)

    l1 = createGraphics(500, 500)
    l1.beginDraw()
    l1.blendMode(REPLACE)
    l1.colorMode(HSB)
    l1.strokeWeight(5)
    l1.endDraw()

    l2 = createGraphics(500, 500)
    l2.beginDraw()
    l2.blendMode(REPLACE)
    l2.colorMode(HSB)
    l2.endDraw()

def draw():
    global i
    background(0)
    h, w = 400, 500
    x = (2 * frameCount) % w
    t = map(x, 0, w, 0, 1)
    y = height - (height - h) / 2 - h * easing_func[i](t)

    l1.beginDraw()
    l1.stroke(i * 32, 255, 255)
    l1.fill(i * 32, 255, 255)
    l1.point(x, y)
    l1.endDraw()

    l2.beginDraw()
    l2.clear()
    l2.fill(i * 32, 255, 255)
    l2.circle(width / 2, y, 40)
    l2.endDraw()

    draw_func_names(l2)
    draw_def(l2)

    image(l1, 0, 0)
    image(l2, 0, 0)

    if x + 2 >= w:
        i = (i + 1) % len(easing_func)
        delay(500)
        if i == 0:
            noLoop()

def keyPressed():
    background(0)
    loop()

def register(lst):
    def wrapper(f):
        lst.append(f)
        return f
    return wrapper

@register(easing_func)
def cubic_ease_in(p):
    return p ** 3

@register(easing_func)
def quadratic_ease_in(p):
    return p ** 2

# @register(easing_func)
# def sine_in_out(p):
#     return -(cos(PI * p) - 1) / 2

@register(easing_func)
def quadratic_ease_in_out(p):
    if p < 0.5:
        return 2 * p ** 2
    return (-2 * p ** 2) + (4 * p) - 1

@register(easing_func)
def cubic_ease_in_out(p):
    """
    y = (1/2)(2x)³        ; [0, 0.5)
    y = (1/2)(2x-2)³ + 2) ; [0.5, 1]
    """
    if p < 0.5:
        return 4 * p ** 3
    else:
        f = ((2 * p) - 2)
        return 0.5 * f ** 3 + 1

@register(easing_func)
def exponential_in_out(p):
    if p == 0.0 or p == 1.0:
        return p
    if p < 0.5:
        return 2 ** ((20 * p) - 10) / 2
    else:
        return -0.5 * 2 ** ((-20 * p) + 10) + 1

@register(easing_func)
def linear(p):
    return p

# @register(easing_func)
# def quadratic_ease_out(p):
#     return -(p * (p - 2))

# @register(easing_func)
# def cubic_ease_out(p):
#     """
#     y = (x - 1)³ + 1
#     """
#     f = (p - 1)
#     return f ** 3 + 1

# @register(easing_func)
def circular_ease_out(p):
    return sqrt((2 - p) * p)

@register(easing_func)
def back_ease_in_out(p):
    c1 = 1.70158
    c2 = c1 * 1.525
    p2 = p * 2
    if p < 0.5:
        return (p2 ** 2 * ((c2 + 1) * p2 - c2)) / 2
    else:
        return ((p2 - 2) ** 2 * ((c2 + 1) * (p2 - 2) + c2) + 2) / 2


def draw_def(pg):
    source = inspect.getsource(easing_func[i])
    a_def = unicode(source[23:], 'utf8')
    pg.beginDraw()
    pg.fill(255)
    pg.textFont(f2)
    pg.textSize(12)
    pg.text(a_def, 15, 180)
    pg.endDraw()

def draw_func_names(pg):
    pg.beginDraw()
    pg.textFont(f1)
    pg.textSize(14)
    for ic in range(i + 1):
        pg.fill(ic * 32, 255, 255)
        pg.text(easing_func[ic].__name__, 15, 25 + ic * 22)
    pg.endDraw()
