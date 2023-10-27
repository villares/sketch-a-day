

def setup():
    size(300, 300)
    background(240)
    blend_mode(MULTIPLY)
    x = y = 50
    fill(255, 255, 0) # amarelo
    rect(x, y, 100, 100)
    fill(0, 255, 255)  # ciano
    rect(x + 50, y + 50, 100, 100)
    fill(255, 0, 255)  # magenta
    rect(x + 25,  y + 75, 100, 100)
