from __future__ import division # não use na versão online!

escala = 25

def setup():
    size(800, 800)
    background(200, 200, 240)
    translate(width / 2, height / 2)
    textSize(14)
    textAlign(CENTER, CENTER)
    #text("Oi", 0, 0 )
    stroke(50)  # traço branco
    line(-width / 2, 0, width / 2, 0)
    line(0, -height / 2, 0, height / 2)
    fill(50)
    for i in range(-width // escala, height // escala):
        ie = i * escala
        circle(ie, 0, 2)
        if i != 0:
            circle(0, ie, 2)
            text(-i, -14, ie)
            text(i, ie, 10)
        else:
            text(0, 6, 10)
    scale(1, -1)
    # for x in range(-16, 16):
    for n in range(-16 * escala, 16 * escala):
        x = n / escala
        y = f(x)
        fill(255, 0, 0)
        noStroke()
        circle(x * escala, y * escala, 3)
        # print(x, y)
    
    saveFrame("sketch_2021_05_05b.png") # não use na versão online!

def f(x):
    return (x * 3) / +20 - 10
