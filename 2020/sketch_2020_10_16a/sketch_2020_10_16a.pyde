from villares.line_geometry import Line, line_intersect

from random import choice

def setup():
    size(400, 400)
    generate_lines()

def generate_lines():
    global lines
    rw = lambda: choice(range(10, width, 10))
    lines = []
    while len(lines) < 50:
        li = Line((rw(), rw()), (rw(), rw()))
        for other_li in lines:
            # ca = other_li.point_colinear(li.a.x, li.a.y)
            # cb = other_li.point_colinear(li.b.x, li.b.y)
            if li.intersect(other_li):  # or ca or cb:
                break
        else:
            li.grow_a = True
            li.grow_b = True
            lines.append(li)

def draw():
    background(0)
    # lines.sort(key = lambda li : li.dist())
    for li in lines:
        for other_li in lines:
            if li is not other_li:
                if li.grow_a and other_li.point_over(li.a.x, li.a.y, 0.01):
                    li.grow_a = False
                if li.grow_b and other_li.point_over(li.b.x, li.b.y, 0.01):
                    li.grow_b = False
        # red line
        if li.point_over(int(frameCount) % width, height / 2):
            stroke(255, 0, 0)
        else:
            stroke(0, 0, 200)

        strokeWeight(2)
        li.draw()

    for li in lines:
        v = PVector(*li.a) - PVector(*li.b)
        v.normalize()
        noStroke()
        fill(0, 255, 200)
        if li.grow_a:
            li.a += v / 2
        else:
            circle(li.a.x, li.a.y, 3)
        if li.grow_b:
            li.b -= v / 2
        else:
            circle(li.b.x, li.b.y, 3)


def keyPressed():
    if key == ' ':
        generate_lines()
