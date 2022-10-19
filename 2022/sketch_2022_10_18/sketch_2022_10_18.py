"""
Thonny + py5 imported mode @ Python Brasil 2022 Manaus
"""

def setup():
    size(600, 600)  # largura e altura do desenho
    background(100, 0, 100)  # Red, Green, Blue
    #no_stroke()

def draw():
    peixe(100, 100, 100, 50)
    peixe(200, 200, 50, 25)


def peixe(x, y, lp, ap):
    cabeca_cauda = lp * 0.66
    fill(255, 0, 0)
    rect(x, y, lp, ap)
    fill(0, 0, 200)
    triangle(x, y, x,
             y + ap, x - cabeca_cauda / 2, y + ap / 2)
    triangle(x + lp, y, x + lp,
             y + ap, x + cabeca_cauda / 2 + lp, y + ap / 2)
    triangle(x + lp + cabeca_cauda, y, x + lp + cabeca_cauda,
             y + ap, x + lp + cabeca_cauda / 2, y + ap / 2)
    
