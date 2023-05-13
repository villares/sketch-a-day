"""
Code using https://py5coding.org "imported mode" style, learn more
at https://abav.lugaralgum.com/como-instalar-py5/index-EN.html
"""

tam = 20

def setup():
    size(800, 800)
    fill(0)
    
def draw():
    background(240)
    for x in range(tam, width, tam):
        for y in range(tam, height, tam):
            w = tam * 0.8
            d = dist(x, y, mouse_x, mouse_y)
            triangle(x - w / 2, y - w / 2,
                     x + w / 2, y - w / 2,
                     x + cos(d / 50) * w / 2, y + w / 2)
            
            
            