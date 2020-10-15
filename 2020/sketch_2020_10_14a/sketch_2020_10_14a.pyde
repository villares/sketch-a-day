from villares.line_geometry import Line, line_intersect

def setup():
    size(400, 400)
    # lines = [Line((rw(), rw()), (rw(), rw()))
    #          for _ in range(5) ]
    generate_lines()

def generate_lines():
    global lines
    rw = lambda: random(width)
    lines = []
    while len(lines) < 20:
        li = Line((rw(), rw()), (rw(), rw()))
        for other_li in lines:
            if line_intersect(li, other_li):
                break
        else:
            lines.append(li)


def draw():
    background(0)
    stroke(0, 255, 0)
    for li in lines:
        li.draw()
        int_count = 0
        for other_li in lines:
            line_ints = line_intersect(li, other_li)
            if line_ints:
                int_count += 1
            if int_count > 2:
                break
        else:
            v = PVector(*li.a) - PVector(*li.b)
            v.normalize()
            li.a += v
            li.b -= v

def keyPressed():
    if key == ' ':
        generate_lines()
