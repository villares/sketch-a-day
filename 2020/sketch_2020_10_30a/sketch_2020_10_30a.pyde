""" Tags? """

def setup():
    global tag_names, categorias, tags
    size(600, 600)
    textSize(14)
    tags = setup_tags()

def draw():
    background(100, 0, 200)
    draw_tags()

def draw_tags():
    for tag in tags:
        x, y = tags[tag]['x'], tags[tag]['y']
        w, h = tags[tag]['w'], tags[tag]['h']
        noFill()
        # rect(x, y, w, h)
        if tags[tag]['state']:
            fill(255)
        elif mouse_over_ele(tag):
            fill(200, 100, 0)
        else:
            fill(0)
        text(tag, x, y + h * 0.75)

def mouseReleased():
    for tag in tags:
        if mouse_over_ele(tag):
            tags[tag]['state'] ^= 1

def mouse_over_ele(tag):
    x, y = tags[tag]['x'], tags[tag]['y']
    w, h = tags[tag]['w'], tags[tag]['h']
    return (x < mouseX < x + w
            and y < mouseY < y + h)

def pos(i, t):
    pos.w = textWidth(t) + pos.gap
    if pos.x + pos.w > width:
        pos.x = pos.gap
        pos.y += pos.h
    x = pos.x
    pos.x += pos.w
    return x

def setup_tags():
    pos.x = pos.xo = 20
    pos.y, pos.h, pos.gap = 20, 25, 20
    lines = loadStrings("tags.txt")
    tag_names = [term for term in lines
                 if term and not '(' in term
                 and not term.startswith('\t')]
    return {tag: {'state': False,
                  'x': pos(i, tag),
                  'y': pos.y,
                  'w': pos.w,
                  'h': 20,
                  }
            for i, tag in enumerate(tag_names)}
