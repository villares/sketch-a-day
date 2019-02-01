from arcs import *

def setup():
    size(500, 500)
    
def draw():
    background(200)
    noStroke()
    var_bar(mouseX, mouseY, 400, 400, 50, 25)
    stroke(0)
    noFill()
    var_bar(400, 100, 200, 350, 50, 100)
    fill(255, 0, 0, 50)
    var_bar(150, 250, 450, 250, 100, 25)
    
