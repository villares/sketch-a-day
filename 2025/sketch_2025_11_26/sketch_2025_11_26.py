# This code is an example of py5 in imported mode, learn more at <py5coding.org>
# You'll need the py5-run-sketch tool or Thonny's plug-in

elementos = 30
passo = 0.005
z = 0

def setup():
    size(600, 600)
    color_mode(HSB) # Matiz, Sat, Bri
    
def draw():
    background(0)
    # fundo, limpa a tela
    stroke_weight(3)
    w = width / elementos  # largura de um elemento
    for fila in range(elementos):
        y = w * fila + w / 2
        for coluna in range(elementos):
            x = w * coluna + w / 2
            n = noise((x + mouse_x) * passo,
                      (y + mouse_y) * passo,
                      z * passo)
            d = n * w 
            stroke(n * 255, 255, 255)
            #line(x - d / 2, y - d / 2, x + d / 2, y + d / 2)
            push_matrix()
            translate(x, y)
            rotate(TWO_PI * n)
            line(-w/2, 0, w/2, 0)
            pop_matrix()
            
            
def key_pressed():
    global z, passo, elementos
    if key_code == UP:
        z += 1
    elif key_code == DOWN:
        z -= 1
    elif key == 'a':
        passo *= 1.1
    elif key == 'z':
        passo /= 1.1
    elif key == 's':
        elementos += 1
    elif key == 'x':
        elementos -= 1
    elif key == 'p':
        save_frame(f'{elementos}-{passo}-{z}.png')                

