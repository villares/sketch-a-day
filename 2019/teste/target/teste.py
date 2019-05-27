from pytop5js import *

def setup():
    colorMode(HSB)
    createCanvas(500, 500)


def draw():
    push()
    rect(10, 10, 100, 100)
    pop()

# ==== This is required by pyp5js to work

# Register your events functions here
event_functions = {
    # "keyPressed": keyPressed,    as an example
}
start_p5(setup, draw, event_functions)
