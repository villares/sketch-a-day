from random import choice, sample
from itertools import combinations, permutations
from itertools import combinations_with_replacement
from itertools import product

colors = [
    color(200, 0, 0),
    color(200, 100, 0),
    color(200, 200, 0),
    color(0, 200, 0),
    color(0, 200, 200),
    color(0, 0, 200),
    color(150, 0, 200),    
    ]

def setup():
    size(900, 450)
    background(0)
    text_size(18)
    no_stroke()
    translate(25, 15)
    x = 0
    y = 20
    w = (width - 50) / len(colors)
    fill(255)
    text(f'{len(colors)} colors', 0, y - 5)
    for cor in colors:
        fill(cor)
        rect(x + 3, y, w - 6, w)
        x = x + w 
    y = y - w + 10
    
    combos = list(combinations(colors, 2))
    tc = f'{len(combos)} pairs from itertools.combinations(colors, 2)'
    combos_r = list(combinations_with_replacement(colors, 2))
    tcr = f'{len(combos_r)} pairs from itertools.combinations_with_replacement(colors, 2)'
    perm = list(permutations(colors, 2))
    tpe = f'{len(perm)} pairs from itertools.permutations(colors, 2)'
    prod = list(product(colors, colors))
    tpr = f'{len(prod)} pairs from itertools.product(colors, colors)'

    for pairs, txt in (
        (combos, tc),
        (combos_r, tcr),
        (perm, tpe),
        (prod, tpr),
        ):
    
        x, y = 0, y + w * 2 + 15
        w = (width - 50) / len(pairs)
        fill(255)
        text(txt, 0, y - 5)
        for cor_a, cor_b in pairs:
            fill(cor_a)
            rect(x + 3, y, w - 6, w - 6)
            fill(cor_b)
            rect(x + 3, y + w - 6, w - 6, w - 6)
            x = x + w
        
    save(f'{__file__[:-3]}.png')