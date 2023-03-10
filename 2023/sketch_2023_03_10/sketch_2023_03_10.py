"""
Code for py5 (py5coding.org) imported mode
"""

def setup():
    size(600, 600)
    draw_combo()
    
    
def draw_combo():
    fill(255, 200, 00)
    rect(0, 0, 600, 600)
    no_stroke()
    fill(0, 0, 200)
    star(width / 2, height / 2, 100, 300, 12)
    fill(200, 0, 0)
    star(width / 2, height / 2, 300, 100, 6, PI / 3)

def star(x, y, radius_a, radius_b, n_points, rot=0):
    step = TWO_PI / n_points
    begin_shape()
    for i in range(n_points + 1):
        ang = i * step + rot
        sx = cos(ang) * radius_a 
        sy = sin(ang) * radius_a
        cx = cos(ang + step / 2.) * radius_b
        cy = sin(ang + step / 2.) * radius_b
        if i == 0:
            vertex(x + cx, y + cy)
        else:
            quadratic_vertex(x + sx, y + sy, x + cx, y + cy)
    end_shape()        


    
    
    
