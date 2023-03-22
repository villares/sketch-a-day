v = 5
esp = 40

def setup():
    size(800, 800)
    

def trapezio(x, y, w, h, varia=0):
    vy = random(-varia, varia) 
    x1, y1 = x + random(-varia, varia), y + vy
    x2, y2 = x + random(-varia, varia) + w, y + vy
    x3, y3 = x + random(-varia, varia)+ w, y + h + vy
    x4, y4 = x + random(-varia, varia), y + h + vy
    quad(x1, y1, x2, y2, x3, y3, x4, y4)
    

def grade(margem, esp, largura, altura, v):
    random_seed(1)  # trava os sorteios
    for x in range(margem, largura - margem , esp):
        for y in range(margem, altura - margem, esp):
            fill(255)
            no_stroke()
            trapezio(x, y, esp / 2, esp / 2, v)
    random_seed(1)  # trava os sorteios
    for x in range(margem, largura - margem , esp):
        for y in range(margem, altura - margem, esp):
            no_fill()
            stroke(0)
            stroke_weight(2)
            trapezio(y, height - x - esp, esp / 2, esp / 2, v)

            

def draw():
    background(100, 100, 200)
    grade(100, esp, width, height, v)
    
def key_pressed():
    if key == 's':
        save_frame(f'{v}-{esp}.png')
                   