
dados_estrelas = [
    {'x': 400, 'y': 100, 'n': 5, 'raio_a': 50, 'raio_b': 10},
    {'x': 200, 'y': 200, 'n': 7, 'raio_a': 150,'raio_b': 100},
    {'x': 350, 'y': 400, 'n': 20,'raio_a': 80, 'raio_b': 40},
]

def setup():
    size(500, 500)
    
def draw():
    background(0)
    for kwargs in dados_estrelas:
        estrela(**kwargs)

def estrela(x, y, n, raio_a, raio_b, rot=0):    
    passo = TWO_PI / n
    begin_shape() 
    for i in range(n): 
        angulo = i * passo + rot
        vx = x + raio_a * sin(angulo)
        vy = y + raio_a * cos(angulo)
        vertex(vx, vy)
        vx = x + raio_b * sin(angulo + passo / 2)
        vy = y + raio_b * cos(angulo + passo / 2)
        vertex(vx, vy) 
    end_shape(CLOSE)
    
def mouse_wheel(e):
    for d in dados_estrelas:
        if dist(d['x'], d['y'], mouse_x, mouse_y) < d['raio_a']:
            d['raio_a'] += e.get_count()
        
        
        
        
    
    
    