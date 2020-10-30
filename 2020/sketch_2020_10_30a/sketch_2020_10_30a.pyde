""" Tags? """

def setup():
    global tags
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

def pos(i, t, lw, lh=25, wgap=20):
    # set pos.x, pos.xo, pox.y before you call this
    pos.tw = textWidth(t)
    if pos.x + pos.tw > lw:
        pos.x = pos.xo
        pos.y += lh
    x = pos.x
    pos.x += pos.tw + wgap
    return x

def setup_tags():
    lines = loadStrings("tags.txt")
    tag_names = [term for term in lines
                 if term and not '(' in term
                 and not term.startswith('\t')]
    pos.x = pos.xo = pos.y = 20  # initial x and y
    return {tag: {'state': False,
                  'x': pos(i, tag, width),
                  'y': pos.y,
                  'w': pos.tw,
                  'h': 20,
                  }
            for i, tag in enumerate(tag_names)}
