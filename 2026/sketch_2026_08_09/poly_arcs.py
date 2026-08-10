import py5

ROTATION = {0 : 0,
            py5.BOTTOM : 0,
            py5.DOWN : 0,
            1 : py5.HALF_PI,
            py5.LEFT : py5.HALF_PI,
            2 : py5.PI,
            py5.TOP : py5.PI,
            py5.UP : py5.PI,
            3 : py5.PI + py5.HALF_PI,
            py5.RIGHT: py5.PI + py5.HALF_PI,
            py5.BOTTOM + py5.RIGHT : 0,
            py5.DOWN + py5.RIGHT : 0,
            py5.DOWN + py5.LEFT : py5.HALF_PI,
            py5.BOTTOM + py5.LEFT : py5.HALF_PI,
            py5.TOP + py5.LEFT : py5.PI,
            py5.UP + py5.LEFT : py5.PI,
            py5.TOP + py5.RIGHT: py5.PI + py5.HALF_PI,
            py5.UP + py5.RIGHT: py5.PI + py5.HALF_PI,
            }
     
def quarter_poly(x, y, radius, quadrant, num_points=2):
    poly_arc(x, y, radius, ROTATION[quadrant], py5.HALF_PI, num_points)
    
def half_poly(x, y, radius, quadrant, num_points=2):
     poly_arc(x, y, radius, ROTATION[quadrant],py5.PI, num_points)

def poly_arc(x, y, radius, start_ang, sweep_ang, num_points=4):
    angle = sweep_ang / int(num_points)
    a = start_ang
    with py5.begin_shape(): 
        while a <= start_ang + sweep_ang:
            sx = x + py5.cos(a) * radius
            sy = y + py5.sin(a) * radius
            py5.vertex(sx, sy)
            a += angle
    
def bar(x1, y1, x2, y2, thickness=None, shorter=0, ends=(1,1)):
    """
    O código para fazer as barras, dois pares (x, y),
    um parâmetro de encurtamento: shorter
    """
    L = py5.dist(x1, y1, x2, y2)
    if not thickness:
        thickness = 10
    with py5.push_matrix():
        py5.translate(x1, y1)
        angle = py5.atan2(x1 - x2, y2 - y1)
        py5.rotate(angle)
        offset = shorter / 2
        py5.line(thickness/2, offset, thickness/2, L - offset)
        py5.line(-thickness/2, offset, -thickness/2, L - offset)
        if ends[0]:
            half_poly(0, offset, thickness/2, py5.UP)
        if ends[1]:
            half_poly(0,  L - offset, thickness/2, py5.DOWN)