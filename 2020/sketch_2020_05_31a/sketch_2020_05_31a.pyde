# Exploring https://easings.net/
# https://gist.github.com/zeffii/c1e14dd6620ad855d81ec2e89a859719
import inspect

add_library('gifAnimation')
from gif_export import gif_export

i = 0
easing_func = []  # easing functions

def setup():
    global l1, l2, f1, f2
    size(600, 400)
    f1 = createFont("DejaVu Sans Mono Bold", 24)
    f2 = createFont("Inconsolata Bold", 11)

    l1 = createGraphics(width, height)
    l1.beginDraw()
    l1.blendMode(REPLACE)
    l1.colorMode(HSB)
    l1.strokeWeight(5)
    l1.endDraw()

    l2 = createGraphics(width, height)
    l2.beginDraw()
    l2.blendMode(REPLACE)
    l2.colorMode(HSB)
    l2.endDraw()

def draw():
    global i
    background(240)
    h, w = 330, 600
    x = (2 * frameCount) % w
    t = map(x, 0, w, 0, 1)
    y = height - (height - h) / 2 - h * easing_func[i](t)

    l1.beginDraw()
    l1.stroke(i * 24, 255, 200)
    l1.fill(i * 24, 255, 200)
    l1.point(x, y)
    l1.endDraw()

    l2.beginDraw()
    l2.clear()
    l2.fill(i * 24, 255, 255)
    l2.strokeWeight(3)
    l2.circle(width / 2, y, 40)
    l2.endDraw()

    draw_func_names(l2)
    draw_def(l2)

    image(l1, 0, 0)
    image(l2, 0, 0)

    if frameCount % 4 == 0:
        gif_export(GifMaker,
                   "sketch_2020_05_31a",
                   quality=90,
                   delay=100)

    if x + 2 >= w:
        i = (i + 1) % len(easing_func)
        delay(1000)
        if i == 0:
            background(240)
            draw_func_names(l2, all=True)
            image(l1, 0, 0)
            image(l2, 0, 0)
            noLoop()

def keyPressed():
    background(0)
    loop()


def draw_def(pg):
    source = inspect.getsource(easing_func[i])
    a_def = unicode(source[23:], 'utf8')
    pg.beginDraw()
    pg.fill(0)
    pg.textFont(f2)
    pg.textSize(10)
    pg.text(a_def, 15, 100)
    pg.endDraw()

def draw_func_names(pg, all=False):
    pg.beginDraw()
    if all:
        n = len(easing_func)
        pg.clear()
    else:
        n = i + 1
    pg.textFont(f1)
    pg.textSize(12)
    for ic in range(n):
        pg.fill(ic * 24, 255, 255)
        pg.text(easing_func[ic].__name__, 15, 25 + ic * 22)
    pg.endDraw()

def register(lst):
    def wrapper(f):
        lst.append(f)
        return f
    return wrapper

@register(easing_func)
def double_exponential_sigmoid(x, const=.7):
    """ 
    from Golan Levin
    https://github.com/golanlevin/Pattern_Master
    """
    min_param = 0.0 + EPSILON
    max_param = 1.0 - EPSILON
    a = 1 - constrain(const, min_param, max_param)
    y = 0
    if x <= 0.5:
        y = ((2.0 * x) ** (1.0 / a)) / 2.0
    else:
        y = 1.0 - ((2.0 * (1.0 - x)) ** (1.0 / a)) / 2.0
    return y

@register(easing_func)
def sigmoid_easing(p, const=6):
    """ from John @introscopia """
    m = lerp(-const, const, p)
    return 1 / (1 + exp(-m))

def sigmoidMap(value, start1, stop1, start2, stop2, const=6):
    """ from John @introscopia """
    m = map(value, start1, stop1, -const, const)
    return ((stop2 - start2) * (1 / (1 + exp(-m)))) + start2

# @register(easing_func)
# def cubic_ease_in(p):
#     return p ** 3

# @register(easing_func)
# def quadratic_ease_in(p):
#     return p ** 2

# @register(easing_func)
# def sine_in_out(p):
#     return -(cos(PI * p) - 1) / 2

# @register(easing_func)
# def quadratic_ease_in_out(p):
#     if p < 0.5:
#         return 2 * p ** 2
#     return -2 * p ** 2 + (4 * p) - 1

# @register(easing_func)
# def cubic_ease_in_out(p):
#     if p < 0.5:
#         return 4 * p ** 3
#     else:
#         f = ((2 * p) - 2)
#         return 0.5 * f ** 3 + 1

# @register(easing_func)
# def exponential_in_out(p):
#     if p == 0.0 or p == 1.0:
#         return p
#     if p < 0.5:
#         r = 2 ** ((20 * p) - 10) / 2
#     else:
#         r = -0.5 * 2 ** ((-20 * p) + 10) + 1
#     return r

# @register(easing_func)
# def linear(p):
#     return p

# @register(easing_func)
# def quadratic_ease_out(p):
#     return -(p * (p - 2))

# @register(easing_func)
# def cubic_ease_out(p):
#     f = (p - 1)
#     return f ** 3 + 1

# @register(easing_func)
# def circular_ease_out(p):
#    return sqrt((2 - p) * p)

# @register(easing_func)
# def back_ease_in_out(p):
#     c1 = 1.70158
#     c2 = c1 * 1.525
#     p2 = p * 2
#     if p < 0.5:
#         return (p2 ** 2 * ((c2 + 1) * p2 - c2)) / 2
#     else:
#         return ((p2 - 2) ** 2 * ((c2 + 1) * (p2 - 2) + c2) + 2) / 2
