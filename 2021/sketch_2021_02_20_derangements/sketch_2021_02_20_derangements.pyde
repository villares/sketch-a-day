"""
Looking for multually deranged derangements
Is there a simpler way?
(from yersterday's sketch that looks into all permutations)
"""
from itertools import permutations
from random import sample, shuffle

def setup():
    global mutual_derrangements
    size(800, 800)
    background(240)
    colorMode(HSB)
    f = createFont("Tomorrow Bold",80)
    textFont(f)
    textAlign(CENTER, CENTER)
    starting = tuple(sample('01234567', 8))
    positions = [{item} for item in starting]
    all_perms = permutations(starting)
    
    mutual_derrangements = [starting]
    for p in all_perms:            
        if not any(item in positions[i] for i, item in enumerate(p)):
            mutual_derrangements.append(p)
            for i, item in enumerate(p):
                positions[i].add(item)
    w = 100
    shuffle(mutual_derrangements)
    for i, d in enumerate(mutual_derrangements):
        for j, item in enumerate(d): 
            fill(int(item) * 32, 200, 200)
            text(item, w / 2 + i * w - 2, w / 2 + j * w - 6)   
            # rectMode(CENTER)
            # circle(w / 2 + i * w, w / 2 + j * w, w * 0.66)
            
    saveFrame("sketch_2021_02_20_derangements.png")
"""
Normal derrangements:
starting = tuple('ABCD')
all_perms = permutations(starting)
derangements = (p for p in all_perms          
                if not any(item == starting[i] for i, item
                           in enumerate(p)))      
"""
