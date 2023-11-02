def setup():
    size(600, 600)
    
def draw():
    estrela_balao(300, 300, mouse_x, mouse_y, 20) #, w_a=2, w_b=2)

def estrela_balao(x, y, radius_a, radius_b, n_points, rot=0, w_a=1, w_b=1):
    step = TWO_PI / n_points
    begin_shape()
    for i in range(n_points + 1):
        ang = i * step + rot
        sx = cos(ang) * radius_a * w_a
        sy = sin(ang) * radius_a
        cx = cos(ang + step / 2.0) * radius_b * w_b
        cy = sin(ang + step / 2.0) * radius_b
        if i == 0:
            vertex(x + cx, y + cy)
        else:
            quadratic_vertex(x + sx, y + sy, x + cx, y + cy)
    end_shape()