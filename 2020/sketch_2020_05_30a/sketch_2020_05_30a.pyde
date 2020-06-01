# Sigmoid easing by *intro

def setup():
    size(400, 400)
    strokeWeight(3)

def draw():
    background(200)

    #  cinza = map(mouseX, 0, width, 0, 255)
    #  x = map(mouseX, 0, width, 100, 300)
    #  pode ser expresso em forma de t para usar lerp()
    t = map(mouseX, 0, width, 0, 1)
    cinza = lerp(0, 255, t)
    x = lerp(100, 300, t)
    fill(cinza)
    stroke(0, 0, 200)
    circle(x, height * .33, 100)

    e = sigmoidMap(t, 0, 1, 0, 1)
    e_cinza = lerp(0, 255, e)
    e_x = lerp(100, 300, e)
    y = lerp(0, height, e)
    fill(e_cinza)
    stroke(200, 0, 0)
    circle(e_x, height * .66, 100)

    for i in range(1 + mouseX):
        y = sigmoidMap(i, 0, width, 0, height)
        stroke(200, 0, 0)
        point(i, y)
        stroke(0, 0, 200)
        point(i, map(i, 0, width, 100, 300))

# From John @introscopia
def sigmoidMap(value, start1, stop1, start2, stop2):
    c = 6
    m = map(value, start1, stop1, -c, c)
    return ((stop2 - start2) * (1 / (1 + exp(-m)))) + start2
