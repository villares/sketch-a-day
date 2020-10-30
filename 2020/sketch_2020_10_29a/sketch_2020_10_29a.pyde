cat = 0

def setup():
    global tag_names, categorias, tags
    size(400, 400)
    textSize(18)
    categorias = loadStrings("categorias.txt")
    print categorias[cat]
    tags = setup_tags()

def draw():
    background(100, 0, 100)
    draw_tags()

def draw_tags():
    for tag in tags:
        x, y = tags[tag]['x'], tags[tag]['y']
        w, h =  tags[tag]['w'], tags[tag]['h']
        noFill()
        rect(x, y, w, h)
        if tags[tag]['state']:
            fill(200, 0, 0)
        elif mouse_over_tag(tag):
            fill(255)
        else:
            fill(0)
        text(tag, x, y + h * 0.75)

def mouseReleased():
    for tag in tags:
        if mouse_over_tag(tag):
            tags[tag]['state'] ^= 1
            
def mouse_over_tag(tag):
    x, y = tags[tag]['x'], tags[tag]['y']
    w, h = tags[tag]['w'], tags[tag]['h']
    return (x < mouseX < x + w
            and y < mouseY < y + h)

def setup_tags():
    pos = lambda i : 10 + i * 30 
    tag_names = loadStrings("tags.txt")
    return {tag: {'state': False,
                  'x': 30 if pos(i) < height else 200,
                  'y': pos(i) if pos(i) < height else 10 + pos(i) - height,
                  'w': textWidth(tag),
                  'h': 20,
                  }
            for i, tag in enumerate(tag_names)}
