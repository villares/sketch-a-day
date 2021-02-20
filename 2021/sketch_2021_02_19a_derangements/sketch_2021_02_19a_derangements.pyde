"""
This is my naïve aproach to find derangements with Python... 

I thought I should be looking for multually deranged derangements
(no deragement had any position in common with any other)

Normal derrangements:
starting = tuple('ABCD')
all_perms = permutations(starting)
derangements = (p for p in all_perms          
                if not any(item == starting[i] for i, item
                           in enumerate(p)))    
"""

from itertools import permutations


def setup():
    global mutual_derrangements
    size(800, 800)
    f = createFont("Tomorrow Bold",60)
    textFont(f)
    textAlign(CENTER, CENTER)
    
    starting = tuple('ABCDEFGH')
    positions = [{item} for item in starting]
    all_perms = permutations(starting)
    
    mutual_derrangements = [starting]
    for p in all_perms:            
        if not any(item in positions[i] for i, item in enumerate(p)):
            mutual_derrangements.append(p)
            for i, item in enumerate(p):
                positions[i].add(item)
    
    for i, d in enumerate(mutual_derrangements):
        for j, item in endumerate(d): 
            text(item, w / 2 + i * w, w / 2 + j * w)   
    
