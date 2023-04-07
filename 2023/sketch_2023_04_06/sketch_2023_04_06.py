from random import choice

options = [10, 30, 50, 70]

def nr_choice(collection):
    """Non-repeating choice"""
    try:
        previous = nr_choice.previous
    except AttributeError:
        previous = None
    c = choice(collection)
    while c == previous:
        c = choice(collection)
    nr_choice.previous = c
    return c

    
def setup():
    size(800, 800)
    color_mode(HSB)
    x = 0
    while x < width:
        c = nr_choice(options)
        fill(c * 3, 200, 200)
        rect(x, 0, c, height)
        x += c