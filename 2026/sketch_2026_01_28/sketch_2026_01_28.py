ns = 0.01 # escala do noise 

T = 10  # tamanho dos elementos

def setup():
    size(600, 600)
    color_mode(HSB)
    no_stroke()  # sem contorno
    background(0)
    
def draw():
    #background(200)
    num = int(width / T)
    
    for fila in range(num):
        y = T / 2 + T * fila
        for coluna in range(num):
            x = T / 2 + T * coluna
            d = dist(mouse_x, mouse_y, x, y)
            if d < 60:
                n = noise(x * ns,
                          y * ns,
                          frame_count * 3 * ns)  # 0 a quase 1
                fill(n * 255, 255, 255)
                circle(x, y, T * n / ((30 + d) / 30))
            
def key_pressed():
    if key == 's':
        save_frame('###.png')
