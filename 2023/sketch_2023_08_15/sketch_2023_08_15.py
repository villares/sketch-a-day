

def olho(x, y, tamanho, cor=100):
    no_stroke()
    fill(255)
    ellipse(x, y, tamanho, tamanho / 2)  # x, y, w, h
    fill(cor)
    circle(x, y, tamanho / 2)  # x, y, d
    fill(0)
    circle(x, y, tamanho * 0.1)

def setup():
    size(600, 400)
    no_loop()
    
def draw():
    background(200)
    cores = [50, 120, 170, color(200, 0, 0), color(200, 200, 0)] * 2
    x = 75
    for cor in cores:  
        olho(x , random(100, 300), 50, cor)
        x = x + 50
        
def key_pressed():
    save_frame('###.png')
    redraw()
