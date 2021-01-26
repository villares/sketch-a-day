from itertools import product, permutations

BORDER = 50
SIZE = 60

def setup():
    size(760, 640)
    background(0)
    grid = list(product(range(BORDER, width - BORDER + 1, SIZE),
                        range(BORDER, height - BORDER + 1, SIZE)))    
    colors = (hex_color('#264653'),
              hex_color('#2a9d8f'), 
              hex_color('#9c46a'), 
              hex_color('#f4a261'),
              hex_color('#e76f51'))

    perms = list(permutations(colors, 4))
    print(len(perms), len(grid))
    
    for i, (x, y) in enumerate(grid):
        if i < len(perms):
            for j, c in enumerate(perms[i]):
                fill(c); noStroke()
                circle(x, y, SIZE - j * 12 - 12)
        
def hex_color(s):
    """
    This function allows you to create color from a string with hex notation in Python mode.
    
    On "standard" Processing (Java) we can use hexadecimal color notation #AABBCC
    On Python mode one can use this notation between quotes, as a string in fill(),
    stroke() and background(), but, unfortunately, not with color().
    """
    if s.startswith('#'):
        s = s[1:]
    return color(int(s[:2], 16), int(s[2:4], 16), int(s[4:6], 16))
