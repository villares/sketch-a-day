
line_height = 60

def setup():
    global terms
    size(600, 600)
    text_size(line_height)
    color_mode(HSB)
    terms = setup_terms()

def draw():
    background(0, 0, 200)
    draw_terms()

def draw_terms():
    for term in terms:
        x, y = terms[term]['x'], terms[term]['y']
        w, h = terms[term]['w'], terms[term]['h']
        selected = terms[term]['state']
        if mouse_over_term(term):
            no_fill()
            rect(x - 2, y, w + 4, h)
        if selected:
            fill(255)
        else:
            fill(0)
        text(term, x, y + h * 0.75)

def mouse_released():
    if is_key_pressed:
        non_exclusive_selection()
    else:
        exclusive_selection()

def non_exclusive_selection():
    for term in terms:
        if mouse_over_term(term):
            terms[term]['state'] ^= 1

def exclusive_selection():
    for term in terms:
        if mouse_over_term(term):
            terms[term]['state'] = True
        else:
            terms[term]['state'] = False


def mouse_over_term(term):
    x, y = terms[term]['x'], terms[term]['y']
    w, h = terms[term]['w'], terms[term]['h']
    return (x < mouse_x < x + w
            and y < mouse_y < y + h)

def pos(i, t, lw, lh=None, wgap=20, hgap=2):
    # set pos.x, pos.xo, pox.y before you call this
    lh = lh or text_ascent() + text_descent()
    pos.tw = text_width(t)
    if pos.x + pos.tw > lw:
        pos.x = pos.xo
        pos.y += lh + hgap
    x = pos.x
    pos.x += pos.tw + wgap
    return x

def setup_terms():
    ls = load_strings("terms.txt")
    term_names = [term for term in ls
                  if term and not '(' in term
                  and not term.startswith('\t')]
    pos.x = pos.xo = pos.y = 20  # initial x and y
    terms = {term: {'state': False,
                    'x': pos(i, term, width),
                    'y': pos.y,
                    'w': pos.tw,
                    'h': line_height,
                    }
             for i, term in enumerate(term_names)
             }
    println(len(terms))
    return terms
