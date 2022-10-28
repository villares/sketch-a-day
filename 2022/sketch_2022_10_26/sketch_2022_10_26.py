from itertools import combinations, permutations
from itertools import combinations_with_replacement
from itertools import product

def setup():
    size(1200, 600)
    color_mode(HSB) # Hue (Matiz), Sat, Bri
    
    cores = []
    for i in range(8):
        cor = color(i * 32, 200, 200)
        cores.append(cor)

    combos = list(combinations(cores, 2))
    print(f'combinations of 8 colors, 2: {len(combos)}')
    x = 0
    w = 12
    for cor_a, cor_b in combos:
        fill(cor_a)
        rect(x, 0, w, height / 5)
        fill(cor_b)
        rect(x, height / 5, w, height / 5)
        x = x + w

    cwr = list(combinations_with_replacement(cores, 2))
    print(f'combinations with replacement of 8 colors, 2: {len(cwr)}')
    x = 0
    w = 12
    for cor_a, cor_b in cwr:
        fill(cor_a)
        rect(x, height / 2, w, height / 4)
        fill(cor_b)
        rect(x, height * 0.75, w, height / 4)
        x = x + w
        
    permuts = list(permutations(cores, 2))
    print(len(permuts))
    x = 500
    w = 10
    for cor_a, cor_b in permuts:
        fill(cor_a)
        rect(x, 0, w, height / 5)
        fill(cor_b)
        rect(x, height / 5, w, height / 5)
        x = x + w

    ps = list(product(cores, cores))
    print(len(ps))
    x = 500
    w = 10
    for cor_a, cor_b in ps:
        fill(cor_a)
        rect(x, height / 2, w, height / 4)
        fill(cor_b)
        rect(x, height * 0.75, w, height / 4)
        x = x + w 