from collections import OrderedDict
from interface import option_pane, multiline_pane

list_a = ["A", "B", "C", "D", "F"] 
missing = []

def setup():
    global terms
    size(600, 400)
    fill(0); textFont(createFont("Inconsolata Condensed Bold", 24))
    terms = make_od(list_a)
    
def make_od(terms):
    return OrderedDict((t, "value " + str(t)) for t in terms if t.strip())
    
def draw():
    background(230)
    text("OrderedDict: " + repr(terms).replace("), ", "),\n" + " " * 26), 10, 30)
    text("Changed: " + repr(missing), 10, 300)

def rename_term(old_term, new_term):
    global terms
    terms = OrderedDict((new_term if k == old_term else k, v) for k, v in terms.viewitems())
                
def new_elements(a, b):
    return list(set(b) - set(a))

def missing_elements(a, b):
    return list(set(a) - set(b))

def mousePressed():
    global missing, terms
    result = multiline_pane(default="\n".join(terms))
    proposal = result.split('\n')
    missing = missing_elements(terms, proposal)
    for m in missing:
            ask_to_rename_or_remove(m, proposal)
    # treat items that have not been added by renaming
    # create new keys in the proposal position
    terms = OrderedDict((k, "new!") if (k not in terms) else (k, terms[k]) for k in proposal)
    
def ask_to_rename_or_remove(term, proposal_options):
    REMOVER = "*remover*"
    title = "Renomear ou remover"
    message = "Renomear ou remover {}?".format(term)
    options = [REMOVER, "---"] + proposal_options
    answer = option_pane(title, message, options, default='')
    if answer == REMOVER:
        terms.pop(term, None)
    elif term:
        rename_term(term, answer)


    
