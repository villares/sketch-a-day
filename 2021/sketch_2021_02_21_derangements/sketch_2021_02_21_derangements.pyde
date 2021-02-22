"""
Looking for multually deranged derangements
"""
from itertools import permutations
from random import sample, shuffle
from villares.arcs import var_bar

eight_ways = ((-1, -1), (0, -1), (1, -1),
              (-1,  0),          (1,  0),
              (-1,  1), (0,  1), (1,  1))

def setup():
    global mutual_derrangements
    size(900, 900)
    background(240)
    colorMode(HSB)
    f = createFont("Tomorrow Bold",80)
    textFont(f)
    textAlign(CENTER, CENTER)
    starting = tuple(sample('01234567', 8))
    positions = [{item} for item in starting]
    all_perms = permutations(starting)
    print(len(list(all_perms)))
    
    mutual_derrangements = [starting]
    for p in all_perms:            
        if not any(item in positions[i] for i, item in enumerate(p)):
            mutual_derrangements.append(p)
            for i, item in enumerate(p):
                positions[i].add(item)
    w = 100
    # shuffle(mutual_derrangements)
    
    translate(50, 50)
    for i, d in enumerate(mutual_derrangements):
        for j, item in enumerate(d): 
            strokeWeight(5)
            pos = int(item)
            # stroke(pos * 32, 200, 200)
            
            fill(pos * 32, 200, 200)
            x0, y0 = w / 2 + i * w , w / 2 + j * w 
            x = x0 + eight_ways[pos][0] * w / 2
            y = y0 + eight_ways[pos][1] * w / 2
            circle(x, y, 20) 
            x0 = x0 - eight_ways[pos][0] * w / 2
            y0 = y0 - eight_ways[pos][1] * w / 2
            circle(x0, y0, 20) 
            noFill() 
            var_bar(x0, y0, x, y, w / 6, w / 3)

            
    saveFrame("_sketch_2021_02_21_derangements_D.png")
"""
Normal derrangements:
starting = tuple('ABCD')
all_perms = permutations(starting)
derangements = (p for p in all_perms          
                if not any(item == starting[i] for i, item
                           in enumerate(p)))      
"""
