from random import choice, sample
from itertools import combinations, permutations
from itertools import combinations_with_replacement
from itertools import product

paleta = [
    color(200, 0, 0),
    color(200, 200, 0),
    color(0, 0, 200),
#    color(0, 200, 200),
    color(200, 0, 200),
#    color(200, 100, 0),
    ]

def setup():
    size(600, 500)
    text_size(18)
    x = y = 0
    w = width / len(paleta)
    for cor in paleta:
        fill(cor)
        rect(x, 0, w, 50)
        x = x + w
        
    combos = list(combinations(paleta, 2))
    fill(0)
    text(f'{len(combos)} combinações (ordem não importa)', 0, 95)
    w = width / len(combos)
    x, y = 0, y + 100
    for cor_a, cor_b in combos:
        fill(cor_a)
        rect(x + 3, y, w - 6, 25)
        fill(cor_b)
        rect(x + 3, y + 25, w - 6, 25)
        x = x + w

    combos_r = list(combinations_with_replacement(paleta, 2))
    fill(0)
    text(f'{len(combos_r)} combinações com repetição (combinations_with_replacement)', 0, 195)
    w = width / len(combos_r)
    x, y = 0, y + 100
    for cor_a, cor_b in combos_r:
        fill(cor_a)
        rect(x + 3, y, w - 6, 25)
        fill(cor_b)
        rect(x + 3, y + 25, w - 6, 25)
        x = x + w

    perm = list(permutations(paleta, 2))
    fill(0)
    text(f'{len(perm)} permutações (permutations)', 0, 295)
    w = width / len(perm)
    x, y = 0, y + 100
    for cor_a, cor_b in perm:
        fill(cor_a)
        rect(x + 3, y, w - 6, 25)
        fill(cor_b)
        rect(x + 3, y + 25, w - 6, 25)
        x = x + w

#    prod = list(product(paleta, repeat=2))
    prod = list(product(paleta, paleta))
    fill(0)
    text(f'{len(prod)} pares de produto (product) parece uma permutação com repetição', 0, 395)
    w = width / len(prod)
    x, y = 0, y + 100
    for cor_a, cor_b in prod:
        fill(cor_a)
        rect(x + 3, y, w - 6, 25)
        fill(cor_b)
        rect(x + 3, y + 25, w - 6, 25)
        x = x + w
        
    save(f'{__file__[:-3]}.png')