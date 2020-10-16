from villares.line_geometry import Line, line_intersect

def setup():
    size(400, 400)
    generate_lines()

def generate_lines():
    global lines
    rw = lambda: random(width)
    lines = []
    while len(lines) < 20:
        li = Line((rw(), rw()), (rw(), rw()))
        for other_li in lines:
            if li.intersect(other_li):
                break
        else:
            li.grow_a = True
            li.grow_b = True
            lines.append(li)

def draw():
    background(0)
    stroke(0, 255, 0)
    for li in lines:
        for other_li in lines:
            if li is not other_li and other_li.point_over(li.a.x,li.a.y):
                circle(li.a.x, li.a.y, 5)
                li.grow_a = False
            if other_li.point_over(*li.b):
                li.grow_b = False
                circle(li.b.x, li.b.y, 5)
            
        v = PVector(*li.a) - PVector(*li.b)
        v.normalize()
        if li.grow_a: li.a += v
        if li.grow_b: li.b -= v
        if li.point_over(mouseX, mouseY):
            stroke(255)
        else:
            stroke(200, 0, 0)
        li.draw()

def keyPressed():
    if key == ' ':
        generate_lines()
