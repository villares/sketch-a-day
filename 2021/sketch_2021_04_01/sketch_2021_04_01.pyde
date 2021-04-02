from __future__ import division
from itertools import combinations

picks = 4 
colunas = 21
filas = 10

def setup():
    size(21 * 20, 10 * 20)
    num_options = tuple(range(10))
    noLoop()
    possible_combos = list(combinations(num_options, picks))
    print(len(list(possible_combos)))    
    global f, escala
    escala = 5
    f = createGraphics(width  * escala, height  * escala)
    beginRecord(f) #  início da gravação
    background(200)
    colorMode(HSB)
    f.scale(escala)
    p = 0
    tam = 20
    for x in range(colunas):
        for y in range(filas):
            for i, c in enumerate(possible_combos[p]):
                push()
                noStroke()
                # fill(c * 25, 200, 200)  # primeira tentativa
                fill((c * 50) % 255, 250, 200 - c * 10)
                translate(x * tam , y * tam)
                rect(i * tam / picks, 0, tam / picks, tam)
                pop()
            noFill()
            rect(x * tam, y * tam, tam, tam)
            if p < len(possible_combos) - 1:
                p = p + 1
    endRecord()
    f.save("output_px{}.png".format(tam))
