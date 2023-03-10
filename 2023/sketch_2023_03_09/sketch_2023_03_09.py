"""
Code for py5 (py5coding.org) imported mode
"""

def setup():
    size(600, 600)
    background(200, 0, 0)
    no_stroke()
    fill(255, 200, 0)
    star(width / 2, height / 2, 100, 300, 10)
    fill(0, 0, 200)
    star(width / 2, height / 2, 300, 100, 10, TWO_PI / 20)


def star(x, y, radius_a, radius_b, n_points, rot=0):
    step = TWO_PI / n_points
    begin_shape()
    ang = 0
    while ang <= TWO_PI:  # enquanto o ângulo for menor ou igual a 2*PI:
        sx = cos(ang + rot) * radius_a 
        sy = sin(ang + rot) * radius_a
        cx = cos(ang + rot + step / 2.) * radius_b
        cy = sin(ang + rot + step / 2.) * radius_b
        if ang == 0:
            vertex(x + cx, y + cy)
        else:
            quadratic_vertex(x + sx, y + sy, x + cx, y + cy)
        ang += step  # aumente o ângulo um passo
    end_shape()        


    
    
    
