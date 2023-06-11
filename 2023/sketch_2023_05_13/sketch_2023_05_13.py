"""
Code using https://py5coding.org "imported mode" style, learn more
at https://abav.lugaralgum.com/como-instalar-py5/index-EN.html
"""

tam = 60 

def setup():
    size(600, 600)
    fill(0)
    
def draw():
    background(240)
    rows = cols = width // tam
    for r in range(rows):
        y = tam / 2 + r * tam 
        for c in range(cols):
            x = tam / 2 + c * tam 
            w = tam * 0.9
            hw = w / 2
            x_down = x + (12 * (c + r)) % w - hw
            triangle(x - hw, y - hw,
                     x + hw, y - hw,
                     x_down, y + hw)
            
            
            