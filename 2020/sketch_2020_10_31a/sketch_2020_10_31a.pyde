""" Exclusive categories """

def setup():
    global terms
    size(600, 600)
    textSize(14)
    terms = setup_terms()

def draw():
    if keyPressed:
        background(0, 100, 200)        
    else:
        background(0, 200, 100)
    draw_terms()

def draw_terms():
    for term in terms:
        x, y = terms[term]['x'], terms[term]['y']
        w, h = terms[term]['w'], terms[term]['h']
        noFill()
        # rect(x, y, w, h)
        selected = terms[term]['state']
        if selected:
            fill(255)
        else:
            fill(0)
        if mouse_over_term(term):
            fill(255, 128 * selected, 128 * selected)
        text(term, x, y + h * 0.75)

def mouseReleased():
    if keyPressed:
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
    return (x < mouseX < x + w
            and y < mouseY < y + h)

def pos(i, t, lw, lh=25, wgap=20, hgap=2):
    # set pos.x, pos.xo, pox.y before you call this
    pos.tw = textWidth(t)
    if pos.x + pos.tw > lw:
        pos.x = pos.xo
        pos.y += lh + hgap
    x = pos.x
    pos.x += pos.tw + wgap
    return x

def setup_terms():
    lines = loadStrings("terms.txt")
    term_names = [term for term in lines[200:]
                 if term and not '(' in term
                 and not term.startswith('\t')]
    pos.x = pos.xo = pos.y = 20  # initial x and y
    return {term: {'state': False,
                  'x': pos(i, term, width),
                  'y': pos.y,
                  'w': pos.tw,
                  'h': 20,
                  }
            for i, term in enumerate(term_names)}
