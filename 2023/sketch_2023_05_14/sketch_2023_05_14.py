"""
Code using https://py5coding.org "imported mode" style, learn more
at https://abav.lugaralgum.com/como-instalar-py5/index-EN.html
"""

tam = 30 

def setup():
    size(600, 600)
    fill(0)
    rect_mode(CENTER)
    
def draw():
    background(240)
    rows = cols = width // tam
    for r in range(rows):
        y = tam / 2 + r * tam 
        for c in range(cols):
            x = tam / 2 + c * tam 
            d = 20 - c  - r
            if d > 0:
                circle(x, y, d + 5)
            else:
                square(x, y, d - 5)
            
            
            