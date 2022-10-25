# colorful tree / árvore colorida
 
def setup():
    size(600, 600)
    color_mode(HSB)

def draw(): # laço/loop principal (ele fica repetindo)
    background(240)
    galho(300, 500, 90, -HALF_PI)
    
def galho(x, y, length, direction):
    nx = x  + length * cos(direction)
    ny = y  + length * sin(direction)
    angle = radians(30)
    stroke((20 * direction) % 255, 200, 200)
    line(x, y, nx, ny) #x1, y1, x2, y2
    shorten = 0.8 # reduz 20% quando multiplica
    if length > 5:
        galho(nx, ny, length * shorten, direction + angle)
        galho(nx, ny, length * shorten, direction - angle)