# Exploring https://easings.net/
# https://gist.github.com/zeffii/c1e14dd6620ad855d81ec2e89a859719
i = 0

def setup():
    size(600, 400)
    background(0)
    strokeWeight(5)
    stroke(255)
    colorMode(HSB)
    global easing
    easing = (
        CubicEaseIn, QuadraticEaseIn,
        SineInOut, QuadraticEaseInOut,
        CubicEaseInOut, ExponentialInOut,
        QuadraticEaseOut, CubicEaseOut,
    )
    f = createFont("DejaVu Sans Mono Bold", 24)
    textFont(f)
    draw_name()

        
def draw():
    global i
    w = 480
    x = (2 * frameCount) % w + 3
    t = map(x, 0, w, 0, 1)
    y = height - height * easing[i](t)
    
    stroke(i * 32, 255, 255)
    point(x, y)

    noStroke()
    fill(0)
    circle(width - 50, y, 100)
    fill(i * 32, 255, 255)
    circle(width - 50, y, 50)

    if x >= w:
        fill(0)
        noStroke()
        circle(width - 50, 0, 100)
        i = (i + 1) % len(easing)
        delay(500)
        draw_name()


def QuadraticEaseOut(p):
    return -(p * (p - 2))

def QuadraticEaseIn(p):
    return p * p

def QuadraticEaseInOut(p):
    if p < 0.5:
        return 2 * p * p
    return (-2 * p * p) + (4 * p) - 1

def SineInOut(p):
    return -(cos(PI * p) - 1) / 2

def ExponentialInOut(p):
    if p == 0.0 or p == 1.0:
        return p
    if p < 0.5:
        return 0.5 * pow(2, (20 * p) - 10)
    else:
        return -0.5 * pow(2, (-20 * p) + 10) + 1


def CubicEaseInOut(p):
    """
    y = (1/2)((2x)^3)       ; [0, 0.5)
    y = (1/2)((2x-2)^3 + 2) ; [0.5, 1]
    """
    if p < 0.5:
        return 4 * p * p * p
    else:
        f = ((2 * p) - 2)
        return 0.5 * f * f * f + 1

def CubicEaseIn(p):
    return p * p * p

def CubicEaseOut(p):
    #  y = (x - 1)^3 + 1
    f = (p - 1)
    return f * f * f + 1

def draw_name():
    noStroke()
    fill(0)
    rect(0, 0, 240, 44)
    fill(i * 32, 255, 255)
    textSize(18)
    text(easing[i].__name__, 28, 40)

def keyPressed():
    background(0)
